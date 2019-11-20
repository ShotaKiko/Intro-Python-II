from room import Room
from player import Player

# class Game:
    # def __init__ (self, player, rooms =[]):
    #     self.player = player
    #     self.rooms = rooms

    # def __str__(self):
    #     output = ""
    #     for player in self.player:
    #         output += f'Welcome {player.name} \n'
    #     i = 1
    #     for room in self.rooms:
    #         output += f'{i}. {room.name} \n'
    #         i += 1
    #     return output
#     

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

adventurer_name = input("Please enter your name adventurer, glory awaits:")

new_player = Player( adventurer_name, room["outside"])

print(f'{new_player.name} is currently in the {new_player.current_room}')
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

user_input = ""
valid_inputs = ["n", "north", "North", "s", "south", "South", "w", "west", "West", "e", "east", "East"]
ending_inputs = ["q", "quit", "Quit", "exit", "Exit"]

while user_input not in ending_inputs:
    user_input = input("In which direction do you want to proceed?")

    if user_input in valid_inputs:
        new_player.current_room = travel(user_input, new_player.current_room)
        print(f'You are currently in the{new_player.current_room} room.')
    elif user_input in ending_inputs:
        print(f'{new_player.name} has left the game.')
    else:
        print("East? I thought you said Weast! Enter valid direction please!")
        





