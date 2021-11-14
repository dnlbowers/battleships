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
    def __init__(self, length, start_position, direction, damaged_tiles):
        self.length = length
        self.start_position = start_position
        self.direction = direction
        self.damaged_tiles = damaged_tiles
        self.coordinates = []

    def position_ship(self):
        """
        Creates list of coordinates for the ship.
        """
        for i in range(self.length):
            if self.direction == "r":
                self.coordinates.append((self.start_position[0], self.start_position[1] + i))
            elif self.direction == "d":
                self.coordinates.append((self.start_position[0] + i, self.start_position[1]))


Carrier =Ship(5, [4, 5], "d", [])
Carrier.position_ship()
print(Carrier.coordinates)