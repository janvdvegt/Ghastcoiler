import logging

from game.player_board import PlayerBoard
from minions.base import Minion
from deathrattles.base import Deathrattle
from minions.tokens import DamagedGolem, Imp, BigBadWolf, Rat


class HarvestGolemDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="HarvestGolemDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        logging.debug("Harvest Golem deathrattle triggered, creating Damaged Golem")
        own_board.add_minion(DamagedGolem(golden=minion.golden), position=minion.position)


class ImprisonerDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="ImprisonerDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        logging.debug("Imprisoner deathrattle triggered, creating Imp")
        own_board.add_minion(Imp(golden=minion.golden), position=minion.position)


class KaboomBotDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="KaboomBotDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        if minion.golden:
            logging.debug("Kaboom Bot (golden) deathrattle triggered, dealing 4 damage twice")
        else:
            logging.debug("Kaboom Bot deathrattle triggered, dealing 4 damage")
        number_bombs = 2 if minion.golden else 1
        for bomb in range(number_bombs):
            # TODO: Should kill the unit before throwing a second bomb
            opposing_minion = opposing_board.random_minion()
            opposing_minion.receive_damage(amount=4, poisonous=False)


class KindlyGrandmotherDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="KindlyGrandmotherDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        logging.debug("Kindly Grandmother deathrattle triggered, creating Big Bad Wolf")
        own_board.add_minion(BigBadWolf(golden=minion.golden), position=minion.position)


class RatPackDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="RatPackDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        number_rats = minion.last_attack
        logging.debug(f"Rat pack deathrattle triggered, creating {number_rats} rats")
        for rat in range(number_rats):
            own_board.add_minion(Rat(golden=minion.golden), position=minion.position)


class SpawnofNZothDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="SpawnofNZothDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        logging.debug(f"Spawn of NZoth deathrattle triggered")
        bonus = 2 if minion.golden else 1
        for other_minion in own_board.get_minions():
            other_minion.add_attack(bonus)
            other_minion.add_defense(bonus)


class UnstableGhoulDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="UnstableGhoulDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        logging.debug(f"Unstable Ghoul deathrattle triggered")
        damage = 2 if minion.golden else 1
        for opposing_minion in opposing_board.get_minions():
            opposing_minion.receive_damage(damage=damage, poisonous=False)
