import logging

from minions.base import Minion
from minions.types import MinionType

from deathrattles.rank_3 import InfestedWolfDeathrattle, PilotedShredderDeathrattle, ReplicatingMenaceDeathrattle,\
    TheBeastDeathrattle


class BronzeWarden(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Bronze Warden",
                         rank=3,
                         base_attack=2,
                         base_defense=1,
                         types=[MinionType.Dragon],
                         base_divine_shield=True,
                         base_reborn=True,
                         **kwargs)


class ColdlightSeer(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Coldlight Seer",
                         rank=3,
                         base_attack=2,
                         base_defense=3,
                         types=[MinionType.Murloc],
                         **kwargs)


class CrowdFavorite(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Crowd Favorite",
                         rank=3,
                         base_attack=4,
                         base_defense=4,
                         **kwargs)


class Crystalweaver(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Crystalweaver",
                         rank=3,
                         base_attack=5,
                         base_defense=4,
                         **kwargs)


class DeflectoBot(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Deflect-o-Bot",
                         rank=3,
                         base_attack=3,
                         base_defense=2,
                         base_divine_shield=True,
                         types=[MinionType.Mech],
                         **kwargs)

    def on_other_enter(self, other_minion):
        if MinionType.Mech in other_minion.types:
            self.divine_shield = True
            if self.golden:
                self.add_attack(2)
            else:
                self.add_attack(1)


class FelvinNavigator(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Felvin Navigator",
                         rank=3,
                         base_attack=4,
                         base_defense=4,
                         types=[MinionType.Murloc],
                         **kwargs)


class HangryDragon(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Hangry Dragon",
                         rank=3,
                         base_attack=4,
                         base_defense=4,
                         types=[MinionType.Dragon],
                         **kwargs)



class Houndmaster(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Houndmaster",
                         rank=3,
                         base_attack=4,
                         base_defense=3,
                         **kwargs)


class ImpGangBoss(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Imp Gang Boss",
                         rank=3,
                         base_attack=2,
                         base_defense=4,
                         types=[MinionType.Demon],
                         **kwargs)

    def on_receive_damage(self):
        # TODO: Summon the 1/1 imp from minions.token
        pass


class InfestedWolf(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Infested Wolf",
                         rank=3,
                         base_attack=3,
                         base_defense=3,
                         base_deathrattle=InfestedWolfDeathrattle(),
                         types=[MinionType.Beast],
                         **kwargs)


class Khadgar(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Khadgar",
                         rank=3,
                         base_attack=2,
                         base_defense=2,
                         **kwargs)

    # TODO: add his text


class PackLeader(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Pack Leader",
                         rank=3,
                         base_attack=3,
                         base_defense=3,
                         **kwargs)

    def on_other_enter(self, other_minion):
        if MinionType.Beast in other_minion.types:
            if self.golden:
                other_minion.add_attack(6)
            else:
                other_minion.add_attack(3)


class PilotedShredder(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Piloted Shredder",
                         rank=3,
                         base_attack=4,
                         base_defense=3,
                         types=[MinionType.Mech],
                         base_deathrattle=PilotedShredderDeathrattle(),
                         **kwargs)


class ReplicatingMenace(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Replicating Menace",
                         rank=3,
                         base_attack=3,
                         base_defense=1,
                         types=[MinionType.Mech],
                         base_deathrattle=ReplicatingMenaceDeathrattle(),
                         **kwargs)


class ScrewjankClunker(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Screwjank Clunker",
                         rank=3,
                         base_attack=2,
                         base_defense=5,
                         types=[MinionType.Mech],
                         **kwargs)


class ShifterZerus(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Shifter Zerus",
                         rank=3,
                         base_attack=1,
                         base_defense=1,
                         **kwargs)

    # TODO: add this card's text


class SoulJuggler(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Soul Juggler",
                         rank=3,
                         base_attack=3,
                         base_defense=3,
                         **kwargs)

    def on_other_death(self, other_minion):
        if MinionType.Demon in other_minion.types:
            # TODO
            pass


class TheBeast(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="The Beast",
                         rank=3,
                         base_attack=9,
                         base_defense=7,
                         types=[MinionType.Beast],
                         base_deathrattle=TheBeastDeathrattle(),
                         **kwargs)


class TwilightEmissary(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Twilight Emissary",
                         rank=3,
                         base_attack=4,
                         base_defense=4,
                         types=[MinionType.Dragon],
                         base_taunt=True,
                         **kwargs)
