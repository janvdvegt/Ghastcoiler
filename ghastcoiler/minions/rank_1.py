import logging

from minions.base import Minion
from minions.types import MinionType

from deathrattles.rank_1 import FiendishServantDeathrattle, MecharooDeathrattle


class Alleycat(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Alleycat",
                         rank=1,
                         base_attack=1,
                         base_defense=1,
                         types=[MinionType.Beast],
                         **kwargs)


class RabidSaurolisk(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Rabid Saurolisk",
                         rank=1,
                         base_attack=3,
                         base_defense=1,
                         types=[MinionType.Beast],
                         **kwargs)

    def on_other_enter(self, other_minion):
        if other_minion.deathrattles:
            increase_amount = 2 if self.golden else 1
            self.add_attack(increase_amount)
            self.add_defense(increase_amount)


class DragonspawnLieutenant(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Dragonspawn Lieutenant",
                         rank=1,
                         base_attack=2,
                         base_defense=3,
                         types=[MinionType.Dragon],
                         base_taunt=True,
                         **kwargs)


class FiendishServant(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Fiendish Servant",
                         rank=1,
                         base_attack=2,
                         base_defense=1,
                         types=[MinionType.Demon],
                         base_deathrattle=FiendishServantDeathrattle())

        
class Mecharoo(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Mecharoo",
                         rank=1,
                         base_attack=1,
                         base_defense=1,
                         types=[MinionType.Mech],
                         base_deathrattle=MecharooDeathrattle())


class MicroMachine(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Micro Machine",
                         rank=1,
                         base_attack=1,
                         base_defense=1,
                         types=[MinionType.Mech])


class MurlocTidecaller(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Murloc Tidecaller",
                         rank=1,
                         base_attack=1,
                         base_defense=2,
                         types=[MinionType.Murloc])


class MurlocTidehunter(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Murloc Tidehunter",
                         rank=1,
                         base_attack=2,
                         base_defense=1,
                         types=[MinionType.Murloc])


class RedWhelp(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Red Whelp",
                         rank=1,
                         base_attack=1,
                         base_defense=2,
                         types=[MinionType.Dragon])

    def at_beginning_game(self, game_instance, player_starts, own_board, opposing_board):
        number_dragons = own_board.count_minion_type(MinionType.Dragon)
        for _ in range(1 + self.golden):
            minion = opposing_board.random_minion()
            game_instance.deal_damage(minion, opposing_board, number_dragons, False)
            logging.debug(f"{self.minion_string()} deals {number_dragons} damage to {minion.minion_string()}")
        if player_starts:
            game_instance.check_deaths(own_board, opposing_board)
        else:
            game_instance.check_deaths(opposing_board, own_board)


class RighteousProtector(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Righteous Protector",
                         rank=1,
                         base_attack=1,
                         base_defense=1,
                         base_taunt=True,
                         base_divine_shield=True)


class SelflessHero(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Selfless Hero",
                         rank=1,
                         base_attack=2,
                         base_defense=1,
                         base_deathrattle=None) # TODO


class VulgarHomunculus(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Vulgar Homunculus",
                         rank=1,
                         base_attack=2,
                         base_defense=4,
                         types=[MinionType.Demon],
                         base_taunt=True)


class WrathWeaver(Minion):
    def __init__(self, **kwargs):
        super().__init__(name="Wrath Weaver",
                         rank=1,
                         base_attack=1,
                         base_defense=1)
