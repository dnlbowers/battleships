#INFINATE LOOP IN BUILD SHIP()

# To check:
#Mixin for the static methods? i,e original tile check in ship also used in board
# better way to do duplicate_tile_check() I am thinking class method, but there is a call in ship and in board so maybe a mixin?

#infinate loop sporadically occurs in build ship. 

#to do
#Make a dictionary for occupied tiles which has the coord as the key and the fleet[i].symbol as the value (i.e. S or C) 
# why doesn't build fleet detect same coord used twice? likely in the build ship function - *args?
# Consider making the occupied tiles a dictionary with the coord as the key and the 
# ship_instance_symbol as the value. This way we maybe skip ship coords and 
# just check the occupied tiles dictionary. Do we still need fleet?

#notes
#MAy be able to do away with damaged tiles

# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random


class Player:
    """
    Creates a player object
    """
    def __init__(self, name):
        self.name = name
        if self.name == "computer":
            self.board = Board()
        else:
            result = input("(a)uto  or (m)anual?: ")
            auto = self.input_checker(result)
            self.board = Board(auto)
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


class Board:
    """"Build the boards"""
    board_size = 10
    
    def __init__(self, auto = True):      
        self.board = self.build_board()
        self.ship_log =  self.build_fleet(auto)
        

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
    

    def build_fleet(self, auto_placement):
        """
        Builds a fleet of ships.
        """
        fleet = []
        occupied_coordinates = []
        ship_obj_type =  [Aircraft_carrier, Battleship, Cruiser, Submarine, Destroyer]
        ship_log = {} 

        
        if auto_placement:
            for i in range(5):
                print("------------")
                not_original = False
                
                random_start = (random.randint(0, 9), random.randint(0, 9))
                random_direction = random.choice(["r", "d"])
                
                #could this be class method in ship?
                
                duplicate_tile = Ship.duplicate_tile_check(random_start, occupied_coordinates, random_start)
                if i == 0:
                    ship_instance = ship_obj_type[i](random_start, random_direction, (random_start))
                    ship_instance.build_ship(True, occupied_coordinates)
                    # not_original = True

                elif not duplicate_tile:
                    ship_instance = ship_obj_type[i](random_start, random_direction, (random_start))
                    ship_instance.build_ship(True, occupied_coordinates)
                    # not_original = True

                else:
                    not_original = True
                    while not_original == True:
                        random_start = (random.randint(0, 9), random.randint(0, 9))
                        not_original = duplicate_tile = Ship.duplicate_tile_check(random_start, occupied_coordinates, random_start)
                        ship_instance = ship_obj_type[i](random_start, random_direction, (random_start))
                        ship_instance.build_ship(True, occupied_coordinates)
                    # here we need to check if index of coordinates equals true or false before appending

                print(ship_instance.name)
                
                print(ship_instance.direction)
                
                print(f"Ship coords: {ship_instance.coordinates}")
                
                # Check each tile agains the occupied tile list before placing
                occupied_coordinates.append(ship_instance.coordinates)
                
                ship_log[ship_instance.name] = Board.ship_log(ship_instance.coordinates, ship_instance.symbol_list)
                print(ship_log)
                # fleet.append(ship_instance)
            
                
                # need to append full ship coords to occupied coords
                print(f"occupied: {occupied_coordinates}")

                
            return ship_log


        elif not auto_placement:
            for i in range(5):
                start_position = input(f"Start coordinate for your {ship_obj_type[i].name}?"
                    "Separate to numbers with a comma i.e 4,5 : ").split(",")
                
                start_position = tuple(int(i) for i in start_position)
                direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                duplicate_tile = Ship.duplicate_tile_check(start_position, occupied_coordinates, start_position)
                print (start_position)
                
                
                if i == 0:
                    ship_instance = ship_obj_type[i]((start_position), direction, (start_position))
                    ship_instance.build_ship(False, occupied_coordinates)
                    # not_original = True

                elif not duplicate_tile:
                    ship_instance = ship_obj_type[i](start_position, direction, (start_position))
                    ship_instance.build_ship(False, occupied_coordinates)
                    # not_original = True

                else:
                    not_original = True
                    while not_original == True:
                        start_position = input(f"Start coordinate for your {ship_obj_type[i].name}? "
                            "Separate to numbers with a comma i.e 4,5 : ").split(",")      
                        start_position = tuple(int(i) for i in start_position)
                        direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                        not_original = Ship.duplicate_tile_check(start_position, occupied_coordinates, start_position)
                        ship_instance = ship_obj_type[i](start_position, direction, [], (start_position))
                        ship_instance.build_ship(False, occupied_coordinates)

                print(ship_instance.name)
                
                print(ship_instance.direction)
                
                print(f"Ship coords: {ship_instance.coordinates}")
                
                # Check each tile agains the occupied tile list before placing
                occupied_coordinates.append(ship_instance.coordinates)

                ship_log[ship_instance.name] = Board.ship_log(ship_instance.coordinates, ship_instance.symbol_list)
                print(ship_log)
                # fleet.append(ship_instance)
            
                
                # need to append full ship coords to occupied coords
                print(f"occupied: {occupied_coordinates}")
                             
                # fleet.append(ship_instance)
            return ship_log    

    @staticmethod
    def ship_log(coords, symbol):

        inner_log = dict(zip(coords, symbol))
        return inner_log
            


     

