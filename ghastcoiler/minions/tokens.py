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
