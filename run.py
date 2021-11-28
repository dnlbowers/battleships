# To check:
# How to print the boards side by side 
#How to add index to the outside - LOW Priority
#line 78 how to access the player name from board for the initial placement function
#Mixin for the static methods? i,e original tile check in ship also used in board
# better way to do duplicate_tile_check() I am thinking class method, but there is a call in ship and in board so maybe a mixin?

#infinate loop sporadically occurs in build ship. 

#to do
#still occasional clashes. I suspect from the while loop before check coord function
#"Already ship here prints even for auto placement.... move print statement elsewhere"

#notes


# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random


class Player:
    """
    Creates a player object
    """
    def __init__(self, name):
        self.name = name
        if self.name == "computer":
            self.board = Board(name)
        else:
            result = input("(a)uto  or (m)anual?: ") #place inout into a function with while loop and then call input checker from there
            auto = self.input_checker(result)
            self.board = Board(name, auto)
        self.guesses = []
        self.guess_index = 0


    @classmethod #static method maybe
    def input_checker(cls, result):
        # add checks later includeding  one for m - needs to return True or False 
        if result == "a":
            return True
        elif result == "m":
            return False
        else:
            print("not valid input will add while loop, variable called valid = false and set to true when a or m is press")

    
    def user_fire(self):
        guess_coordinate = input('"Sir! Where should we fire the first excess round?" : eg 0,4 \n').split(",")
        guess_coordinate = self.guesses.append(tuple(int(i) for i in guess_coordinate))


class Board:
    """"Build the boards"""
    board_size = 10
    
    def __init__(self, owner, auto = True): 
        self.owner = owner
        self.auto = auto     
        self.board = self.build_board()
        self.fleet =  self.build_fleet()
        self.fleet_coords_map = self.fleet_coords_map() 
        

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
        print(f"     {self.owner}'s board:")
        print(" ")
        print("    0 1 2 3 4 5 6 7 8 9")
        print("   +-+-+-+-+-+-+-+-+-+-")
        row_num = 0
        for row in self.board:
            print(row_num, "|", " ".join(row))
            row_num += 1
        print(" ")
    

    def build_fleet(self):
        """
        Builds a fleet of ships.
        """
        fleet = []
        occupied_coordinates = []
        ship_obj_type =  [Aircraft_carrier, Battleship, Cruiser, Submarine, Destroyer]
   
        for i in range(5):

            if self.auto:
                random_start = (random.randint(0, 9), random.randint(0, 9))
                random_direction = random.choice(["r", "d"])
                ship_instance = ship_obj_type[i](random_start, random_direction, (random_start))

            else:
                start_position = input(f"Start coordinate for your {ship_obj_type[i].name}?"
                    "Separate to numbers with a comma i.e 4,5 : ").split(",")
                
                start_position = tuple(int(i) for i in start_position)
                direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                ship_instance = ship_obj_type[i]((start_position), direction, (start_position))

            self.build_ship(self.auto, ship_instance, occupied_coordinates)  
            occupied_coordinates.append(ship_instance.coordinates)
            
            self.initial_placement(ship_instance, self.auto)
            
            fleet.append(ship_instance)
        if self.auto:
            self.print_board()
        return fleet


    def build_ship(self, auto_placement, ship, occupied_tiles):
        """
        Builds the ship in the chosen direction and advises user if the intended location
        is already occupied. if required asks for/generates randomly a new start coordinate.
        """
        placement_process = True

        while placement_process:
            
            temp_ship = []
            temp_ship.append(ship.start_coordinate)

            for i in range(1, ship.length):
                
                if ship.direction == "d":
                    next_tile = (ship.start_coordinate[0] + i, ship.start_coordinate[1])
                    index_to_increment = 0

                elif ship.direction == "r":
                    next_tile = (ship.start_coordinate[0], ship.start_coordinate[1] + i)
                    index_to_increment = 1
                duplicate_tile = self.duplicate_tile_check(ship, occupied_tiles, next_tile)

                if ship.start_coordinate[index_to_increment] + ship.length > 9:
                    
                    if auto_placement:
                        ship.start_coordinate = (random.randint(0, 9), random.randint(0, 9))
                        ship.direction = random.choice(["r", "d"]) 
                        break
                    else:
                        print("Out of bounds")
                        ship.start_coordinate = input(f"Pick a new start coordinate for your {ship.name}? /n"
                            "Separate two numbers with a comma i.e 4,5 : ").split(",")
                        ship.start_coordinate = tuple(int(i) for i in ship.start_coordinate) 
                        ship.direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                        break    

                elif not duplicate_tile:
                    temp_ship.append(next_tile)
                    if len(temp_ship) == ship.length:
                        ship.coordinates = temp_ship
                        placement_process = False
                        return ship.coordinates 
                #look to condense   
                else:
                    if auto_placement:
                        ship.start_coordinate = (random.randint(0, 9), random.randint(0, 9))
                        ship.direction = random.choice(["r", "d"]) 
                        break
                    elif not auto_placement:
                        print("There is already another ship here...")
                        ship.start_coordinate = input(f"Pick a new start coordinate for your {ship.name}? /n"
                            "Separate two numbers with a comma i.e 4,5 : ").split(",")
                        ship.start_coordinate = tuple(int(i) for i in ship.start_coordinate) 
                        ship.direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                        break                   
        
        return ship.coordinates
    

    @staticmethod
    def duplicate_tile_check(ship, occupied_tiles, next_tile):
        """
        Checks if a tile is occupied before allowing a ship to be placed across it.
        """
        for list in occupied_tiles:
            for coord in list:
                if  next_tile in list:
                    return True
                elif ship.start_coordinate in list:
                    return True    
    
    def fleet_coords_map(self):
        """"
        Creates a dictionary of the fleets coordinates. 
        Key = coordinate 
        Value = Ship symbol to identify which ship was hit
        """
        
        ship_log = {}
        for i in range(5):
            ship_log.update(dict(zip(self.fleet[i].coordinates, self.fleet[i].symbol_list)))
        return ship_log 

    
    def initial_placement(self, ship, auto_placement = False):
        """
        If auto placement = False (Manually placed ships) - Prints a board showing each ship in the chose location

        """
        for i in range(ship.length):
            self.board[ship.coordinates[i][0]][ship.coordinates[i][1]] = ship.symbol_list[i]
        if not auto_placement:    
            self.print_board()

   

