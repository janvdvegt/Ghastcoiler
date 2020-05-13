class Minion:
    def __init__(self, 
                 name, 
                 rank,
                 base_attack, 
                 base_defense, 
                 attack=None, 
                 defense=None, 
                 types=None, 
                 base_poisonous=False,
                 poisonous=False,
                 base_divine_shield=False, 
                 divine_shield=False, 
                 base_taunt=False, 
                 taunt=False, 
                 base_cleave=False, 
                 cleave=False, 
                 base_reborn=False,
                 reborn=False,
                 base_windfury=False, 
                 windfury=False,
                 base_deathrattle=None,
                 deathrattles=None, 
                 golden=False,
                 position=None,
                 player_id=None):
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

    def copy(self):
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

    def add_attack(self, amount):
        self.attack += amount
        self.last_attack += amount

    def add_defense(self, amount):
        self.defense += amount
        self.last_defense += amount

    def minion_string(self, name=False):
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
        return self.minion_string(name=True)

    def receive_damage(self, amount, poisonous):
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

    def check_death(self, own_board, opposing_board):
        total_defense = self.total_defense(own_board, opposing_board)
        if total_defense <= 0:
            self.total_attack(own_board, opposing_board)
            return True
        return False

    def update_attack_and_defense(self, own_board, opposing_board):
        self.total_defense(own_board, opposing_board)
        self.total_attack(own_board, opposing_board)

    def at_beginning_game(self, game_instance, player_starts, own_board, opposing_board):
        pass

    def on_attack(self):
        pass

    def total_attack(self, own_board, opposing_board):
        additional_attack = self.additional_attack(own_board=own_board, opposing_board=opposing_board)
        total_bonus_attack = 0
        for other_minion in own_board.minions:
            if self.position != other_minion.position:
                bonus_attack, _ = other_minion.gives_attack_defense_bonus(self)
                total_bonus_attack += bonus_attack
        total_attack = self.attack + additional_attack + total_bonus_attack
        self.last_attack = total_attack
        return total_attack

    def total_defense(self, own_board, opposing_board):
        total_bonus_defense = 0        
        for other_minion in own_board.minions:
            if self.position != other_minion.position:
                _, bonus_defense = other_minion.gives_attack_defense_bonus(self)
                total_bonus_defense += bonus_defense
        total_defense = self.defense + total_bonus_defense
        self.last_defense = total_defense
        return total_defense

    def total_attack_and_defense(self, own_board, opposing_board):
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

    def additional_attack(self, own_board, opposing_board):
        return 0

    def gives_attack_defense_bonus(self, other_minion):
        return 0, 0

    def on_kill(self):
        pass

    def on_receive_damage(self):
        pass

    def on_other_enter(self, other_minion):
        pass

    def on_other_death(self, other_minion):
        pass

    def on_any_minion_loses_divine_shield(self):
        pass

    def shift_left(self):
        self.position -= 1

    def shift_right(self):
        self.position += 1
