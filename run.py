# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint

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


class Ships(Board, Player):
    """
    Creates a naval fleet to be placed on the board by the player.
    Give method for auto deployment of ships on the board.
    Auto deployment is optional for the player but mandatory for the computer.
    """
    naval_fleet = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2
    }
    #How to __init__ ? 

    #Possible method to place ships on the board:
    # def place_ship(self, ship, start_row, start_col, end_row, end_col):
    #     """
    #     Places a ship on the board.
    #     """
    #     if start_row == end_row:
    #         for col in range(start_col, end_col + 1):
    #             self.board[start_row][col] = ship
    #     elif start_col == end_col:
    #         for row in range(start_row, end_row + 1):
    #             self.board[row][start_col] = ship
    #     else:
    #         raise ValueError("Invalid ship placement.")

player_name = input("What is your name? ")
player = Board(player_name)
computer = Board("Computer")


pprint(player.__dict__)
pprint(computer.__dict__)

print(player.name + ", place your ships!")

Board.print_board(player)
Board.print_board(computer)

print(issubclass(Ships, Player))
print(isinstance(player, Player))
