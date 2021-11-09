# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint


class Board:
    """
    Creates Boards for both the user and the computer.
    """
    def __init__(self, rows, columns, name, num_of_ships):
        self.rows = rows
        self.name = name
        self.num_of_ships = num_of_ships
        self.columns = columns
    
    def build_board(self):
        """
        Builds a blank board.
        """
        board = []
        for row in range(self.rows):
            board.append([])
            for _ in range(self.columns):
                board[row].append("~")
        return board

class Ship:
    """
    Creates the ship class for later sub class of ships.
    """
    def __init__(self, length, start_position, direction, damaged_tiles):
        self.length = length
        self.start_position = start_position
        self.direction = direction
        self.damaged_tiles = damaged_tiles



# Build boards
player_board = Board(10, 10, "Player", 5)
pprint(player_board.build_board())