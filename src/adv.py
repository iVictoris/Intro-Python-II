from room import Room
from player import Player

def main():

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
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

room['outside'].assign_room('s', room['foyer'])
room['foyer'].assign_room('s', room['overlook'])
room['foyer'].assign_room('w', room['narrow'])
room['overlook'].assign_room('n', room['foyer'])
room['narrow'].assign_room('s', room['treasure'])
    valid_choices = list('newsq')

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Me', room['outside'])
        print('\n')
        print(player)

        # get room will return the room the player is currently in
        print('\n' + player.get_room().get_description())

        choice = input('Please choose what direction you would like to go: ')

        if (choice not in valid_choices):
            print(f'Choices can only be {", ".join(valid_choices).rstrip() }.')
            continue


        if (choice == 'q'):
            return
        try:
            player.enter_room(choice)
        except ValueError:
            print('Unfortunately, that path does not exist, please try again')
            continue
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
