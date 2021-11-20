#to do
# in build_fleet function - if first ship in fleet build_ship() before appending and add coordinates to a list
                    #any ship after this make sure that the coordinates are not already
                    #in the above mentioned list before creating the ship object

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

    def __init__(self):      
        self.board = self.build_board()
        self.fleet =  self.build_fleet(input("(a)uto  or (m)anual?: ")) #How to add a conditional here so it doesn't ask for input if it's a computer

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

    def print_board(self, player_object):
        """
        Prints the board.
        """
        print(f"{player_object.name}'s board:")

        for row in self.board:
            print(" ".join(row))
    
    #Build fleet here
    def build_fleet(self, placement_type):
        """
        Builds a fleet of ships.
        """
        fleet = []
        occupied_coordinates = []
        ship_obj_type =  [Aircraft_carrier, Battleship, Cruiser, Submarine, Destroyer]
        
        if placement_type == "a":
            for i in range(5):

                random_start = [random.randint(0, 9), random.randint(0, 9)]
                occupied_coordinates.append(random_start)
                random_direction = random.choice(["r", "d"])
                ship_instance = ship_obj_type[i](random_start, random_direction, [], random_start)
                print(ship_instance.name)
                print(ship_instance.coordinates)
                print(ship_instance.direction)

                ship_instance.build_ship()
                # here we need to build the ship by adding coordinates to the obj(ship_instance.coordinaes) and check 
                #each tile agains the occupied tile list before placing


                
                fleet.append(ship_instance)
                #how do i add the coordinates to the list of coordinates?
                #occupied_coordinates.append(ship_instance.coordinates) 
                # ship = ship_instance.build_ship()
                # print(ship) 
                # hi = ship_instance.build_ship(ship_instance.coordinates, ship_instance.direction, ship_instance.length, ship_instance.coordinates)
                # print(hi)
                
                
                
                print(occupied_coordinates)
                
                # print(occupied_coordinates[0][1])
                # # this is how to add to it
                # print(occupied_coordinates[0][1]+1)
                # print(occupied_coordinates[0])
                # print(fleet[i].name)
                # print(fleet[i].length)
                # print(fleet[i].__dict__)
                
            return fleet
            # print(fleet)

        elif placement_type == "m":
            for i in range(5):
                start_position = input(f"Start coordinate for your {ship_obj_type[i].name}?/n"
                    "Separate to numbers with a comma i.e 4,5 : ").split(",")
                start_position = [int(i) for i in start_position]

                ship_instance = ship_obj_type[i](start_position,
                    (input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")), [], start_position)
                fleet.append(ship_instance)
            return fleet    
    

        

class Ship:
    """
    Creates the ship class for later sub class of ships.
    """
    def __init__(self, start_coordinate, direction, damaged_tiles, coordinates):
        self.start_coordinate = start_coordinate
        self.direction = direction
        self.damaged_tiles = damaged_tiles
        self.coordinates = []

    # Check the output here and how to get this into the ship opject
    def build_ship(self):
        for i in range(5):
            if self.direction == "r":
                self.coordinates.append([self.start_coordinate[0] + i, self.start_coordinate[1]])
            elif self.direction == "d":
                self.coordinates.append([self.start_coordinate[1], self.start_coordinate[1] + i])               
        # start is now a list of lists
        print(self.coordinates)

    # @classmethod
    # def build_ship(cls, start_coordinate, direction, length, coordinates):
    #     """
    #     Builds a ship object.
    #     """
    #     for i in range(length):
    #         if direction == "r":
    #             coordinates.append(tuple(start_coordinate[0] + i))
    #         elif direction == "d":
    #             coordinates.append(tuple(start_coordinate[1] + i))
    #     return  coordinates


    # def build_ship(self):
    #     """
    #     Builds a ship.
    #     """
    #     if self.direction == "r":
    #         for i in range(self.length):
    #             self.coordinates.append(tuple(self.start_coordinate[0] + i, self.start_coordinate[1]))
    #         return self.coordinates  
    #     elif self.direction == "d":
    #         for i in range(len(self.coordinates)):
    #             self.coordinates.append(tuple(self.start_coordinate[0], self.start_coordinate[1] + i))
    #         return self.coordinates

class Aircraft_carrier(Ship):
    """
    Creates an instance of the Aircraft_carrier class.
    """
    name =  "Aircraft_carrier"
    length = 5
    symbol = "A"

    def __init__(self, start_coordinate, direction, damaged_tiles, coordinates):
        super().__init__(start_coordinate, direction, damaged_tiles, coordinates)
        
        


class Battleship(Ship):
    """
    Creates an instance of the Battleship class.
    """
    name = "Battleship"
    length = 4
    symbol = "B"

    def __init__(self, start_coordinate, direction, damaged_tiles, coordinates):
        super().__init__(start_coordinate, direction, damaged_tiles, coordinates)


class Cruiser(Ship):
    """
    Creates an instance of the Cruiser class.
    """
    name = "Cruiser"
    length = 3
    symbol = "C"

    def __init__(self, start_coordinate, direction, damaged_tiles, coordinates):
        super().__init__(start_coordinate, direction, damaged_tiles, coordinates)


class Submarine(Ship):
    """
    Creates an instance of the Submarine class.
    """
    name = "Submarine"
    length = 3
    symbol = "S"

    def __init__(self, start_coordinate, direction, damaged_tiles, coordinates):
        super().__init__(start_coordinate, direction, damaged_tiles, coordinates)

    
class Destroyer(Ship):
    """
    Creates an instance of the Destroyer class.
    """
    name = "Destroyer"
    length = 2
    symbol = "D"

    def __init__(self, start_coordinate, direction, damaged_tiles, coordinates):
        super().__init__(start_coordinate, direction, damaged_tiles, coordinates)




#Construction of the game

#This now creates a player, board, and feet.
player_name = input("What is your name? ")
user = Player(player_name)
# print(user.__dict__)
# print(user.board.__dict__)
# print(user.board.fleet[0].__dict__)

#Need to figure out how to tell this to default auto placement of ships.
# computer = Player("Computer")
# for ship in user.board.fleet:
#     print (ship.start_coordinate)
#     print(ship.direction)
#     print(ship.coordinates)



#----------------------------------Junk constructors------------------------------------------------------------------
# user.board.build_board()
# user.board.print_board(user)
# computer.board.print_board(computer)

# print(user.board.fleet[1].name)

# print(user.__dict__)
# print(user.board.__dict__)

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