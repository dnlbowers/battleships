# To check
# How to print the boards side by side -
#     if I could make the print board a return value would ZIP work ?
#How to sort the error of damaged tile * self length in Ship
#When can I use try and except

#to do
# If computer create a blank board.
# create a firing round
    # take guess as input/ generates randon guess for the computer - done
    # checks coordinate - where to place....?
        # if in dictionary replaces the tile with the value "@"
        # If not in dictionary mark with "X"
# create sink function
#catch all input errors


#notes


# Write your code to expect a terminal of 80 characters wide and 24 rows high


import random


class Player:
    """
    Creates a player object
    """
    def __init__(self, name):
        self.name = name
        if self.name == "Computer":
            self.board = Board(name)
        else:
            auto = self.quick_start_check()
            self.board = Board(name, auto)
        self.guesses = []
        # self.guess_index = 0


    @staticmethod #static method maybe
    def quick_start_check():
        """"
        Asks human player if they wish to set the ships up themselves
        or use the quick start feature.
        """

        # add checks later includeding  one for m - needs to return True or False
        invalid_input= True
        while invalid_input:
            setup_type = input('Type "(Q)uick" to place your ships randomly,'
                ' or "(M)anual" to place your ships yourself\n').lower()
            if setup_type == "quick" or setup_type == "q":
                invalid_input = False
                return True
            elif setup_type == "manual" or setup_type == "m":
                invalid_input = False
                return False
            else:
                print('Not valid input please only type "Quick" or "Manual: \n')


    def take_guess(self, opponent):
        """
        Sets the guess coordinates by input or random and returns only original guesses
        """

        valid_guess = False
        while valid_guess is False:
            if self.name == "Computer":
                while valid_guess is False:
                    guess_coordinate = (random.randint(0, 9), random.randint(0, 9))
                    previously_guessed = guess_coordinate in self.guesses
                    if previously_guessed:
                        break
                    else:
                        self.guesses.append(guess_coordinate)
                        valid_guess = True
            else:
                guess_coordinate = input('"Sir! To which coordinate should we unload the chamber?":'
                  ' eg 0,4 \n').split(",")
                guess_coordinate = (tuple(int(i) for i in guess_coordinate))

            previously_guessed = guess_coordinate in self.guesses

            #Somewhere in here I need to account for invalid input types
            if guess_coordinate[0] > 9 or guess_coordinate[1] > 9:
                print("But capt'n thats out of bounds, respectively I ask you again...")
            elif previously_guessed:
                print("Sir? has the war driven you crazy? We've already fired there,"
                    "so with all due respect I repeat....")
            else:
                print(f"Aye, Aye Capt'n! Fire in the hole boys aim for sector {guess_coordinate}")
                self.guesses.append(guess_coordinate)
                valid_guess = True
        opponent.guess_checker(guess_coordinate)


