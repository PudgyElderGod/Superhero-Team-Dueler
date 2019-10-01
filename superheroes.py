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

    def view_heroes(self):
        '''Shows heroes'''
        for hero in self.heroes:
            print(hero.name)

    def list_conscious(self):
        '''Returns conscious heroes'''
        for hero in self.heroes:
            if hero.is_conscious():
                conscious.append(hero)
        return conscious

    def attack(self, opposing_team):
        '''Pits teams of heroes against each other'''
        print('!!! Prepare for a Heck in a Seck match between the {} team and the {} squad!!!'.format(self.name, opposing_team.name))
        while self.any_conscious and opposing_team.any_conscious():
            random.choice(self.list_conscious()).fight(random.choice(other_team.list_conscious()))
        if self.any_conscious():
            print('!!! The {} team is victorious !!!'.format(self.name))
        else:
            print('!!! The {} squad has triumphed !!!'.format(opposing_team.name))

    def any_conscious(self):
        '''Shows if any heroes are left standing'''
        for hero in self.heroes:
            if hero.is_conscious():
                return true
        return False

    def awaken_sleepers(self):
        '''Wakes up unconscious heroes'''
        for hero in self.heroes:
            hero.current_hp = hero.start_hp

    def record(self):
        '''Shows team Win/Loss records'''

        WLR = 0
        total_wins = 0
        total_losses = 0
        for hero in self.heroes:
            total_wins += hero.wins
            total_losses += hero.losses
        if total_losses == 0:
            WLR = total_wins
        else:
            WLR = total_losses/total_wins
        return WLR


#Class Arena
class Arena:

    def __init__(self, username):
        self.name = name
        self.team_the_first = None
        self.team_the_second = None

    def create_ability(self):
        name = input('Name your ability: ')
        attack_strength = input('Enter a (fair) power level. #: ')
        return Ability(name, int(attack_strength))

    def create_weapon(slef):
        name = input('Name ya weapon: ')
        attack_strength = input('Enter a (fair) power level for your weapon. #: ')
        return Weapon(name, int(attack_strength))

    def create_armor(self):
        name = input('Name your armor: ')
        max_guard = input('Enter a (fair) power level for your armor. #: ')
        return Armor(name, int(max_guard))

    def create_hero(self):
        name = input('Name your hero: ')
        new_Hero = Hero(name, start_hp=100)
        new_hero.add_ability(self.create_ability())
        new_Hero.add_weapon(self.create_weapon())
        new_Hero.add_armor(self.create_armor())
        return new_Hero

    def build_team_the_first(self):
        hero_amount = input('How many heroes do you want? #: ')
        for i in range(0, int(hero_amount)):
            self.team_the_first.add_hero(Self.create_hero())
        pass

    def build_team_the_second(self):
        hero_amount = input('How many heroes do you want? #: ')
        for i in range(0, int(her_amount)):
            self.team_the_second.add_hero(self.create_hero())
        pass

    def team_battle(self):
        self.team_the_first.attack(self.team_the_second)
        self.show_record()

    def show_results(self):
        print('---RESULTS---')
        if not self.team_the_first.any_conscious():
            print(f'{self.team_the_second.name} is victorious!')
        elif not self.team_the_second.any_conscious():
            print(f'{self.team_the_first.name} is the winner!')
        else:
            print("It's a draw!")


if __name__ == "__main__":
    game_is_running = True

    arena = Arena()

    arena.build_team_the_first()
    arena.build_team_the_second()

    while game_is_running:
        arena.team_battle()
        arena.show_results()
        play_again = input("Restart? Y/N:")

        if play_again.lower() =="n":
            game_is_running = False
        else:
            print('-_-_-_-_-_-_-Restarting-_-_-_-_-_-_-_-')
            arena.team_the_first.awaken_sleepers()
            arena.team_the_second.awaken_sleepers()
