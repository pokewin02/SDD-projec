#Making characters

class Fireman:
    def __init__(self):
        self.maxhealth = '70'
        self.health = self.maxhealth
        self.base_attack = '20'
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
        self.maxhealth = '80'
        self.health = self.maxhealth
        self.base_attack = '10'
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
        self.maxhealth = '60'
        self.health = self.maxhealth
        self.base_attack = '30'
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
        self.maxhealth = '40'
        self.health = self.maxhealth
        self.base_attack = '40'
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
