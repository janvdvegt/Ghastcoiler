from minions.base import Minion
from minions.types import MinionType


class JoEBot(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Jo-E Bot",
                         rank=1,
                         base_attack=1,
                         base_defense=1,
                         types=[MinionType.Mech],
                         **kwargs)


class DamagedGolem(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Damaged Golem",
                         rank=1,
                         base_attack=2,
                         base_defense=1,
                         types=[MinionType.Mech],
                         **kwargs)


class Imp(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Imp",
                         rank=1,
                         base_attack=1,
                         base_defense=1,
                         types=[MinionType.Demon],
                         **kwargs)


class BigBadWolf(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Big Bad Wolf",
                         rank=1,
                         base_attack=3,
                         base_defense=2,
                         types=[MinionType.Beast],
                         **kwargs)


class Rat(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Rat",
                         rank=1,
                         base_attack=1,
                         base_defense=1,
                         types=[MinionType.Beast],
                         **kwargs)


class Spider(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Spider",
                         rank=1,
                         base_attack=1,
                         base_defense=1,
                         types=[MinionType.Beast],
                         **kwargs)
