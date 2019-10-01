import random

#Default Ability
class Ability:
    '''Default Ability'''

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):

        rand_hit = random.randint(0, self.attack_strength)
        return rand_hit

#Weapon Ability
class Weapon(Ability):
    '''Type of Ability'''

    def attack(self):
        return random.randint(self.attack_strength//2, self.attack_strength)
        return rand_attack

#Armor Class
class Armor:
    '''Block class'''
    def __init__(self,name,max_guard):
        self.name = name
        self.max_guard = max_guard

    def guard(self):
        return random.randint(0, self.max_guard)


#Heroes
class Hero:
    '''All bois begin here'''
    def __init__(self, name, start_hp=100):
        self.name = name
        self.start_hp = start_hp
        self.current_hp = start_hp
        self.abilities = []
        self.armors = []
        self.losses = 0
        self.wins = 0

    def is_conscious(self):
        '''Makes sure the boi is conscious'''
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

    def attack(self):
        '''Calculates the total damage.'''
        damage = 0
        for ability in self.abilities:
            attack = ability.attack()
            damage += attack

    def defend(self):
        '''Blocks damage'''
        block = 0
        for armor in self.armors:
            block += armor.block()
        return block

    def take_damage(self, damage):
        '''Updates health to show the amount of damage minus block'''
        self.current_hp -= (damage - self.defend())

    def fight(self, foe):
        '''The battle between the forces of code and coder.'''
        print('!!! The battle begins between ' + self.name + 'and ' + foe.name + ' !!!')
        combatant = random.randint(0, 1)
        while self.is_alive() and foe.is_alive():
            if combatant == 0:
                damage = self.attack()
                foe.take_damage(damage)
                combatant = 1
            else:
                damage = foe.attack()
                self.take_damage(damage)
                combatant = 0

        if (self.is_conscious()):
            self.add_wins()
            foe.add_losses()
            print('!!! ' + self.name + ' is victorious!!!')
        elif (foe.is_conscious()):
            self.add_losses()
            foe.add_wins()
            print('!!! ' + self.name + ' has been defeated!!!')

    def add_losses(self, loss_count=1):
        '''Updates losses'''
        self.losses += loss_count

    def add_win(self, win_count=1):
        '''Updates wins'''
        self.wins += win_count

    def get_record(self):
        '''Returns wins and losses'''
        WLR = 0
        total_wins = 0
        total_losses = 0
        for hero in self.heroes:
            total_wins += hero.wins
            total_losses += hero.losses
        if total_losses == 0:
            WLR = total_wins
        else:
            WLR = total_wins/total_losses
        return WLR

#Class Team
class Team:
    '''List of champions'''

    def __init__(self, name):
        '''Properties ahoy'''
        self.name = name
        self.heroes = []

    def add_help(self, hero):
        '''Adds a boi'''
        self.heroes.append(hero)

    def remove_hero(self, hero):
        '''Subtracts a boi'''
        if hero in self.heroes:
            self.heroes.remove(hero)
        else:
            return 0
