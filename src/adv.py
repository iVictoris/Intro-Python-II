from room import Room
from player import Player

def main():

    room = {
        'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", ['Common Staff', 'Common Sword']),
        'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east.""", ['Rare Staff', 'Rare Sword', 'Rare Armor']),

        'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm.""", ['Rare Gloves', 'Epic Sword', 'Epic Staff', 'Epic Bow', 'Epic Glove']),

        'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air."""),

        'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south."""),
    }

    room['outside'].assign_room('s', room['foyer'])
    room['foyer'].assign_room('s', room['overlook'])
    room['foyer'].assign_room('w', room['narrow'])
    room['overlook'].assign_room('n', room['foyer'])
    room['narrow'].assign_room('s', room['treasure'])
    valid_choices = list('newsq')

    # Make a new player object that is currently in the 'outside' room.
    player = Player('Me', room['outside'])

    # Player's __str__ method prints its name and room location
    while True:
        print('\n')
        print(player)

        # get room will return the room the player is currently in
        print('\n' + player.get_room().get_description())

        choice = input('Please choose what direction you would like to go or enter a take/drop command: ').split(' ')
        
        # only if len(choice) < 1 or take or drop not inside choice
        if (len(choice) < 1 or ('take' not in choice and 'drop' not in choice)):
            continue

        elif (len(choice) == 1):

        if (choice not in valid_choices):
            print(f'Choices can only be {", ".join(valid_choices).rstrip() }.')
            continue


        if (choice == 'q'):
            return
        try:
            player.enter_room(choice)
                continue
        except ValueError:
            print('Unfortunately, that path does not exist, please try again')
            continue

        # here the choices > 1
        verb, *item = choice
        item = ' '.join(item)
        # if user enters get/take
        if verb == 'get' or verb == 'take':
            current_room = player.get_room()
if __name__ == '__main__':
    main()
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
