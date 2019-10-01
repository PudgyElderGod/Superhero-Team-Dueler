import random

class Ability:
    '''Default Ability'''

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):

        rand_hit = random.randint(0, self.attack_strength)
        return rand_hit

class Weapon(Ability):
    '''Type of Ability'''

    def attack(self):
        return random.randint(self.attack_strength//2, self.attack_strength)
        return rand_attack

class Armor:
    '''Block class'''
    def __init__(self,name,max_guard):
        self.name = name
        self.max_guard = max_guard

    def guard(self):
        return random.randint(0, self.max_guard)


class Hero:
    '''All bois begin here'''
    def __init__(self, name, start_hp=100):
        self.name = name
        self.start_hp = start_hp
        self.current_hp = start_hp
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def is_alive(self):
        '''Makes sure the boi lives'''
        return self.current_hp > 0

    def add_ability(self, ability):
        '''Adds the generic ability. Probably Big Punch.'''
        self.abilities.append(Ability)

    def add_weapon(self, weapon):
        '''Adds the weapon ability'''
        self.abilities.append(weapon)

    def add_armor(self, armor):
        '''Slap some protection on that bad boi.'''
        self.armors.append(armor)

    def defend(self):
        '''Blocks damage'''
        block = 0
        for armor in self.armors:
            block += armor.block()
        return block

    def take_damage(self, damage):
        '''Updates health to show the amount of damage minus block'''
        self.current_hp -= (damage - self.defend())
