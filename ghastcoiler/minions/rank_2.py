import logging

from minions.base import Minion
from minions.types import MinionType

from deathrattles.rank_2 import HarvestGolemDeathrattle, ImprisonerDeathrattle, KaboomBotDeathrattle, \
    KindlyGrandmotherDeathrattle, RatPackDeathrattle, SpawnofNZothDeathrattle, UnstableGhoulDeathrattle


class GlyphGuardian(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Glyph Guardian",
                         rank=2,
                         base_attack=2,
                         base_defense=4,
                         types=[MinionType.Dragon],
                         **kwargs)

    def on_attack(self):
        self.attack *= 2


class HarvestGolem(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Harvest Golem",
                         rank=2,
                         base_attack=2,
                         base_defense=3,
                         types=[MinionType.Mech],
                         base_deathrattle=HarvestGolemDeathrattle(),
                         **kwargs)


class Imprisoner(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Imprisoner",
                         rank=2,
                         base_attack=3,
                         base_defense=3,
                         types=[MinionType.Demon],
                         base_taunt=True,
                         base_deathrattle=ImprisonerDeathrattle(),
                         **kwargs)


class KaboomBot(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Kaboom Bot",
                         rank=2,
                         base_attack=2,
                         base_defense=2,
                         types=[MinionType.Mech],
                         base_deathrattle=KaboomBotDeathrattle(),
                         **kwargs)


class KindlyGrandmother(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Kindly Grandmother",
                         rank=2,
                         base_attack=1,
                         base_defense=1,
                         types=[MinionType.Beast],
                         base_deathrattle=KindlyGrandmotherDeathrattle(),
                         **kwargs)


class MetaltoothLeaper(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Metaltooth Leaper",
                         rank=2,
                         base_attack=3,
                         base_defense=3,
                         types=[MinionType.Mech],
                         # TODO : add battlecry
                         **kwargs)


class MurlocWarleader(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Murloc Warleader",
                         rank=2,
                         base_attack=3,
                         base_defense=3,
                         types=[MinionType.Murloc],
                         **kwargs)

    def gives_attack_defense_bonus(self, other_minion):
        if other_minion.types is MinionType.Murloc:
            if self.golden:
                return 4, 0
            return 2, 0
        return 0, 0


class NathrezimOverseer(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Nathrezim Overseer",
                         rank=2,
                         base_attack=2,
                         base_defense=3,
                         types=[MinionType.Demon],
                         **kwargs)


class OldMurkEye(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="OldMurkEye",
                         rank=2,
                         base_attack=2,
                         base_defense=4,
                         types=[MinionType.Murloc],
                         **kwargs)

    def additional_attack(self, own_board, opposing_board):
        # TODO: +1 attack for each other murloc on the battlefield
        pass


class PogoHopper(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Pogo-Hopper",
                         rank=2,
                         base_attack=1,
                         base_defense=1,
                         types=[MinionType.Mech],
                         **kwargs)


class RatPack(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="RatPack",
                         rank=2,
                         base_attack=2,
                         base_defense=2,
                         types=[MinionType.Beast],
                         base_deathrattle=RatPackDeathrattle(),
                         **kwargs)


class ScavengingHyena(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Scavenging Hyena",
                         rank=2,
                         base_attack=2,
                         base_defense=2,
                         types=[MinionType.Beast],
                         **kwargs)

    def on_other_death(self, other_minion):
        # TODO
        pass


class SpawnofNZoth(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Spawn of N'Zoth",
                         rank=2,
                         base_attack=2,
                         base_defense=2,
                         base_deathrattle=SpawnofNZothDeathrattle(),
                         **kwargs)


class StewardofTime(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Steward of Time",
                         rank=2,
                         base_attack=3,
                         base_defense=4,
                         types=[MinionType.Dragon],
                         **kwargs)


class UnstableGhoul(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Unstable Ghoul",
                         rank=2,
                         base_attack=1,
                         base_defense=3,
                         base_taunt=True,
                         base_deathrattle=UnstableGhoulDeathrattle(),
                         **kwargs)


class WaxriderTogwaggle(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Waxrider Togwaggle",
                         rank=2,
                         base_attack=1,
                         base_defense=2,
                         **kwargs)

    def on_other_death(self, other_minion):
        # TODO: Whenever a friendly Dragon kills an enemy, gain +2/+2.
        pass


class Zoobot(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Steward of Time",
                         rank=2,
                         base_attack=3,
                         base_defense=3,
                         types=[MinionType.Mech],
                         **kwargs)

