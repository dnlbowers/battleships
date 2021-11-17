# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random


class Player:
    """
    Creates a player object
    """
    def __init__(self, name):
        self.name = name
        self.board = Board()
        self.guesses = []
        self.guess_index = 0


class Board:
    """"Build the boards"""
    board_size = 10

    def __init__(self, player):      
        self.player = player
        self.board = self.build_board()
        self.fleet = self.build_fleet() #This needs to colate all ship objects

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
    #Build fleet here

class Ship:
    """
    Creates the ship class for later sub class of ships.
    """
    def __init__(self, name, length, start_coordinate, direction, damaged_tiles):
        self.name = name #sub class
        self.length = length #sub
        self.start_coordinate = start_coordinate
        self.direction = direction
        self.damaged_tiles = damaged_tiles
        self.coordinates = []

    #This needs to be moved into the board class.
    def build_ship_objects(self, set_up_type):
        """
        Builds a list of ship objects.
        """
        #these will be the sub classes of the ship.
        ship_type = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
        ship_length = [5, 4, 3, 3, 2]
        fleet = []

        if set_up_type == "auto":
#Need to break these up before creating instance of object. and check to ensure no clashes or off the board 
            for i in range(len(ship_type)):
                ship_instance = Ship(ship_type[i], ship_length[i], (random.randint(0, 9),
                    random.randint(0, 9)), random.choice(["r", "d"]), [])
                fleet.append(ship_instance)

            return fleet

        elif set_up_type == "manual":
 
            for i in range(len(ship_type)):

                start_position = input(f"Start coordinate for your {ship_type[i]}?/n"
                    "Separate to numbers with a comma i.e 4,5 : ").split(",")
                start_position = [int(i) for i in start_position]                
                ship_instance = Ship(ship_type[i], ship_length[i], start_position,
                    (input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")), [])
                fleet.append(ship_instance)

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

class Carrier(Ship):
    """
    Creates an instance of the Carrier class.
    """
    name = "Carrier"
    length = 5

    def __init__(self, start_coordinate, direction, damaged_tiles):
        super().__init__(start_coordinate, direction, damaged_tiles)
        


class Battleship(Ship):
    """
    Creates an instance of the Battleship class.
    """
    
    name = "Battleship"
    length = 4
    def __init__(self, start_coordinate, direction, damaged_tiles):
        super().__init__(start_coordinate, direction, damaged_tiles)


class Cruiser(Ship):
    """
    Creates an instance of the Cruiser class.
    """
    name = "Cruiser"
    length = 3
    def __init__(self, start_coordinate, direction, damaged_tiles):
        super().__init__(start_coordinate, direction, damaged_tiles)


class Submarine(Ship):
    """
    Creates an instance of the Submarine class.
    """
    name = "Submarine"
    length = 3
    def __init__(self, start_coordinate, direction, damaged_tiles):
        super().__init__(start_coordinate, direction, damaged_tiles)

    
class Destroyer(Ship):
    """
    Creates an instance of the Destroyer class.
    """
    name = "Destroyer"
    length = 2
    def __init__(self, start_coordinate, direction, damaged_tiles):
        super().__init__(start_coordinate, direction, damaged_tiles)


print(Carrier.name)

#Construction of the game

# username= input("What is your name?: ")
# user = Player(username)
# cpu = Player("cpu")
# user_board = Board(user)
# cpu_board = Board(cpu)

# #Build a fleet and place at the same time
# test = Ship.build_ship_objects(CPU_board, "auto")
# for ship in test:
#     print(ship.build_ship())


# #test for object creation
# for obj in test:
#     print("-----")
#     print(obj.name)
#     print(obj.length)
#     print(obj.start_coordinate)
#     print(obj.direction)
#     print(obj.damaged_tiles)
#     print(obj.coordinates)

# print(issubclass(Ship, Player))
# print(isinstance(test[1], Player))