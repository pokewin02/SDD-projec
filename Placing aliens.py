#Placing the aliens

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
    def __init__(enemy):
        enemy.health = '75'
        enemy.attack = '15'
        enemy.location = 'a3'
enemy = Alien()

class Alien:
    def __init__(enemy):
        enemy.health = '75'
        enemy.attack = '15'
        enemy.location = 'a1'
enemy = Alien()

class Alien:
    def __init__(enemy):
        enemy.health = '75'
        enemy.attack = '15'
        enemy.location = 'c3'
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
        print('\n')
        print('That ain\'t one of the jobs.')

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

if enemy.location == 'c3':
    print('wow')
