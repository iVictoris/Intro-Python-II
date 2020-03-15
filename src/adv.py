from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

"""
                    outside
narrow       foyer
treasure     overlook
"""

room['outside'].rooms['south'] = room['foyer']
room['foyer'].rooms['north'] = room['outside']
room['foyer'].rooms['south'] = room['overlook']
room['foyer'].rooms['west'] = room['narrow']
room['overlook'].rooms['north'] = room['foyer']
room['narrow'].rooms['east'] = room['foyer']
room['narrow'].rooms['south'] = room['treasure']
room['treasure'].rooms['north'] = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player = Player('Victor')
while (True):
    location = player.location
    print(f'You are currently here: {location}')
    choice = input(
        'Please enter a direction in which you\'d like to go: n, e, s, w or q to quit: ')
    valid_choices = ['n', 'e', 'w', 's', 'q']
    if choice not in valid_choices:
        print('Invalid choice, please try again')
        continue
    if (choice == 'q'):
        print('You\'ve elected to quit, so good bye.')

    # figure out a way to print room => __str__
    if choice == 's':

        if (room[location].rooms['south']):
            print(room[location].rooms['south'])
