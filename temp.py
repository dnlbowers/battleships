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


#this may be a subclass of board to place ships

class Ships(Board):
    """
    Creates a naval fleet to be placed on the board by the player.
    Give method for auto deployment of ships on the board.
    Auto deployment is optional for the player but mandatory for the computer.
    """
    def __init__(self, name):
        super().__init__(name)
        self.naval_fleet = {
            "Carrier": 5,
            "Battleship": 4,
            "Cruiser": 3,
            "Submarine": 3,
            "Destroyer": 2
    }

    def auto_deploy(self):
        """
        Auto deploys ships on the board.
        """
        coordinates = [(random.randint(0, 9), random.randint(0, 9))
            for _ in range(len(self.naval_fleet))]
        direction = [random.randint(0,1) for _ in range(len(self.naval_fleet))]
        
        print (direction)
        print (coordinates)


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


# Build boards
player_board = Board(10, "Player", 5)
pprint(player_board.build_board())

player_name = input("What is your name? ")
player = Ship(player_name)
computer = Ship("Computer")


pprint(player.__dict__)
pprint(computer.__dict__)

print(player.name + ", place your ships!")

Ships.print_board(player)
Ships.print_board(computer)
Ships.auto_deploy(player)

print(issubclass(Ships, Player))
print(isinstance(player, Player))
#print(help(Ships))
