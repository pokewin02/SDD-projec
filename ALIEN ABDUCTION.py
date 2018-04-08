import random
import time
import cmd
import textwrap
import os
import sys
## Player Creation##

#class Occupation(object):
#   job for all characters
#   def __init__(self, health, attack, occupation, name):
#        self.health = health
#        self.attack = attack
#        self.name = name
#        print ("self = ", self)


weapon = {'laser gun'}

class Fireman:
    def __init__(self):
        self.maxhealth = '70'
        self.health = self.maxhealth
        self.base_attack = '20'
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
player = Fireman()    


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

       

enemy = Alien()

#class laser_gun
    #def __init__(self):
        #self.attack = '15'

#class health_flask
    #def __init__(self):
        #self.health = '30'
        
     
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
    print("\n")
    print("You need to a key to operate an escape pod.")


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


#map
print('\n')
print('\n')
print(" a1 a2...        ")  
print("----------       ")
print("|  |  |  | a3    ")
print("----------       ")
print("|  |  |  | b3 ...")
print("----------       ")
print("|  |  |  |       ")
print("----------       ")
print('\n')
print('\n')
print('This is the map')


ZONENAME = ''
EXAMINATION = 'examine'
DISCOVERED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

discovered_places = {'a1': False, 'a2': False, 'a3': False, 
                    'b1': False, 'b2': False, 'b3': False,
                    'c1': False, 'c2': False, 'c3': False,
                    }

zonemap = {
    'a1': {
        ZONENAME: 'medical Bay',
        EXAMINATION: 'There\'s nothing here.',
        DISCOVERED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: 'lavatory',
        EXAMINATION: 'There\'s nothing here.',
        DISCOVERED: False,
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: 'emergency exit',
        EXAMINATION: 'There are escape pods here.',
        DISCOVERED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: 'corridor',
        EXAMINATION: 'There\'s nothing here.',
        DISCOVERED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: 'corridor',
        EXAMINATION: 'There\'s nothing here.',
        DISCOVERED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: 'corridor',
        EXAMINATION: 'There\'s nothing here.',
        DISCOVERED: False, 
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: '',
    },
    'c1': {
        ZONENAME: 'lab',
        EXAMINATION: 'You need to get out of here!',
        DISCOVERED: False,
        UP: 'b1',
        DOWN: '',
        LEFT: '',
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: 'armoury',
        EXAMINATION: 'There\'s nothing here.',
        DISCOVERED: False,
        UP: 'b2',
        DOWN: '',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: 'engine room',
        EXAMINATION: 'There\'s nothing here.',
        DISCOVERED: False,
        UP: 'b3',
        DOWN: '',
        LEFT: 'c2',
        RIGHT: '',
    },

}

#placing key
rooms = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
room_with_key = random.choice(rooms)

#MOVING AND STUFF

def prompt():
    print('\n')
    print("You are in room", player.location)
    print("What would you like to do?")
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
    if destination in ['up', 'north']:
        location = zonemap[player.location][UP]
        movement_handler(location)
    elif destination in ['down', 'south']:
        location = zonemap[player.location][DOWN]
        movement_handler(location)
    elif destination in ['left', 'west']:
        location = zonemap[player.location][LEFT]
        movement_handler(location)
    elif destination in ['right', 'east']:
        location = zonemap[player.location][RIGHT]
        movement_handler(location)
    else:
        print('invalid direction'),
        player_move()


def movement_handler(location):
        player.location = location
        if player.location == '':
            print('There is a wall that way. Go another direction.')
            prompt()
        else:
            print('\n')
            print('\n')
            print(" a1 a2...        ")  
            print("----------       ")
            print("|  |  |  | a3    ")
            print("----------       ")
            print("|  |  |  | b3 ...")
            print("----------       ")
            print("|  |  |  |       ")
            print("----------       ")
            print('\n')
            print('\n')
            print('This is the map')
            print('\n' + 'You have moved to ' + location + '.')
            prompt()

def player_examine():
    print('\n')
    print('This room is the', zonemap[player.location][ZONENAME])
    print(zonemap[player.location][EXAMINATION] + '\n')
    if player.location == 'a3' and 'key' in player.inventory:
        game_win()
    elif player.location == room_with_key:
        print('Wait....There is a key on the floor. Pick it up? ')
        choice = input('yes/no? ')
        if choice == 'yes':
            player.inventory.append('key')
            print('You can now operate the escape pods')
            print('\n')
            prompt()
        else:
            prompt()
    else:
        prompt()
    
def game_win():
    print('Do you want to get in an escape pod and head back to Earth?')
    answer = input('yes/no? ')
    if answer == 'yes':
        print('You\'ve escaped, ' + player.name + '!')
        print('You win!')
    elif answer == 'no':
        prompt()
    else:
        game_win()

prompt()




    



