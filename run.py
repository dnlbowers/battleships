# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint
import random

class Player:
    """
    Creates a player object
    """
    def __init__(self, name):
        self.name = name


class Board(Player):
    """"Build the boards"""
    board_size = 10
    def __init__(self, name):
        super().__init__(name)
        self.board = self.build_board()

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

    def print_board(self):
        """
        Prints the board.
        """
        print(self.name + "'s board:")
        for row in self.board:
            print(" ".join(row))

class Ship:
    """
    Creates the ship class for later sub class of ships.
    """
    def __init__(self, name, length, start_coordinate, direction, damaged_tiles):
        self.name = name
        self.length = length
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



# how do I put this into the class? 
# I want to be able to use the below to create a ship object for and add to the board.
ship_keys = ["name", "length"]
name_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
length_list = [5, 4, 3, 3, 2]
fleet = []

# the logic to auto create fleet and auto place them on the board.
for i in range(len(name_list)):
    ship = Ship(name_list[i], length_list[i], (random.randint(0, 9), random.randint(0, 9)), random.choice(["r", "d"]), [])
    fleet.append(ship) 
    
    print(ship.__dict__)
print(fleet[0].build_ship())
print(fleet[1].build_ship())



# start_position = input("Where would you like to place your Aircraft Carrier? Separate to numbers with a comma i.e 4,5 : ").split(",")
# start_position = [int(i) for i in start_position]
# print(start_position)

# Carrier =Ship("Aircraft Carrier",5, start_position, "d", [])
# Carrier.build_ship()
# print(Carrier.coordinates)

# start_position = input("Where would you like to place your Submarine? Separate to numbers with a comma i.e 4,5 : ").split(",")
# start_position = [int(i) for i in start_position]
# print(start_position)

# sub =Ship("Submarine", 3, start_position, "r", [])
# sub.build_ship()
# print(sub.coordinates)
# print(Carrier.coordinates)




# player_name = input("What is your name? ")
# player = Board(player_name)
# computer = Board("Computer")


# pprint(player.__dict__)
# pprint(computer.__dict__)

# print(player.name + ", place your ships!")

# Board.print_board(player)
# Board.print_board(computer)