class Board:
    """"Build the boards"""
    board_size = 10
    number_of_ships = 5

    def __init__(self, owner, auto = True):
        self.owner = owner
        self.auto = auto
        self.guess_board = self.build_guess_board()
        self.board = self.build_board()
        self.fleet =  self.build_fleet()
        self.map_of_fleet = self.fleet_coords_map()


    def build_board(self):
        """
        Builds a blank board with coordinates as a key.
        """
        self.board = []

        for row in range(self.board_size):
            self.board.append([])
            for _ in range(self.board_size):
                self.board[row].append("~")
        # for index, row in enumerate(zip(player_board, player_guess_board))
        return self.board

    def build_guess_board(self):
        """"
        Builds a the board for the user to track their guess results
        """
        self.guess_board =[]
        for row in range(self.board_size):
            self.guess_board.append([])
            for _ in range(self.board_size):
                self.guess_board[row].append("~")
        return self.guess_board

    def print_board(self):
        """
        Prints the board.
        """
        # if self.owner != "computer":
        #     How can I make this a return value and use it in the below zip format string?
        if self.owner == "blank":
            self.owner = "Computer"
        print(f"     {self.owner}'s board:")
        print("    0 1 2 3 4 5 6 7 8 9")
        print("   +-+-+-+-+-+-+-+-+-+-")
        row_num = 0
        for row in self.board:
            print(row_num, "|", " ".join(row))
            row_num += 1
        print("\n")


    def build_fleet(self):
        """
        Builds a fleet of ships.
        """
        fleet = []
        occupied_coordinates = []
        ship_obj_type =  [AircraftCarrier, Battleship, Cruiser, Submarine, Destroyer]

        for i in range(self.number_of_ships):

            if self.auto:
                random_start = (random.randint(0, 9), random.randint(0, 9))
                random_direction = random.choice(["r", "d"])
                ship_instance = ship_obj_type[i](random_start, random_direction, (random_start))

            else:
                start_position = input(f"Start coordinate for your {ship_obj_type[i].name}?"
                    "Separate to numbers with a comma i.e 4,5 : ").split(",")

                start_position = tuple(int(i) for i in start_position)
                direction = input('From the bow in which direction is stern pointing,'
                    '"(R)ight" or "(D)own": ').lower()
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

                if ship.direction == "d" or ship.direction == "down":
                    next_tile = (ship.start_coordinate[0] + i, ship.start_coordinate[1])
                    index_to_increment = 0

                elif ship.direction == "r" or ship.direction == "right":
                    next_tile = (ship.start_coordinate[0], ship.start_coordinate[1] + i)
                    index_to_increment = 1
                duplicate_tile = self.duplicate_tile_check(ship, occupied_tiles, next_tile)

                if ship.start_coordinate[index_to_increment] + (ship.length - 1) > 9:

                    if auto_placement:
                        ship.start_coordinate = (random.randint(0, 9), random.randint(0, 9))
                        ship.direction = random.choice(["r", "d"])
                        break
                    else:
                        print("Out of bounds")
                        ship.start_coordinate = input("Pick a new start coordinate for your "
                            f"{ship.name}?/nSeparate two numbers with a comma i.e 4,5: ").split(",")
                        ship.start_coordinate = tuple(int(i) for i in ship.start_coordinate)
                        ship.direction = input('From the bow in which direction is stern pointing,'
                            ' "(R)ight" or "(D)own": ').lower()
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
                        ship.start_coordinate = input("Pick a new start coordinate for your "
                            f"{ship.name}?\nSeparate two numbers with a comma i.e 4,5: ").split(",")
                        ship.start_coordinate = tuple(int(i) for i in ship.start_coordinate)
                        ship.direction = input("From the bow in which direction is stern pointing?"
                            "(r)ight or (d)own: ")
                        break

        return ship.coordinates


    @staticmethod
    def duplicate_tile_check(ship, occupied_tiles, next_tile):
        """
        Checks if a tile is occupied before allowing a ship to be placed across it.
        """
        for list in occupied_tiles:
            for _ in list:
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
        for i in range(self.number_of_ships):
            ship_log.update(dict(zip(self.fleet[i].coordinates, self.fleet[i].symbol_list)))
        return ship_log


    def initial_placement(self, ship, auto_placement = False):
        """
        If auto placement = False (Manually placed ships)
        Prints a board showing each ship in the chose location
        """
        if self.owner != "computer":
            for i in range(ship.length):
                self.board[ship.coordinates[i][0]][ship.coordinates[i][1]] = ship.symbol_list[i]
            if not auto_placement:
                self.print_board()


    def guess_checker(self, guess):
        """
        Takes guess and check against fleet dictionary.
        """
        print("Guess_checker")
        print(f"self = {self.owner}")
        
        result = self.map_of_fleet
        print(f"{result}")
        result = result.get(guess)
        if result is None:
            print("Thats a miss capt'n.... nothing but water.")
        else:
            for i in range(5):
                if result is self.fleet[i].symbol_list[0]:
                    print(f"Direct hit was made on {self.owner}'s "
                        f"{self.fleet[i].name}")
                    self.update_ship_damage(self.fleet[i])
        self.update_board(guess, result)

    def update_ship_damage(self, ship):
        """"
        Checks through the ships damage tiles and updates as required
        """
        print("Update_ship")
        print(f"opponent is {self.owner}")

        ship.damaged_tiles.append(True)
        print(f"{ship.damaged_tiles} on {ship.name}")
        if len(ship.damaged_tiles) == ship.length:
            ship.is_sunk = True
            print(f" sunk {self.owner}'s {ship.name}")
            self.ships_remaining()


    def update_board(self, guess, result):
        """"
        Updates Board with latest hit or miss.
        """
        print("update board")
        print(f"{guess}")
        print(f"{result} marked for {self.owner}")
        if result is None:
            self.board[guess[0]][guess[1]] = "X"
        else:
            self.board[guess[0]][guess[1]] = "%"
        self.print_board()


    def ships_remaining(self):
        """
        Reduces number of ships by one and ends game if all ships sunk.
        """
        print("Ships_remaining")

        print(f"self = {self.owner}")
        # print(f"opponent = {opponent.owner}")
        game_over = False
        self.number_of_ships -= 1
        print(f"ships left {self.number_of_ships}")
        print(f"self{self.owner}")
        # print(f"opponenet{opponent.owner}")
        if self.number_of_ships <= 0:
            game_over = True
            return game_over
        return game_over


