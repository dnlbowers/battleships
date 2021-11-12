# Write your code to expect a terminal of 80 characters wide and 24 rows high
from pprint import pprint

class Player:
    """
    Creates a player object
    """
    
    def __init__(self, name, board_size, num_of_ships):
        self.name = name
        self.board_size = board_size
        self.num_of_ships = num_of_ships

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


name = input("What is your name? ")
player = Player(name, 10, 5)
computer = Player("Computer", 10, 5)

pprint(player.build_board())
pprint(computer.build_board())
print(player.name + ", place your ships!")