class Ship:
    """
    Creates the ship class for later sub class of ships.
    """
    def __init__(self, start_coordinate, direction, coordinates):
        self.start_coordinate = start_coordinate
        self.direction = direction
        self.damaged_tiles = [False] * self.length
        self.coordinates = coordinates


    def build_ship(self, auto_placement, *occupied_tiles):
        placement_process = True
        
        while placement_process:
            
            temp_ship = []
            temp_ship.append(self.start_coordinate)

            if self.direction == "r":
                for i in range(1, self.length):

                    next_tile = (self.start_coordinate[0] + i, self.start_coordinate[1])
                    duplicate_tile = self.duplicate_tile_check(occupied_tiles, self.start_coordinate)
                    if self.start_coordinate[0] + self.length > 9:
                        if auto_placement:
                            self.start_coordinate = (random.randint(0, 9), random.randint(0, 9))
                            self.direction = random.choice(["r", "d"]) 
                            break
                        elif not auto_placement:
                            print("Your ship does not fit here")
                            self.start_coordinate = input(f"Pick a new start coordinate for your {self.name}? /n"
                                "Separate two numbers with a comma i.e 4,5 : ").split(",")
                            self.start_coordinate = tuple(int(i) for i in self.start_coordinate) 
                            self.direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                            break    
                    
                    elif not duplicate_tile:
                        temp_ship.append(next_tile)
                        if len(temp_ship) == self.length:
                            self.coordinates = temp_ship
                            placement_process = False
                            return self.coordinates 
                        
                    else:
                        if auto_placement:
                            self.start_coordinate = (random.randint(0, 9), random.randint(0, 9))
                            self.direction = random.choice(["r", "d"]) 
                            break
                        elif not auto_placement:
                            print("Your ship does not fit here")
                            self.start_coordinate = input(f"Pick a new start coordinate for your {self.name}? /n"
                                "Separate two numbers with a comma i.e 4,5 : ").split(",")
                            self.start_coordinate = tuple(int(i) for i in self.start_coordinate) 
                            self.direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                            break      
                
            elif self.direction == "d":
                for i in range(1, self.length):
                    next_tile = (self.start_coordinate[0], self.start_coordinate[1] + i)
                    duplicate_tile = self.duplicate_tile_check(occupied_tiles, self.start_coordinate)
                    if self.start_coordinate[1] + self.length > 9:
                        if auto_placement:
                            self.start_coordinate = (random.randint(0, 9), random.randint(0, 9))
                            self.direction = random.choice(["r", "d"]) 
                            break 
                        elif not auto_placement:
                            print("Your ship does not fit here")
                            self.start_coordinate = input(f"Pick a new start coordinate for your {self.name}? /n"
                                "Separate two numbers with a comma i.e 4,5 : ").split(",")
                            self.start_coordinate = tuple(int(i) for i in self.start_coordinate) 
                            self.direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                            break   
                    
                    elif not duplicate_tile:
                        temp_ship.append(next_tile)
                        if len(temp_ship) == self.length:
                            self.coordinates = temp_ship
                            placement_process = False
                            return self.coordinates

                            
                    else:
                        if auto_placement:
                            self.start_coordinate = (random.randint(0, 9), random.randint(0, 9))
                            self.direction = random.choice(["r", "d"]) 
                            break  
                        elif not auto_placement:
                            print("Your ship does not fit here")
                            self.start_coordinate = input(f"Pick a new start coordinate for your {self.name}? /n"
                                "Separate two numbers with a comma i.e 4,5 : ").split(",")
                            self.start_coordinate = tuple(int(i) for i in self.start_coordinate)
                            self.direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                            break               
        
        return self.coordinates

    #use this above to check the list of lists (occupied tiles)
    
    def duplicate_tile_check(start_coordinate, occupied_tiles, next_tile):
        for list in occupied_tiles:
            for coord in list:
                if  next_tile in list:
                    print("Already a ship here")
                    return True
                elif start_coordinate in list:
                    print("Already a ship here")
                    return True


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
player_name = input("What is your name? ")
user = Player(player_name)
print (user.board.fleet[1].__dict__)
# print(user.board.ship_log())
# for i in range(len(user.board.fleet)):
#     print(user.board.ship_log(user.board.fleet[i]))
# Player("computer")

