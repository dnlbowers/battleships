#INFINATE LOOP IN BUILD SHIP()

# To check:


#to do
#Make a dictionary for occupied tiles which has the coord as the key and the fleet[i].symbol as the value (i.e. S or C) 
# why doesn't build fleet detect same coord used twice? likely in the build ship function - *args?
# Consider making the occupied tiles a dictionary with the coord as the key and the 
# ship_instance_symbol as the value. This way we maybe skip ship coords and 
# just check the occupied tiles dictionary. Do we still need fleet?

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
        self.fleet =  self.build_fleet(auto) 

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

        
        if auto_placement:
            for i in range(5):
                print("------------")
                first_occurrence = False
                
                random_start = (random.randint(0, 9), random.randint(0, 9))
                random_direction = random.choice(["r", "d"])

                if i == 0:
                    ship_instance = ship_obj_type[i](random_start, random_direction, [], (random_start))
                    ship_instance.build_ship(True, occupied_coordinates)
                    # first_occurrence = True

                elif random_start not in occupied_coordinates:
                    ship_instance = ship_obj_type[i](random_start, random_direction, [], (random_start))
                    ship_instance.build_ship(True, occupied_coordinates)
                    # first_occurrence = True

                else:
                    while first_occurrence == False:
                        print(f"Duplicate {i}{random_start}")
                        random_start = (random.randint(0, 9), random.randint(0, 9))
                        print(f"New {i}{random_start}")
                        print(f"first instance check : {first_occurrence}")
                        first_occurrence = random_start not in occupied_coordinates
                        print(f"first instance : {first_occurrence}")
                        ship_instance = ship_obj_type[i](random_start, random_direction, [], (random_start))
                        ship_instance.build_ship(True, occupied_coordinates)
                    # here we need to check if index of coordinates equals true or false before appending

                print(ship_instance.name)
                
                print(ship_instance.direction)
                
                print(f"Ship coords: {ship_instance.coordinates}")
                
                # Check each tile agains the occupied tile list before placing
                occupied_coordinates.append(ship_instance.coordinates)

                
                fleet.append(ship_instance)
            
                
                # need to append full ship coords to occupied coords
                print(f"occupied: {occupied_coordinates}")

                
            return fleet


        elif not auto_placement:
            for i in range(5):
                start_position = input(f"Start coordinate for your {ship_obj_type[i].name}?"
                    "Separate to numbers with a comma i.e 4,5 : ").split(",")
                
                start_position = tuple(int(i) for i in start_position)

                print (start_position)
                direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                
                if i == 0:
                    ship_instance = ship_obj_type[i]((start_position), direction, [], (start_position))
                    ship_instance.build_ship(False, occupied_coordinates)
                    # first_occurrence = True

                elif start_position not in occupied_coordinates:
                    print(f"{start_position not in occupied_coordinates} not in")
                    ship_instance = ship_obj_type[i](start_position, direction, [], (start_position))
                    ship_instance.build_ship(False, occupied_coordinates)
                    # first_occurrence = True

                else:
                    
                    while first_occurrence == False:
                        print(f"Duplicate {i}{start_position}")
                        start_position = input(f"Start coordinate for your {ship_obj_type[i].name}?"
                            "Separate to numbers with a comma i.e 4,5 : ").split(",")
                        
                        start_position = tuple(int(i) for i in start_position)
                        direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                        print(f"New {i}{direction}")
                        print(f"first instance check : {first_occurrence}")
                        first_occurrence = start_position not in occupied_coordinates
                        print(f"first instance : {first_occurrence}")
                        ship_instance = ship_obj_type[i](start_position, direction, [], (start_position))
                        ship_instance.build_ship(False, occupied_coordinates)

                print(ship_instance.name)
                
                print(ship_instance.direction)
                
                print(f"Ship coords: {ship_instance.coordinates}")
                
                # Check each tile agains the occupied tile list before placing
                occupied_coordinates.append(ship_instance.coordinates)

                
                fleet.append(ship_instance)
            
                
                # need to append full ship coords to occupied coords
                print(f"occupied: {occupied_coordinates}")
                             
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


    def build_ship(self, auto_placement = False, *occupied_tiles):
        placement_process = True
        
        while placement_process:
            print(f"within function occupied: {occupied_tiles}")
            temp_ship = []
            temp_ship.append(self.start_coordinate)

            if self.direction == "r":
                for i in range(1, self.length):
                    next_tile = (self.start_coordinate[0] + i, self.start_coordinate[1])
                    
                    if self.start_coordinate[0] + self.length > 9:
                        if auto_placement:
                            self.start_coordinate = (random.randint(0, 9), random.randint(0, 9))
                            self.direction = random.choice(["r", "d"]) 
                            break
                        elif not auto_placement:
                            print("Your ship does not fit here")
                            self.start_coordinate = input(f"Pick a new start coordinate for your {self.name}?/n"
                                "Separate to numbers with a comma i.e 4,5 : ").split(",")
                            self.start_coordinate = tuple(int(i) for i in self.start_coordinate) 
                            self.direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                            break    
                    
                    elif next_tile not in occupied_tiles:
                        print(f"{next_tile} appended")
                        temp_ship.append(next_tile)
                        if len(temp_ship) == self.length:
                            print(f"{temp_ship} length == to the ship length")
                            self.coordinates = temp_ship
                            placement_process = False
                            return self.coordinates 
                        
                    else:
                        if auto_placement:
                            self.start_coordinate = (random.randint(0, 9), random.randint(0, 9))
                            self.direction = random.choice(["r", "d"]) 
                            break
                        elif not auto_placement:
                            print("Your ship does fit here")
                            self.start_coordinate = input(f"Pick a new start coordinate for your {self.name}?/n"
                                "Separate to numbers with a comma i.e 4,5 : ").split(",")
                            self.start_coordinate = tuple(int(i) for i in self.start_coordinate) 
                            self.direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                            break      
                
            elif self.direction == "d":
                for i in range(1, self.length):
                    next_tile = (self.start_coordinate[0], self.start_coordinate[1] + i)

                    if self.start_coordinate[1] + self.length > 9:
                        if auto_placement:
                            self.start_coordinate = (random.randint(0, 9), random.randint(0, 9))
                            self.direction = random.choice(["r", "d"]) 
                            break 
                        elif not auto_placement:
                            print("Your ship does fit here")
                            self.start_coordinate = input(f"Pick a new start coordinate for your {self.name}?/n"
                                "Separate to numbers with a comma i.e 4,5 : ").split(",")
                            self.start_coordinate = tuple(int(i) for i in self.start_coordinate) 
                            self.direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                            break   
                    
                    elif next_tile not in occupied_tiles:
                        temp_ship.append(next_tile)
                        print(f"{next_tile} appended")
                        if len(temp_ship) == self.length:
                            print(f"{temp_ship} length == to the ship length")
                            self.coordinates = temp_ship
                            placement_process = False
                            return self.coordinates 
                            
                    else:
                        if auto_placement:
                            self.start_coordinate = (random.randint(0, 9), random.randint(0, 9))
                            self.direction = random.choice(["r", "d"]) 
                            break  
                        elif not auto_placement:
                            print("Your ship does fit here")
                            self.start_coordinate = input(f"Pick a new start coordinate for your {self.name}?/n"
                                "Separate to numbers with a comma i.e 4,5 : ").split(",")
                            self.start_coordinate = tuple(int(i) for i in self.start_coordinate)
                            self.direction = input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")
                            break               
        # start is now a list of lists
        print(f"i = {temp_ship} print at end")
        
        return self.coordinates

    #use this above to check the list of lists (occupied tiles)
    @staticmethod
    def original_tile_check(occupied_tiles, next_tile):
        for list in occupied_tiles:
            for coord in list:
                if  next_tile in list:
                    return False

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
# Player("computer")

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