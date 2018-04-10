import random
import time
import cmd
import textwrap
import os
import sys

#BATTLE TEST#

weapon = {'laser gun'}

class Fireman:
    def __init__(self):
        self.maxhealth = '70'
        self.health = self.maxhealth
        self.attack = '20'
        self.name = ''
        self.inventory = []
        self.location = 'c1'
        self.equipweap = []

    @property
    def weap_attack(self):
        attack = int(self.attack)
        if self.equipweap == 'laser gun':
            attack += 15
        return attack

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)
 


class Chef:
    def __init__(self):
        self.maxhealth = '80'
        self.health = self.maxhealth
        self.base_attack = '10'
        self.name = ''
        self.inventory = []
        self.location = 'c1'
        self.equipweap = []

    @property
    def attack(self):
        if self.equipweap == 'laser gun':
            attack = int(self.base_attack) + 15
        return attack

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)
player = Chef()


class Martial_Artist:
    def __init__(self):
        self.maxhealth = '60'
        self.health = self.maxhealth
        self.base_attack = '30'
        self.name = ''
        self.inventory = []
        self.location = 'c1'
        self.equipweap = []

    @property
    def attack(self):
        attack = self.base_attack
        if self.equipweap == 'laser gun':
            attack += 15
        return attack

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)
player = Martial_Artist()


class Gambler:
    def __init__(self):
        self.maxhealth = '40'
        self.health = self.maxhealth
        self.base_attack = '40'
        self.name = ''
        self.inventory = []
        self.location = 'c1'
        self.equipweap = []

    @property
    def attack(self):
        attack = self.base_attack
        if self.equipweap == 'laser gun':
            attack += 15
        return attack

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)
player = Gambler()

class Alien:
    def __init__(self):
        self.health = '75'
        self.attack = '15'
enemy = Alien()

#class laser_gun
    #def __init__(self):
        #self.attack = '15'

#class health_flask
    #def __init__(self):
        #self.health = '30'
        
     
# Intro

def choose_occupation():
    print("\n\n")
    print("What is your job?")
    print("1) Fireman")
    print("2) Chef")
    print("3) Martial Artist")
    print("4) Gambler")
    occupation = input("Type in the number of your job: ")
    if occupation == '1':
        return 'fireman'
    if occupation == '2':
        return 'chef'
    if occupation == '3':
        return 'martial_artist'
    if occupation == '4':
        return 'gambler'

 
loop = 1
while loop == 1:
    userChoice = choose_occupation()
    if userChoice == 'fireman':
        player = Fireman()
        player.name_player()
        player.print_stats()
        loop = 0
        print('These are your stats', player.name)
    elif userChoice == 'chef':
        player = Chef()
        player.name_player()
        player.print_stats()
        loop = 0
        print('These are your stats', player.name)
    elif userChoice == 'martial_artist':
        player = Martial_Artist()
        player.name_player()
        player.print_stats()
        loop = 0
        print('These are your stats', player.name)
    elif userChoice == 'gambler':
        player = Gambler()
        player.name_player()
        player.print_stats()
        loop = 0
        print('These are your stats', player.name)
    else:
        print('That ain\'t one of the classes.')

def choose_item():
    print('You can choose between')
    print('1.)laser gun')
    print('2.)health potion')
    item_option = input('number of choice: ')
    if item_option == '1':
        player.inventory.append('laser gun')
        print('You now have a',player.inventory)
        #prompt()
    elif item_option == '2':
        player.inventory.append('health potion')
        print('You now have a',player.inventory)
        #prompt()
    else:
        print('those aren\'t one of the options')
        choose_item()

choose_item()

def equip():
    print ("What do you want to equip?")
    for weapon in player.inventory:
        print (weapon)
    print ('b to go back')
    equip_option = input('Choice: ')
    if equip_option == 'b':
        inventory()
    elif equip_option in player.inventory:
        player.equipweap = equip_option
        print('You have now equipped', equip_option)
        player.weap_attack()
    else:
        equip()
        
def inventory():
    print ('What do you want to do')
    print ('1.) Equip weapon')
    print ('2.) Drink potion')
    print ('2.) Go back')
    inventory_option = input('number of choice: ')
    if inventory_option == '1':
        equip()
    elif inventory_option == '2':
        heal()

#inventory()


def battle():
    print('The alien is in front of you')
    print('You are engaging in battle against the alien')
    print('1.) Attack')
    print('2.) Run')
    print('3.) Heal')
    option = input('number of choice: ')
    if option == '1':
        damage_enemy(player, enemy)
    elif option == '2':
        run_prompt()
    elif option == '3':
        battle_heal()
    else:
        battle()

def run_prompt():
    print('\n')
    print("You are in room", player.location)
    print("You are about to escape, what would you like to do?")
    print("1) Move room")
    print("2) Get back into battle? ")
    action = input("Number of choice: ")
    acceptable_actions = ('1', '2')
    while action not in acceptable_actions:
        print("Action, unknown. Please try again."),
        action = input("Number of choice: ")
    if action == '1':
        hp = int(player.health) - 30
        health = str(hp)
        print('While escaping, you were damage and have ' + health + ' remaining health.')
        if int(health) < 0:
                game_over()
        else:
            player.health = health
            player_move()
    elif action == '2':
        battle()

        
def damage_enemy(attacker, defender):
    damage = int(attacker.attack)
    defender.health = int(defender.health) - damage
    if defender.health <=0:
        print('\n')
        print('Alien has been defeated')
        prompt()
    else:
        print('Alien is on', defender.health,'health.')
        damage_player(enemy, player)

        
def damage_player(attacker,defender):
    print('\n')
    print('The alien has retaliated')
    damage = int(attacker.attack)
    defender.health = int(defender.health) - damage
    if defender.health <=0:
        game_over()
    else:
        print('You are on', defender.health,'health.')
        return defender.health
        battle()



def battle_heal():
    if 'health potion' in player.inventory:
        player.health = int(player.health) + 30
        print('You are on ', player.health, 'health.')
    else:
        ('You don\'t have a health potion')
        battle()

def heal():
    if 'health potion' in player.inventory:
        player.health = int(player.health) + 30
        print('You are on ', player.health, 'health.')
    else:
        ('You don\'t have a health potion')
        prompt()
        
        
    

battle()
