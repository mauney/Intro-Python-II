from item import Item
from player import Player
from room import Room
from textwrap import fill

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Create some items

items = {
    'shovel': Item('shovel',
                   'a garden shovel'),
    'marble': Item('marble',
                   'a blue marble')
}

# Place the items in the foyer
room['foyer'].add_item(items['shovel'])
room['foyer'].add_item(items['marble'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print('Welcome to your adventure!')
player_name = input('What is your name?\n')
player = Player(player_name, room['outside'])
print(f'Greetings, {player.name}!\n')

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

instructions = """Enter one of the following commands:
n to move north, e to move east, s to move south, or w to move west
d to describe your current location
i to list your inventory
r to view items in the room
c to see this list of commands
q to abandon your adventure
"""

print(instructions)

def unknown_command():
    print("I'm sorry, you command was not understood\n")
    print(instructions)

while True:
    cmd = input('~~>').lower().split()
    if len(cmd) == 1:
        cmd = cmd[0]
        if cmd in ['n', 'e', 's', 'w']:
            player.move(cmd)
        elif cmd == 'i' or cmd == 'inventory':
            print(player.list_inventory ())
        elif cmd == 'r':
            print(player.current_room.list_items())
        elif cmd == 'd':
            print(player.current_room.description)
        elif cmd == 'c':
            print(instructions)
        elif cmd == 'q':
            print(f'Thank for for playing, {player.name}! Come back any time.')
            exit()
        else:
            unknown_command()
    elif len(cmd) == 2:
        if cmd[0] == 'get' or cmd[0] == 'take':
            player.pickup_item(cmd[1])
        elif cmd[0] == 'drop' or cmd[0] == 'leave':
            player.drop_item(cmd[1])
        else:
            unknown_command()
    else:
        unknown_command()
