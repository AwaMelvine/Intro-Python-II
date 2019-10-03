from room import Room
from player import Player
from item import Item

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


# Put some items inside some of the rooms
items = {
    "apple": Item('Apple', 'A fruit you can eat.'),
    "ball": Item('Ball', 'Kids and grown ups alike run after it and kick it away when they meet it'),
    "car": Item('Car', 'A moving box that moves people from one place to another, crying all the while')
}

room['foyer'].items.append(items['apple'])
room['foyer'].items.append(items['car'])
room['narrow'].items.append(items['ball'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player("Awa", room["outside"])

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


def movePlayer(side, current_room):
    attrib = side + '_to'
    if hasattr(current_room, attrib):
        return getattr(current_room, attrib)
    print("Oops, no passage there. Try again...")
    return current_room


def displayPlayerInventory(player):
    if len(player.inventory) == 0:
        print(f"\nYou currently have no items")
    else:
        print(f"\nYou are carrying:")
        i = 0
        for item in player.inventory:
            i += 1
            print(f"{i}. {item.name}")


print("\nWELCOME TO ADVENTURELAND!\n\t\tINSTRUCTIONS\nEnter 'n', 'w', 's', 'e' to navigate\nEnter command to add or drop itmes or q to quit:")

done = False

while not done:
    print(newPlayer.current_room)

    direction = input("Command> ").strip().lower()

    if direction == 'q':
        print("\nGood Bye!")
        done = True
    elif direction in ['n', 'w', 's', 'e']:
        newPlayer.current_room = movePlayer(direction, newPlayer.current_room)
    elif direction == 'i':
        displayPlayerInventory(newPlayer)
    elif direction.split(' ')[0] == 'take' or direction.split(' ')[0] == 'get':
        selected = direction.split(' ')[1]
        if selected in items:
            newPlayer.on_take(items.get(selected))
            print(f"You have picked up {items.get(selected).name}")
            newPlayer.current_room.items.remove(items.get(selected))
        else:
            print("Item not found")
    else:
        print("Invalid command\n")
