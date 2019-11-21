# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __repr__(self):
        return f' {self.name} {self.current_room}'
    
    
    def travel_to(self, input_direction):
        newRoom = self.current_room.determinedPathFromCurrent(input_direction)
        if newRoom is not None:
            self.current_room = newRoom
        else:
            print("There's nowhere to go in that direction, Please try another direction")