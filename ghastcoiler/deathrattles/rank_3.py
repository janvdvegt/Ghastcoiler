import logging

from game.player_board import PlayerBoard
from minions.base import Minion
from deathrattles.base import Deathrattle
from minions.tokens import Spider


class InfestedWolfDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="InfestedWolfDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        # TODO
        pass


class PilotedShredderDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="PilotedShredderDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        # TODO
        pass


class ReplicatingMenaceDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="ReplicatingMenaceDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        # TODO
        pass


class TheBeastDeathrattle(Deathrattle):
    def __init__(self):
        super().__init__(name="TheBeastDeathrattle")

    def trigger(self, minion: Minion, own_board: PlayerBoard, opposing_board: PlayerBoard):
        # TODO
        pass
