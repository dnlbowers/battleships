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

    def build_ship_objects(self, set_up_type):
        """
        Builds a list of ship objects.
        """
        name_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
        length_list = [5, 4, 3, 3, 2]
        fleet = []
        if set_up_type == "auto":
            for i in range(len(name_list)):
                ship = Ship(name_list[i], length_list[i], (random.randint(0, 9), random.randint(0, 9)), random.choice(["r", "d"]), [])
                fleet.append(ship)
            return fleet
        elif set_up_type == "manual":
            for i in range(len(name_list)):
                start_position = input(f"Start coordinate for your {name_list[i]}?/n Separate to numbers with a comma i.e 4,5 : ").split(",")
                start_position = [int(i) for i in start_position]
                test = Ship(name_list[i], length_list[i], start_position, (input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")), [])
                fleet.append(test)
            return fleet

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


# test = Ship.build_ship_objects(Board, "auto")
# for i in test:
#     print(i.build_ship())
username= input("What is your name?: ")
user_board = Board(username)
CPU_board = Board("CPU")
user_board.print_board()
CPU_board.print_board()

