# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from typing import Sized


class Board:
    """
    Creates Boards for both the user and the computer.
    """
    def __init__(self, size, name, num_of_ships):
        self.size = size
        self.name = name
        self.num_of_ships = num_of_ships
        