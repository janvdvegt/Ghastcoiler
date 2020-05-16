import random
import logging

from typing import List

from minions.base import Minion
from minions.types import MinionType


class PlayerBoard:
    def __init__(self, player_id, hero, life_total, rank, minions: List[Minion]):
        self.player_id = player_id
        self.hero = hero
        self.life_total = life_total
        self.rank = rank
        self.minions: List[Minion] = minions
        self.attack_position = 0
        for index, minion in enumerate(minions):
            minion.position = index
            minion.player_id = player_id

    def copy(self):
        return PlayerBoard(player_id=self.player_id, hero=self.hero, life_total=self.life_total, rank=self.rank, minions=[minion.copy() for minion in self.minions])

    def minions_string(self):
        minion_string = []
        for minion in self.minions:
            minion_string.append(minion.minion_string())
        return "\n".join(minion_string)

    def __str__(self):
        return_string = f"Hero: {self.hero}\nLife: {self.life_total}\nRank: {self.rank}\n"
        for minion in self.minions:
            return_string += str(minion) + "\n"
        return return_string

    def score(self):
        if len(self.minions) == 0:
            return 0
        return sum([minion.rank for minion in self.minions]) + self.rank

    def count_minion_type(self, minion_type):
        return len([minion for minion in self.minions if minion_type in minion.types])

    def select_taunts(self):
        return [minion for minion in self.minions if minion.taunt]

    def divine_shield_popped(self):
        for minion in self.minions:
            minion.on_any_minion_loses_divine_shield()

    def select_attacking_minion(self):
        # TODO: Take care of 0 attack units
        if self.attack_position >= len(self.minions):
            self.attack_position = 0
        minion = self.minions[self.attack_position]
        self.attack_position += 1
        return minion

    def generate_possible_defending_minions(self):
        possible_minions = self.select_taunts()
        if len(possible_minions) == 0:
            possible_minions = self.minions
        return possible_minions

    def select_defending_minion(self, attacks_lowest=False):
        # TODO: Rank 6 windfury guy
        possible_minions = self.generate_possible_defending_minions()
        defending_minion_index = random.randint(0, len(possible_minions) - 1)
        return possible_minions[defending_minion_index]

    def get_minions(self):
        return self.minions

    def random_minion(self):
        if len(self.minions) > 0:
            return self.minions[random.randint(0, len(self.minions) - 1)]

    def remove_minion(self, minion):
        # logging.debug(f"Removing {minion.minion_string()}")
        position = minion.position
        self.minions.pop(position)
        for minion in self.minions[position:]:
            minion.shift_left()

    def add_minion(self, minion, position=None):
        if len(self.minions) < 7:
            if position is None:
                position = len(self.minions)
            minion.position = position
            minion.player_id = self.player_id
            self.minions.insert(position, minion)
            for minion in self.minions[position + 1:]:
                minion.shift_right()
            logging.debug(f"Adding {minion.minion_string()}")
            return minion
        else:
            logging.debug(f"Did not add {minion.minion_string()} because of a lack of space")