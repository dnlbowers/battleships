# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint

# This will generate the boards co-ordinates
#coordinates = [(row, column) for row in range(self.rows) for column in range(self.columns)]

#creates a dictionary of coordinates, will use later to place ships and check for hits
# {(row,column):"~" for row in range(self.rows) for column in range(self.columns)
#             if row != 0 and column != 0}
# for the player guess consider a class method to split the string https://youtu.be/rq8cL2XMM5M
class Board:
    """
    Creates Boards for both the user and the computer.
    """
    def __init__(self, size, name, num_of_ships):
        self.size = size
        self.name = name
        #think about making this a class variable(num_of_ships = 5) but may need
        #to move to ships class
        #sample - https://www.youtube.com/watch?v=BJ-VvGyQxho
        self.num_of_ships = num_of_ships

    #maybe make this a static method @staticmethod func with no params https://youtu.be/rq8cL2XMM5M
    def build_board(self):
        """
        Builds a blank board with coordinates as a key.
        """
        board = []
        for row in range(self.size):
            board.append([])
            for _ in range(self.size):
                board[row].append("~")
        return board

#this may be a subclass of board to place ships
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
player_board = Board(10, "Player", 5)
pprint(player_board.build_board())
