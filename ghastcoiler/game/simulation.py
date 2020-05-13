from collections import Counter

from game.game_instance import GameInstance


class Simulation:
    def __init__(self, player_board, opponent_board, max_simulations=10000, time_budget_in_milliseconds=1000):
        self.player_board = player_board
        self.opponent_board = opponent_board
        self.max_simulations = max_simulations
        self.time_budget_in_milliseconds = time_budget_in_milliseconds

    def simulate(self):
        scores = []
        for simulation_index in range(self.max_simulations):
            game_instance = GameInstance(player_board_0=self.player_board.copy(), player_board_1=self.opponent_board.copy(), player_turn=simulation_index % 2)
            scores.append(game_instance.start())
        counter = Counter(scores)
        return sorted(counter.items(), key=lambda x: x[0])