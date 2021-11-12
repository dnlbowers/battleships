# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint

class Player:
    """
    Creates a player object
    """
    num_of_ships = 5
    board_size = 10
    def __init__(self, name):
        self.name = name
        

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


player_name = input("What is your name? ")
player = Player(player_name)
computer = Player("Computer")

pprint(player.build_board())
pprint(computer.build_board())
print(player.name + ", place your ships!")
