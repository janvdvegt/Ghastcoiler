from __future__ import annotations

from typing import Optional, List

from deathrattles.base import Deathrattle
from minions.types import MinionType

class Minion:
    def __init__(self, 
                 name: str, 
                 rank: int,
                 base_attack: int, 
                 base_defense: int, 
                 attack: Optional[int] = None, 
                 defense: Optional[int] = None, 
                 types: Optional[List[MinionType]] = None, 
                 base_poisonous: bool = False,
                 poisonous: bool = False,
                 base_divine_shield: bool = False, 
                 divine_shield: bool = False, 
                 base_taunt: bool = False, 
                 taunt: bool = False, 
                 base_cleave: bool = False, 
                 cleave: bool = False, 
                 base_reborn: bool = False,
                 reborn: bool = False,
                 base_windfury: bool = False, 
                 windfury: bool = False,
                 base_deathrattle: Optional[Deathrattle] = None,
                 deathrattles: Optional[List[Deathrattle]] = None, 
                 golden: bool = False,
                 position: Optional[int] = None,
                 player_id: Optional[int] = None):
        """Base minion class of which all normal minions and tokens should inherit from, and they can override certain triggers to implement custom behaviour.
        Important to note is that all the "base_*" arguments should be used in implementing the normal minions and that the non-base versions should be used
        for specific instances of the normal minions, so for the simulations itself in which case they can be different than their base type.

        Arguments:
            name {str} -- Name of the minion
            rank {int} -- Rank of the minion
            base_attack {int} -- Base attack of the non-golden version
            base_defense {int} -- Base defense of the non-golden version

        Keyword Arguments:
            attack {Optional[int]} -- Optional overwritten attack (default: {None})
            defense {Optional[int]} -- Optional overwritten defense (default: {None})
            types {Optional[List[MinionType]]} -- Optional list of MinionTypes (default: {None})
            base_poisonous {bool} -- Standard poisonous (default: {False})
            poisonous {bool} -- Poisonous (default: {False})
            base_divine_shield {bool} -- Standard divine shield (default: {False})
            divine_shield {bool} -- Divine shield (default: {False})
            base_taunt {bool} -- Standard taunt (default: {False})
            taunt {bool} -- Taunt (default: {False})
            base_cleave {bool} -- Standard cleave (default: {False})
            cleave {bool} -- Cleave (default: {False})
            base_reborn {bool} -- Standard reborn (default: {False})
            reborn {bool} -- Reborn (default: {False})
            base_windfury {bool} -- Standard windfury (default: {False})
            windfury {bool} -- Windfury (default: {False})
            base_deathrattle {Optional[Deathrattle]} -- Standard deathrattle (default: {None})
            deathrattles {Optional[List[Deathrattle]]} -- Additional deathrattles (default: {None})
            golden {bool} -- Golden version (default: {False})
            position {Optional[int]} -- Position on the player board (default: {None})
            player_id {Optional[int]} -- ID of player minion belongs to (default: {None})
        """
        self.name = name
        self.rank = rank
        self.base_attack = base_attack * 2 if golden else base_attack
        self.base_defense = base_defense * 2 if golden else base_defense
        self.attack = attack if attack else base_attack
        self.defense = defense if defense else base_defense
        self.last_attack = self.attack
        self.last_defense = self.defense
        self.types = types if types else []
        self.base_divine_shield = base_divine_shield
        self.divine_shield = divine_shield if divine_shield else base_divine_shield
        self.base_taunt = base_taunt
        self.taunt = taunt if taunt else base_taunt
        self.base_cleave = base_cleave
        self.cleave = cleave if cleave else base_cleave
        self.base_reborn = base_reborn
        self.reborn = reborn if reborn else base_reborn
        self.base_windfury = base_windfury
        self.windfury = windfury if windfury else base_windfury
        self.base_poisonous = base_poisonous
        self.poisonous = poisonous if poisonous else base_poisonous
        self.base_deathrattles = [base_deathrattle] if base_deathrattle else []
        self.deathrattles = self.base_deathrattles + deathrattles if deathrattles else self.base_deathrattles
        self.golden = golden
        self.position = position
        self.player_id = player_id

    def copy(self) -> "Minion":
        """Semi-deep copy of minion - should only be used for copying initial state of player boards

        Returns:
            Minion -- Copy of the minion
        """
        return Minion(name=self.name, 
                      rank=self.rank,
                      base_attack=self.base_attack,
                      base_defense=self.base_defense, 
                      attack=self.attack, 
                      defense=self.defense, 
                      types=self.types, 
                      divine_shield=self.divine_shield, 
                      taunt=self.taunt, 
                      cleave=self.cleave,
                      reborn=self.reborn,
                      windfury=self.windfury,
                      poisonous=self.poisonous,
                      deathrattles=self.deathrattles,
                      golden=self.golden)

    def add_attack(self, amount: int):
        """Add attack to minion, should be used for deathrattles and triggers, not for dynamic bonusses by other minions

        Arguments:
            amount {int} -- Amount of attack to increase
        """
        self.attack += amount
        self.last_attack += amount

    def add_defense(self, amount: int):
        """Add defense to minion, should be used for deathrattles and triggers, not for dynamic bonusses by other minions

        Arguments:
            amount {int} -- Amount of defense to increase
        """
        self.defense += amount
        self.last_defense += amount

    def minion_string(self):
        """String representation of minion

        Returns:
            str -- String representation
        """
        attributes = []
        if self.taunt:
            attributes += "[Ta]"
        if self.windfury:
            attributes += "[Wf]"
        if self.poisonous:
            attributes += "[Po]"
        if self.divine_shield:
            attributes += "[Di]"
        if self.cleave:
            attributes += "[Cl]"
        if self.reborn:
            attributes += "[Re]"
        return_string = f"{self.last_attack}/{self.last_defense} {''.join(attributes)} ({self.name})"
        positional_part = f"<P{self.player_id} {self.position}> "
        return_string = positional_part + return_string
        return return_string

    def __str__(self):
        """String representation of minion

        Returns:
            str -- String representation
        """
        return self.minion_string()

    def receive_damage(self, amount: int, poisonous: bool):
        """Receive amount of damage which can be poisonous

        Arguments:
            amount {int} -- Amount of damage to receive
            poisonous {bool} -- Whether the damage is poisonous

        Returns:
            bool -- Whether the minion has popped a shield
        """
        popped_shield = False
        if self.divine_shield:
            if amount > 0:
                popped_shield = True
                self.divine_shield = False
        else:
            if poisonous:
                self.defense = -9999999
            else:
                self.defense -= amount
        return popped_shield

    def check_death(self, own_board: PlayerBoard, opposing_board: PlayerBoard) -> bool:
        """Check whether the minion is dead

        Arguments:
            own_board {PlayerBoard} -- Board minion belongs to
            opposing_board {PlayerBoard} -- Board minion does not belong to

        Returns:
            bool -- Whether minion is dead
        """
        total_defense = self.total_defense(own_board, opposing_board)
        if total_defense <= 0:
            self.total_attack(own_board, opposing_board)
            return True
        return False

    def update_attack_and_defense(self, own_board, opposing_board):
        """Update attack and defense 

        Arguments:
            own_board {[type]} -- [description]
            opposing_board {[type]} -- [description]
        """
        self.total_defense(own_board, opposing_board)
        self.total_attack(own_board, opposing_board)

    def at_beginning_game(self, game_instance: GameInstance, player_starts: bool, own_board: PlayerBoard, opposing_board: PlayerBoard):
        """Trigger that can be implemented to do things at the beginning of the game

        Arguments:
            game_instance {GameInstance} -- The instance of the game we are working in
            player_starts {bool} -- Whether this minion belongs to the starting player
            own_board {PlayerBoard} -- Player board belonging to minion
            opposing_board {PlayerBoard} -- Player board not belonging to minion
        """
        pass

    def on_attack(self):
        """Trigger that can be implemented when the minion attacks
        """
        pass

    def total_attack(self, own_board: PlayerBoard, opposing_board: PlayerBoard):
        """Calculate total attack of minion - WILL BE PART OF REFACTORING OF BONUS SYSTEM

        Arguments:
            own_board {PlayerBoard} -- Player board minion belongs to
            opposing_board {PlayerBoard} -- Player board minion does not belong to

        Returns:
            int -- Total attack of minion
        """
        additional_attack = self.additional_attack(own_board=own_board, opposing_board=opposing_board)
        total_bonus_attack = 0
        for other_minion in own_board.minions:
            if self.position != other_minion.position:
                bonus_attack, _ = other_minion.gives_attack_defense_bonus(self)
                total_bonus_attack += bonus_attack
        total_attack = self.attack + additional_attack + total_bonus_attack
        self.last_attack = total_attack
        return total_attack

    def total_defense(self, own_board: PlayerBoard, opposing_board: PlayerBoard):
        """Calculate total defense of minion - WILL BE PART OF REFACTORING OF BONUS SYSTEM

        Arguments:
            own_board {PlayerBoard} -- Player board minion belongs to
            opposing_board {PlayerBoard} -- Player board minion does not belong to

        Returns:
            int -- Total defense of minion
        """
        total_bonus_defense = 0        
        for other_minion in own_board.minions:
            if self.position != other_minion.position:
                _, bonus_defense = other_minion.gives_attack_defense_bonus(self)
                total_bonus_defense += bonus_defense
        total_defense = self.defense + total_bonus_defense
        self.last_defense = total_defense
        return total_defense

    def total_attack_and_defense(self, own_board: PlayerBoard, opposing_board: PlayerBoard):
        """Calculate total attack and defense of minion - WILL BE PART OF REFACTORING OF BONUS SYSTEM

        Arguments:
            own_board {PlayerBoard} -- Player board minion belongs to
            opposing_board {PlayerBoard} -- Player board minion does not belong to

        Returns:
            Tuple[int, int] -- Total attack and defense of minion
        """
        
        additional_attack = self.additional_attack(own_board=own_board, opposing_board=opposing_board)
        total_bonus_attack, total_bonus_defense = 0, 0
        for other_minion in own_board.minions:
            if self.position != other_minion.position:
                bonus_attack, bonus_defense = other_minion.gives_attack_defense_bonus(self)
                total_bonus_attack += bonus_attack
                total_bonus_defense += bonus_defense
        total_attack = self.attack + additional_attack + total_bonus_attack
        total_defense = self.defense + total_bonus_defense
        self.last_attack = total_attack
        self.last_defense = total_defense
        return total_attack, total_defense

    def additional_attack(self, own_board: PlayerBoard, opposing_board: PlayerBoard) -> int:
        """Additional attack due to personal bonuses

        Arguments:
            own_board {PlayerBoard} -- Player board minion belongs to
            opposing_board {PlayerBoard} -- Player board minion does not belong to

        Returns:
            int -- Additional attack due to personal bonsus
        """
        return 0

    def gives_attack_defense_bonus(self, other_minion: Minion):
        """How much additional attack and defense this minion grants the other minion

        Arguments:
            other_minion {Minion} -- Minion to potentially grant bonus attack and defense

        Returns:
            Tuple[int, int] -- Attack and defense bonus granted
        """
        return 0, 0

    def on_kill(self):
        """Trigger that happens when this minion kills another minion"""
        pass

    def on_receive_damage(self):
        """Trigger that happens when this minion receives damage"""
        pass

    def on_other_enter(self, other_minion: Minion):
        """Trigger that happens when another minion enters the player board

        Arguments:
            other_minion {Minion} -- Minion entering the player board
        """
        pass

    def on_other_death(self, other_minion: Minion):
        """Trigger that happens when another minion on the player board dies

        Arguments:
            other_minion {Minion} -- Other minion that dies
        """
        pass

    def on_any_minion_loses_divine_shield(self):
        """Trigger that happens when a minion loses divine shield"""
        pass

    def shift_left(self):
        """Shift position of minion left because a space cleared up"""
        self.position -= 1

    def shift_right(self):
        """Shift position of minion right because a minion was added to the left"""
        self.position += 1
