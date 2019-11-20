# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def findPossiblePaths(self):
        available_paths = []
        if self.n_to != None:
            available_paths.append("North")
        if self.s_to != None:
            available_paths.append("South")
        if self.w_to != None:
            available_paths.append("West")
        if self.e_to != None:
            available_paths.append("East")
        return available_paths
    
    def determinedPathFromCurrent(self, input_direction):
        northbound = ["n", "north", "North"]
        southbound = ["s", "south", "South"]
        westbound = ["w", "west", "West"]
        eastbound = ["e", "east", "East"]
    
        if input_direction in northbound:
            return self.n_to == "n"
        elif input_direction in southbound:
            return self.s_to == "s"
        elif input_direction in westbound:
            return self.w_to == "w"
        elif input_direction in eastbound:
            return self.e_to == "e"
        else:
            return None
    
    
    
    def __repr__(self):
        return f'{self.name}  \nA brief description:\n {self.description}\n Here are your options: [{self.findPossiblePaths()}]'
 



