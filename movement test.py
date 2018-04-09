def prompt():
    print('\n')
    print("Would you like to do?")
    print("1) Move room")
    print("2) Examine rooms")
    action = input("Number of choice: ")
    acceptable_actions = ('1', '2')
    while action not in acceptable_actions:
        print("Action unknown. Please try again."),
        action = input("Number of choice: ")
    if action == '1':
        player_move()
    elif action == '2':
        player_examine()

def player_move():
    destination = input("Where do you want to go? ")
    if destination in ['up', 'north']:
        print('Hi')
        #if zonemap[player.location][UP] == '':
            #print ('There is a wall that way. Go another direction.')
            #prompt()
        #else:
            #location = zonemap[player.location][UP]
            #movement_handler(location)
    elif destination in ['down', 'south']:
        if zonemap[player.location][DOWN] == '':
            print ('There is a wall that way. Go another direction.')
            prompt()
        else:
            location = zonemap[player.location][DOWN]
            movement_handler(location)
    elif destination in ['left', 'west']:
        if zonemap[player.location][LEFT] == '':
            print ('There is a wall that way. Go another direction.')
            prompt()
        else:
            location = zonemap[player.location][LEFT]
            movement_handler(location)
    elif destination in ['right', 'east']:
        if zonemap[player.location][RIGHT] == '':
            print ('There is a wall that way. Go another direction.')
            prompt()
        else:
            location = zonemap[player.location][RIGHT]
            movement_handler(location)
    else:
        print('invalid direction'),
        player_move()

def movement_handler(location):
    player.location = location
    if player.location == enemy1.location:
        battle()
    elif player.location == enemy2.location:
        battle()
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


prompt()
