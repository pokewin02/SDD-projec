import random
import time
import cmd
import textwrap
import os
import sys
## Player Creation##

#class Occupation(object):
    # job for all characters
#    health = 0
#    attack = 0
#    name = ""
#
#   def __init__(self, health, attack, occupation, name):
#        self.health = health
#        self.attack = attack
#        self.name = name
#        print ("self = ", self)


class Fireman:
    health = '70'
    attack = '20'
    name = ''
    inventory = []
    location = 'a1'

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)
player = Fireman()    


class Chef:
    health = '80'
    attack = '10'
    name = ''
    inventory = []
    location = 'a1'

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)
player = Chef()


class Martial_Artist:
    health = '60'
    attack = '30'
    name = ''
    inventory = []
    location = 'a1'

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)
player = Martial_Artist()


class Gambler:
    health = '40'
    attack = '40'
    name = ''
    inventory = []
    location = 'a1'

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)
player = Gambler()

class Alien:
    health = '15'
    attack = '40'

        
# Intro
def gameStart():
    #time.sleep(2)
    print("Hello there")
    #time.sleep(2)
    print("Welcome to....")
    #time.sleep(2)
    print("  ___   _  _                _____                                 ")
    print(" / _ \ | |(_)              |  ___|                                ")
    print("/ /_\ \| | _   ___  _ __   | |__   ___   ___   __ _  _ __    ___  ")
    print("|  _  || || | / _ \| '_ \  |  __| / __| / __| / _` || '_ \  / _ \ ")
    print("| | | || || ||  __/| | | | | |___ \__ \| (__ | (_| || |_) ||  __/ ")
    print("\_| |_/|_||_| \___||_| |_| \____/ |___/ \___| \__,_|| .__/  \___| ")
    print("                                                    | |           ")
    print("                                                    |_|           ")
    #time.sleep(2)
    print(".....")
    print("You've been abducted by aliens for experimentation...")
    print("You wake up in the docking bay and you see a panel next to you")
    print("It displays")
    print(" ___________ ")
    print("|           |")
    print("|Job: ?     |")
    print("|           |")
    print("|Attack: ?  |")
    print("|           |")
    print("|Health: ?  |")
    print("|           |")
    print("|___________|")


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


gameStart()   
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

# Game Map
def game_map():

#map

    """    
    a1 a2...    
    -------------
    |  |  |  |  | a4
    -------------
    |  |  |  |  | b4 ...
    -------------
    |  |  |  |  |
    -------------
    |  |  |  |  |
    -------------
    """

    ZONENAME = ''
    EXAMINATION = 'examine'
    DISCOVERED = False
    UP = 'up', 'north'
    DOWN = 'down', 'south'
    LEFT = 'left', 'west'
    RIGHT = 'right', 'east'

    discovered_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                     'b1': False, 'b2': False, 'b3': False, 'b4': False,
                     'c1': False, 'c2': False, 'c3': False, 'c4': False,
                     'd1': False, 'd2': False, 'd3': False, 'd4': False,
                     }

    zonemap = {
        'a1': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: '',
            DOWN: 'b1',
            LEFT: '',
            RIGHT: 'a2',
        },
        'a2': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: '',
            DOWN: 'b2',
            LEFT: 'a1',
            RIGHT: 'a3',
        },
        'a3': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: '',
            DOWN: 'b3',
            LEFT: 'a2',
            RIGHT: 'a4',
        },
        'a4': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: '',
            DOWN: 'b4',
            LEFT: 'a3',
            RIGHT: '',
        },
        'b1': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: 'a1',
            DOWN: 'c1',
            LEFT: '',
            RIGHT: 'b2',
        },
        'b2': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: 'a2',
            DOWN: 'c2',
            LEFT: 'b1',
            RIGHT: 'b3',
        },
        'b3': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False, 
            UP: 'a3',
            DOWN: 'c3',
            LEFT: 'b2',
            RIGHT: 'b4',
        },
        'b4': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: 'a4' ,
            DOWN: 'c4',
            LEFT: 'b3',
            RIGHT: '',
        },
        'c1': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: 'b1',
            DOWN: 'd1',
            LEFT: '',
            RIGHT: 'c2',
        },
        'c2': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: 'b2',
            DOWN: 'd2',
            LEFT: 'c1',
            RIGHT: 'c3',
        },
        'c3': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: 'b3',
            DOWN: 'd3',
            LEFT: 'c2',
            RIGHT: 'c4',
        },
        'c4': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: 'b4',
            DOWN: 'd4',
            LEFT: 'c3',
            RIGHT: '',
        },
        'd1': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: 'c1',
            DOWN: '',
            LEFT: '',
            RIGHT: 'd2',
        },
        'd2': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: 'c2',
            DOWN: '',
            LEFT: 'd1',
            RIGHT: 'd3',
        },
        'd3': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: 'c3',
            DOWN: '',
            LEFT: 'd2',
            RIGHT: 'd4',
        },
        'd4': {
            ZONENAME: "",
            EXAMINATION: '',
            DISCOVERED: False,
            UP: 'c4',
            DOWN: '',
            LEFT: 'd3',
            RIGHT: '',
        },
}
game_map()

#MOVING AND STUFF
def print_location():
    print('\n')
    print("You are in room", player.location)

def prompt():
    print('\n')
    print("Would you like to do?")
    print("1) Move room")
    print("2) Examine rooms")
    action = input("Number of choice: ")
    acceptable_actions = ('1', '2')
    while action not in acceptable_actions:
        print("Action, unknown. Please try again."),
        action = input("Number of choice: ")
    if action == '1':
        player_move()
    elif action == '2':
        player_examine()

def player_move():
    destination = input("Where do you want to go? ")
    if destination == ['up', 'north']:
        location = zonemap[player.location][UP]
        movement_handler()
    elif destination == ['down', 'south']:
        location = zonemap[player.location][DOWN]
        movement_handler()
    elif destination == ['left', 'west']:
        location = zonemap[player.location][LEFT]
        movement_handler()
    elif destination == ['right', 'east']:
        location = zonemap[player.location][RIGHT]
        movement_handler()

def movement_handler():
        location = player.location
        print('\n' + 'You have moved to ' + location + '.')

    
        
print_location()
prompt()

            


                 


