import random
import logging

from game.player_board import PlayerBoard
from minions.base import Minion


class GameInstance:
    def __init__(self, player_board_0: PlayerBoard, player_board_1: PlayerBoard, player_turn=None):
        self.player_board = {0: player_board_0, 1: player_board_1}
        self.player_turn = player_turn if player_turn else random.randint(0, 1)
        self.turn = 0

    def print_game(self):
        self.update_attack_and_defense()
        logging.debug("Player 0 board:")
        logging.debug(self.player_board[0].minions_string())
        logging.debug("Player 1 board:")
        logging.debug(self.player_board[1].minions_string())

    def __str__(self):
        self.update_attack_and_defense()
        return_string = "Player 0:\n"
        return_string += str(self.player_board[0]) + "\n\n"
        return_string += "Player 1:\n"
        return_string += str(self.player_board[1])
        return return_string

    def update_attack_and_defense(self):
        for minion in self.player_board[0].get_minions():
            minion.update_attack_and_defense(self.player_board[0], self.player_board[1])
        for minion in self.player_board[1].get_minions():
            minion.update_attack_and_defense(self.player_board[1], self.player_board[0])

    def attacking_player_board(self):
        return self.player_board[self.player_turn]

    def defending_player_board(self):
        return self.player_board[1 - self.player_turn]

    def finished(self):
        return len(self.player_board[0].minions) == 0 or len(self.player_board[1].minions) == 0

    def deal_damage(self, minion, board, amount, poisonous):
        divine_shield_popped = minion.receive_damage(amount, poisonous)
        if divine_shield_popped:
            logging.debug("Divine shield popped")
            board.divine_shield_popped()

    def kill(self, minion, minion_board, opposing_board, minion_defending_player):
        # TODO: Baron
        if minion_defending_player:
            opposing_board.remove_minion(minion)
        else:
            minion_board.remove_minion(minion)
        for deathrattle in minion.deathrattles:
            if minion_defending_player:
                deathrattle.trigger(minion, opposing_board, minion_board)
            else:
                deathrattle.trigger(minion, minion_board, opposing_board)
        self.check_deaths(minion_board, opposing_board)

    def check_deaths(self, current, other):
        for minion in current.get_minions():
            if minion.check_death(current, other):
                self.kill(minion, current, other, minion_defending_player=False)
                return
        for minion in other.get_minions():
            if minion.check_death(other, current):
                self.kill(minion, current, other, minion_defending_player=True)
                return

    def attack(self, attacking_minion: Minion, defending_minion: Minion):
        # TODO: Cleave
        current, other = self.attacking_player_board(), self.defending_player_board()
        logging.debug(f"{attacking_minion.minion_string()} attacks {defending_minion.minion_string()}")
        attacking_minion.on_attack()
        attacking_minion_attack, _ = attacking_minion.total_attack_and_defense(current, other)
        defending_minion_attack, _ = defending_minion.total_attack_and_defense(other, current)
        self.deal_damage(attacking_minion, current, defending_minion_attack, defending_minion.poisonous)
        self.deal_damage(defending_minion, other, attacking_minion_attack, attacking_minion.poisonous)

    def calculate_score_player_0(self):
        if len(self.player_board[0].minions) == 0:
            return - self.player_board[1].score()
        else:
            return self.player_board[0].score()

    def start(self):
        current = self.attacking_player_board()
        other = self.defending_player_board()
        for minion in current.get_minions():
            minion.at_beginning_game(self, True, current, other)
        for minion in other.get_minions():
            minion.at_beginning_game(self, False, other, current)
        while not self.finished():
            self.turn += 1
            logging.debug(f"Turn {self.turn} has started, player {self.player_turn} will attack")
            self.print_game()
            logging.debug('-----------------')
            attacking_minion = self.attacking_player_board().select_attacking_minion()
            defending_minion = self.defending_player_board().select_defending_minion()
            self.attack(attacking_minion, defending_minion)
            self.check_deaths(self.attacking_player_board(), self.defending_player_board())
            logging.debug("=================")
            self.player_turn = 1 - self.player_turn
        logging.debug(self.calculate_score_player_0())
        return self.calculate_score_player_0()