class Ship:
    """
    Creates the ship class for later sub class of ships.
    """
    def __init__(self, start_coordinate, direction, coordinates):
        self.start_coordinate = start_coordinate
        self.direction = direction
        self.damaged_tiles = []
        self.coordinates = coordinates
        self.is_sunk = False



class AircraftCarrier(Ship):
    """
    Creates an instance of the Aircraft_carrier class.
    """
    name =  "Aircraft_carrier"
    length = 5
    symbol_list = ["A"] * length
    #it told me these were useless seems to work without
    # def __init__(self, start_coordinate, direction, coordinates):
    #     super().__init__(start_coordinate, direction, coordinates)


class Battleship(Ship):
    """
    Creates an instance of the Battleship class.
    """
    name = "Battleship"
    length = 4
    symbol_list = ["B"] * length

    # def __init__(self, start_coordinate, direction, coordinates):
    #     super().__init__(start_coordinate, direction, coordinates)


class Cruiser(Ship):
    """
    Creates an instance of the Cruiser class.
    """
    name = "Cruiser"
    length = 3
    symbol_list = ["C"] * length

    # def __init__(self, start_coordinate, direction, coordinates):
    #     super().__init__(start_coordinate, direction, coordinates)


class Submarine(Ship):
    """
    Creates an instance of the Submarine class.
    """
    name = "Submarine"
    length = 3
    symbol_list = ["S"] * length

    # def __init__(self, start_coordinate, direction, coordinates):
    #     super().__init__(start_coordinate, direction, coordinates)


class Destroyer(Ship):
    """
    Creates an instance of the Destroyer class.
    """
    name = "Destroyer"
    length = 2
    symbol_list = ["D"] * length

    # def __init__(self, name, length, symbol_list, start_coordinate, direction, coordinates):
    #     super().__init__(start_coordinate, direction, coordinates)
    #     self.name = name
    #     self.length = length
    #     self.symbol_list = symbol_list

class Game:

    """
    Creates objects and plays the game
    """


    def welcome(self):
        """"
        Displays title art, offers user to view the game rules and asks if
        they wish to begin the game
        """

    def user_turn(self):
        """"
        Player fires at the computer and players visual for the opponents board
        updates with a result
        """


    def opponent_turn(self):
        """"
        Computer fires at the player and the players board is updated accordingly.
        """

#Construction of the game
# #This now creates a player, board, and feet.
# player_name = input("What is your name? ")
user = Player(input("What is your name? "))
computer = Player("Computer")
# print(user.board.__dict__)
# print(computer.board.__dict__)
game_over = False
while not game_over:

    game_over = user.take_guess(computer.board)
    game_over = computer.take_guess(user.board)
    
print("game_over")

#doesn't work
# Game(Player(input("What is your name? ")), Player("computer"), Player("computer")).welcome()

# Play_game(user, computer, "B")
# user_guess_board = Player("CPU")


# print(user.board.fleet_coords_map)
# cpu = Player("computer")
# print(cpu.board.fleet_coords_map)
# print(cpu.board.__dict__)

#How do I apply this propely? reference print boards side by side https://www.codegrepper.com/code-examples/python/how+to+print+two+lists+side+by+side+in+python
# self.board = "\n".join("{} {}".format(x, y) for x, y in zip(player_board, player_guess_board))


# # it works but I cannot access the print board to tidy it up
# print(res)

# print(user.board.__dict__)
# print(computer.__dict__)


# print(user.board.ship_log())
# for i in range(len(user.board.fleet)):
#     print(user.board.ship_log(user.board.fleet[i]))
# Player("computer")
