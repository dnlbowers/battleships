#to do
# in build_fleet function - if first ship in fleet build_ship() before appending and add coordinates to a list
                    #any ship after this make sure that the coordinates are not already
                    #in the above mentioned list before creating the ship object

# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random


class Player:
    """
    Creates a player object
    """
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.guesses = []
        self.guess_index = 0


class Board:
    """"Build the boards"""
    board_size = 10

    def __init__(self):      
        self.board = self.build_board()
        self.fleet =  self.build_fleet(input("auto  or manual?: ")) #How to add a conditional here so it doesn't ask for input if it's a computer

    def build_board(self):
        """
        Builds a blank board with coordinates as a key.
        """
        board = []

        for row in range(self.board_size):
            board.append([])
            for _ in range(self.board_size):
                board[row].append("~")

        return board

    def print_board(self, player_object):
        """
        Prints the board.
        """
        print(f"{player_object.name}'s board:")

        for row in self.board:
            print(" ".join(row))
    
    #Build fleet here
    def build_fleet(self, placement_type):
        """
        Builds a fleet of ships.
        """
        fleet = []
        ship_obj_type = [Carrier, Battleship, Cruiser, Submarine, Destroyer]
        
        if placement_type == "auto":
            for i in range(5):
                fleet.append(ship_obj_type[i]((random.randint(0, 9),
                    random.randint(0, 9)), random.choice(["r", "d"]), []))

            return fleet
        elif placement_type == "manual":
            for i in range(5):
                start_position = input(f"Start coordinate for your {ship_obj_type[i].name}?/n"
                    "Separate to numbers with a comma i.e 4,5 : ").split(",")
                start_position = [int(i) for i in start_position]

                ship_instance = ship_obj_type[i](start_position,
                    (input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")), [])
                fleet.append(ship_instance)
            return fleet
        

class Ship:
    """
    Creates the ship class for later sub class of ships.
    """
    def __init__(self, start_coordinate, direction, damaged_tiles):
        self.start_coordinate = start_coordinate
        self.direction = direction
        self.damaged_tiles = damaged_tiles
        self.coordinates = []

    def build_ship(self):
        """
        Creates list of coordinates for the ship.
        """
#Need to add a checking statement here to make sure the ship is not placed off the board.
        for i in range(self.length):
            if self.direction == "r":
                self.coordinates.append((self.start_coordinate[0], self.start_coordinate[1] + i))
            elif self.direction == "d":
                self.coordinates.append((self.start_coordinate[0] + i, self.start_coordinate[1]))
        return self.coordinates

class Carrier(Ship):
    """
    Creates an instance of the Carrier class.
    """
    name = "Carrier"
    length = 5

    def __init__(self, start_coordinate, direction, damaged_tiles):
        super().__init__(start_coordinate, direction, damaged_tiles)
        


class Battleship(Ship):
    """
    Creates an instance of the Battleship class.
    """
    
    name = "Battleship"
    length = 4
    def __init__(self, start_coordinate, direction, damaged_tiles):
        super().__init__(start_coordinate, direction, damaged_tiles)


class Cruiser(Ship):
    """
    Creates an instance of the Cruiser class.
    """
    name = "Cruiser"
    length = 3
    def __init__(self, start_coordinate, direction, damaged_tiles):
        super().__init__(start_coordinate, direction, damaged_tiles)


class Submarine(Ship):
    """
    Creates an instance of the Submarine class.
    """
    name = "Submarine"
    length = 3
    def __init__(self, start_coordinate, direction, damaged_tiles):
        super().__init__(start_coordinate, direction, damaged_tiles)

    
class Destroyer(Ship):
    """
    Creates an instance of the Destroyer class.
    """
    name = "Destroyer"
    length = 2
    def __init__(self, start_coordinate, direction, damaged_tiles):
        super().__init__(start_coordinate, direction, damaged_tiles)


print(Carrier.name)

#Construction of the game

#This now creates a player, board, and feet.
player_name = input("What is your name? ")
user = Player(player_name)

#Need to figure out how to tell this to default auto placement of ships.
# computer = Player("Computer")




#----------------------------------Junk constructors------------------------------------------------------------------
# user.board.build_board()
# user.board.print_board(user)
# computer.board.print_board(computer)

# print(user.board.fleet[1].name)

print(user.__dict__)
print(user.board.__dict__)

# username= input("What is your name?: ")
# user = Player(username)
# cpu = Player("cpu")
# user_board = Board(user)
# cpu_board = Board(cpu)

# #Build a fleet and place at the same time
# test = Ship.build_ship_objects(CPU_board, "auto")
# for ship in test:
#     print(ship.build_ship())


# #test for object creation
# for obj in test:
#     print("-----")
#     print(obj.name)
#     print(obj.length)
#     print(obj.start_coordinate)
#     print(obj.direction)
#     print(obj.damaged_tiles)
#     print(obj.coordinates)

# print(issubclass(Ship, Player))
# print(isinstance(test[1], Player))