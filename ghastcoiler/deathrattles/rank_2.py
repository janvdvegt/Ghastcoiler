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
    # TODO
    pass


class KaboomBotDeathrattle(Deathrattle):
    # TODO
    pass


class KindlyGrandmotherDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="KindlyGrandmotherDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        logging.debug("Kindly Grandmother deathrattle triggered, creating Big Bad Wolf")
        own_board.add_minion(BigBadWolf(golden=minion.golden), position=minion.position)


class RatPackDeathrattle(Deathrattle):
    # TODO
    pass


class SpawnofNZothDeathrattle(Deathrattle):
    # TODO
    pass


class UnstableGhoulDeathrattle(Deathrattle):
    # TODO
    pass

