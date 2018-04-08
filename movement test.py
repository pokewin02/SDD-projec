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
    dest = input("Where do you want to go? ")
    destination = str(dest)
    if destination == ('up', 'north'):
        print("hi")
        #location = zonemap[player.location][UP]
        #movement_handler()
    elif destination == ('down', 'south'):
        location = zonemap[player.location][DOWN]
        movement_handler()
    elif destination == ('left', 'west'):
        location = zonemap[player.location][LEFT]
        movement_handler()
    elif destination == ('right', 'east'):
        location = zonemap[player.location][RIGHT]
        movement_handler()

#def movement_handler():
        #location = player.location
        #print('\n' + 'You have moved to ' + player.location + '.')

prompt()
