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
        print('hi')
        #location = zonemap[player.location][UP]
        #movement_handler()
    elif destination in ['down', 'south']:
        location = zonemap[player.location][DOWN]
        movement_handler()
    elif destination in ['left', 'west']:
        location = zonemap[player.location][LEFT]
        movement_handler()
    elif destination in ['right', 'east']:
        location = zonemap[player.location][RIGHT]
        movement_handler()
    else:
        print('invalid direction'),
        player_move()

#def movement_handler():
        #location = player.location
        #print('\n' + 'You have moved to ' + player.location + '.')

prompt()
