import random
import time
import cmd
import textwrap
import os
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

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)
        

class Chef:
    health = '80'
    attack = '10'
    name = ''
    inventory = []

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)


class Martial_Artist:
    health = '60'
    attack = '30'
    name = ''
    inventory = []

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)


class Gambler:
    health = '40'
    attack = '40'
    name = ''
    inventory = []

    def name_player(self):
        self.name = input('Enter your name? ')

    def add_inventory(self, item):
        self.inventory.append(item)

    def print_stats(self):
        print("Health =", self.health)
        print("Attack =", self.attack)

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

    EXAMINATION = 'examine'
    INSIDE = False
    UP = 'up', 'north'
    DOWN = 'down', 'south'
    LEFT = 'left', 'west'
    Right = 'right', 'east'

    inside_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                     'b1': False, 'b2': False, 'b3': False, 'b4': False,
                     'c1': False, 'c2': False, 'c3': False, 'c4': False,
                     'd1': False, 'd2': False, 'd3': False, 'd4': False,
                     }

    zonemap = {
        'a1': {
            ZONENAME: "",
            EXAMINATION: '',
            INSIDE: False,
            UP: '',
            DOWN: 'b1',
            LEFT: '',
            RIGHT: 'a2',

        'a2': {
            ZONENAME: "",
            EXAMINATION: '',
            INSIDE: False,
            UP: '',
            DOWN: 'b2',
            LEFT: 'a1',
            RIGHT: 'a3',

        'a3': {
            ZONENAME = "",
            EXAMINATION = '',
            INSIDE = False,
            UP = '',
            DOWN = 'b3',
            LEFT = 'a2',
            RIGHT = 'a4',

        'a4': {
            ZONENAME: "",
            EXAMINATION = '',
            INSIDE = False,
            UP = '',
            DOWN = 'b4',
            LEFT = 'a3',
            RIGHT = '',

        'b1': {
            ZONENAME: "",
            EXAMINATION = '',
            INSIDE = False,
            UP = 'a1',
            DOWN = 'c1',
            LEFT = '',
            RIGHT = 'b2',

        'b2': {
            ZONENAME: "",
            EXAMINATION = '',
            INSIDE = False,
            UP = 'a2',
            DOWN = 'c2',
            LEFT = 'b1',
            RIGHT = 'b3',

        'b3': {
            ZONENAME: "",
            EXAMINATION = '',
            INSIDE = False, 
            UP = 'a3',
            DOWN = 'c3',
            LEFT = '
            RIGHT =

        'b4': {
            ZONENAME: "",
            EXAMINATION =
            INSIDE = False
            UP = 
            DOWN = 
            LEFT =
            RIGHT =

        'c1': {
            ZONENAME: "",
            EXAMINATION =
            INSIDE = False
            UP = 
            DOWN = 
            LEFT =
            RIGHT =

        'c2': {
            ZONENAME: "",
            EXAMINATION =
            INSIDE = False
            UP = 
            DOWN = 
            LEFT =
            RIGHT =

        'c3': {
            ZONENAME: "",
            EXAMINATION =
            INSIDE = False
            UP = 
            DOWN = 
            LEFT =
            RIGHT =

        'c4': {
            ZONENAME: "",
            EXAMINATION =
            INSIDE = False
            UP = 
            DOWN = 
            LEFT =
            RIGHT =

        'd1': {
            ZONENAME: "",
            EXAMINATION =
            INSIDE = False
            UP = 
            DOWN = 
            LEFT =
            RIGHT =

        'd2': {
            ZONENAME: "",
            EXAMINATION =
            INSIDE = False
            UP = 
            DOWN = 
            LEFT =
            RIGHT =

        'd3': {
            ZONENAME: "",
            EXAMINATION =
            INSIDE = False
            UP = 
            DOWN = 
            LEFT =
            RIGHT =

        'd4': {
            ZONENAME: "",
            EXAMINATION =
            INSIDE = False
            UP = 
            DOWN = 
            LEFT =
            RIGHT =
            


                 


