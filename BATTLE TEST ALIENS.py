import random
import time
import cmd
import textwrap
import os
import sys

#BATTLE TEST#

class Fireman:
    def __init__(self):
        self.health = '70'
        self.attack = '20'
        self.name = ''
        self.inventory = []
        self.location = 'c1'

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)
player = Fireman()    


class Chef:
    def __init__(self):
        self.health = '80'
        self.attack = '10'
        self.name = ''
        self.inventory = []
        self.location = 'c1'

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
        self.health = '60'
        self.attack = '30'
        self.name = ''
        self.inventory = []
        self.location = 'c1'

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
        self.health = '40'
        self.attack = '40'
        self.name = ''
        self.inventory = []
        self.location = 'c1'

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
        print('That aint one of the classes.')


def battle():
    print('You are engaging in battle against an alien')
    print('1.) Attack')
    print('2.) Heal')
    print('3.) Run')
    option = input('number of choice: ')
    if option == '1':
        damage_enemy()
    if option == '2':
        heal()
    if option == '3':
        prompt()
    else:
        battle()
    
        

def damage_enemy():
    playeratk = int(player.attack)
    playerhp = int(player.health)
    enemyatk = int(enemy.attack)
    enemyhp = int(enemy.health)
    enemyhp = enemyhp - playeratk
    if enemyhp <=0:
        print('Alien has been slain')
    else:
        print('Alien is on', enemyhp,'health.')
        battle()

def heal(player):
    if healing_flask in player.inventory:
        player.health + 30

battle()