class Ship:
    """
    Creates the ship class for later sub class of ships.
    """
    def __init__(self, start_coordinate, direction, coordinates):
        self.start_coordinate = start_coordinate
        self.direction = direction
        self.damaged_tiles = [False] * self.length
        self.coordinates = coordinates


    def is_destroyed():
        pass

class Aircraft_carrier(Ship):
    """
    Creates an instance of the Aircraft_carrier class.
    """
    name =  "Aircraft_carrier"
    length = 5
    symbol_list = ["A"] * length

    def __init__(self, start_coordinate, direction, coordinates):
        super().__init__(start_coordinate, direction, coordinates)
        
        
class Battleship(Ship):
    """
    Creates an instance of the Battleship class.
    """
    name = "Battleship"
    length = 4
    symbol_list = ["B"] * length

    def __init__(self, start_coordinate, direction, coordinates):
        super().__init__(start_coordinate, direction, coordinates)


class Cruiser(Ship):
    """
    Creates an instance of the Cruiser class.
    """
    name = "Cruiser"
    length = 3
    symbol_list = ["C"] * length

    def __init__(self, start_coordinate, direction, coordinates):
        super().__init__(start_coordinate, direction, coordinates)


class Submarine(Ship):
    """
    Creates an instance of the Submarine class.
    """
    name = "Submarine"
    length = 3
    symbol_list = ["S"] * length

    def __init__(self, start_coordinate, direction, coordinates):
        super().__init__(start_coordinate, direction, coordinates)

    
class Destroyer(Ship):
    """
    Creates an instance of the Destroyer class.
    """
    name = "Destroyer"
    length = 2
    symbol_list = ["D"] * length

    def __init__(self, start_coordinate, direction, coordinates):
        super().__init__(start_coordinate, direction, coordinates)


#Construction of the game

#This now creates a player, board, and feet.
# player_name = input("What is your name? ")
user = Player(input("What is your name? "))
computer = Player("computer")

# print(user.board.fleet_coords_map)
# cpu = Player("computer")
# print(cpu.board.fleet_coords_map)
# print(cpu.board.__dict__)

#How do I apply this propely? reference print boards side by side https://www.codegrepper.com/code-examples/python/how+to+print+two+lists+side+by+side+in+python
res = "\n".join("{} {}".format(x, y) for x, y in zip(user.board.board, computer.board.board))

# it works but I cannot access the print board to tidy it up
print(res)
# print(user.board.__dict__)
# print(computer.__dict__)


# print(user.board.ship_log())
# for i in range(len(user.board.fleet)):
#     print(user.board.ship_log(user.board.fleet[i]))
# Player("computer")
