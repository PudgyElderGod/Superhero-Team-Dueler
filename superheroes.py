import random

class Ability:
    def __init__(self, name, attack_strength):
      '''Create Instance Variables:
          name:String
          max_damage: Integer
       '''
       self.name = name
       self.attack_strength = attack_strength


      def attack(self):
        ''' Return Damage Values '''
        return random.randint(0, self.attack_strength)

class Weapon(Ability):
    '''Type of Ability'''

    def attack(self):
        return random.randint(self.attack_strength//2, self.attack_strength)

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
