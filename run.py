import random
import os


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

    @staticmethod
    def quick_start_check():
        """"
        Asks human player if they wish to set the ships up themselves
        or use the quick start feature.
        """
        invalid_input = True
        while invalid_input:
            setup_type = input(
                'Type "(Q)uick" to place your ships randomly,'
                ' or "(M)anual" to place your ships yourself\n').lower()
            if setup_type == "quick" or setup_type == "q":
                invalid_input = False
                return True
            elif setup_type == "manual" or setup_type == "m":
                invalid_input = False
                return False
            else:
                print(
                    'Not valid input please only type "Q" , M, "Quick",'
                    'or "Manual (Casing does not matter): \n')

    def take_guess(self, opponent_guess_checker):
        """
        Sets the guess coordinates by input or random
        returns only original guesses
        """
        valid_guess = False
        while not valid_guess:
            if self.name == "Computer":
                while valid_guess is False:
                    guess_coordinate = (
                        random.randint(
                            0, 9), random.randint(
                            0, 9))
                    previously_guessed = guess_coordinate in self.guesses
                    if previously_guessed:
                        break

                    self.guesses.append(guess_coordinate)
                    valid_guess = True
            else:
                guess_coordinate = input(
                    '"Sir! To which coordinate should we unload the chamber?":'
                    ' eg 0,4 \n').split(",")

                guess_coordinate = (tuple(int(i) for i in guess_coordinate))
                print(guess_coordinate)
                previously_guessed = guess_coordinate in self.guesses

                # Somewhere in here I need to account for invalid input types
                while previously_guessed:
                    if guess_coordinate[0] > 9 or guess_coordinate[1] > 9:
                        print(
                            "But capt'n thats out of bounds, respectively I"
                            " ask you again...")
                        break
                    elif previously_guessed:
                        print(
                            "Sir? has the war driven you crazy? We've already"
                            " fired there,so with all due respect I repeat...")
                        break
                if not previously_guessed:
                    print(
                        "Aye, Aye Capt'n! Fire in the hole boys aim"
                        f" for sector {guess_coordinate}")
                    self.guesses.append(guess_coordinate)
                    valid_guess = True
        opponent_guess_checker(self, guess_coordinate)


class Board:
    """"
    Builds the boards where ships will be placed
    """
    board_size = 10
    number_of_ships = 5

    def __init__(self, owner, auto=True):
        self.owner = owner
        self.auto = auto
        self.guess_board = self.build_guess_board()
        self.board = self.build_board()
        self.fleet = self.build_fleet()
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
        return self.board

    def build_guess_board(self):
        """"
        Builds a the board for the user to track their guess results
        """
        self.guess_board = []
        for row in range(self.board_size):
            self.guess_board.append([])
            for _ in range(self.board_size):
                self.guess_board[row].append("~")
        return self.guess_board

    def user_display(self):
        """
        Prints out the user view, their placement board
        and their guess tally board
        """
        print("    Map of your Fleet:             Enemy hit tracker:")
        print("    0 1 2 3 4 5 6 7 8 9            0 1 2 3 4 5 6 7 8 9")
        print("   +-+-+-+-+-+-+-+-+-+-           +-+-+-+-+-+-+-+-+-+-")
        for index, row in enumerate(zip(self.board, self.guess_board)):
            print(
                # print row numbers for 1st board
                f'{str(index) + " |":2s}',
                # print current row for 1st board, join as string and space out
                # 3 spaces with :3s
                ''.join(f'{str(x):2s}' for x in row[0]),
                # separate the two boards
                ' ' * 5,
                # print row numbers for 2nd board
                f'{str(index)+" |" :2s}',
                # print current row for 2nd board, join as string and space out
                # 3 spaces with :3s
                ''.join(f'{str(x):2s}' for x in row[1]),
            )
        print("\n")

    def build_fleet(self):
        """
        Builds a fleet of ships.
        """
        fleet = []
        occupied_coordinates = []
        ship_obj_type = [
            AircraftCarrier,
            Battleship,
            Cruiser,
            Submarine,
            Destroyer]

        for i in range(self.number_of_ships):

            if self.auto:
                random_start = (random.randint(0, 9), random.randint(0, 9))
                random_direction = random.choice(["r", "d"])
                ship_instance = ship_obj_type[i](
                    random_start, random_direction, (random_start))

            else:
                self.clear_boards()
                start_position = input(
                    f"Start coordinate for your {ship_obj_type[i].name}?"
                    "Separate to numbers with a comma i.e 4,5 : \n").split(",")

                start_position = tuple(int(i) for i in start_position)
                direction = input(
                    'From the bow in which direction is stern pointing,'
                    '"(R)ight" or "(D)own": \n').lower()
                ship_instance = ship_obj_type[i](
                    (start_position), direction, (start_position))

            self.build_ship(self.auto, ship_instance, occupied_coordinates)
            occupied_coordinates.append(ship_instance.coordinates)

            self.initial_placement(ship_instance, self.auto)

            fleet.append(ship_instance)
        if self.auto:
            if self.owner != "Computer":
                self.user_display()
        return fleet

    def build_ship(self, auto_placement, ship, occupied_tiles):
        """
        Builds the ship in the chosen direction and advises user if
        the intended location is already occupied.
        if required asks for/generates randomly a new start coordinate.
        """
        placement_process = True

        while placement_process:

            temp_ship = []
            temp_ship.append(ship.start_coordinate)

            for i in range(1, ship.length):

                if ship.direction == "d" or ship.direction == "down":
                    next_tile = (
                        ship.start_coordinate[0] + i,
                        ship.start_coordinate[1])
                    index_to_increment = 0

                elif ship.direction == "r" or ship.direction == "right":
                    next_tile = (
                        ship.start_coordinate[0],
                        ship.start_coordinate[1] + i)
                    index_to_increment = 1
                duplicate_tile = self.duplicate_tile_check(
                    ship, occupied_tiles, next_tile)

                if ship.start_coordinate[index_to_increment] + \
                        (ship.length - 1) > 9:

                    if auto_placement:
                        ship.start_coordinate = (
                            random.randint(
                                0, 9), random.randint(
                                0, 9))
                        ship.direction = random.choice(["r", "d"])
                        break
                    else:
                        print("Out of bounds")
                        ship.start_coordinate = input(
                            "Pick a new start coordinate for your "
                            f"{ship.name}? \n Separate two numbers with a comma i.e 4,5: \n").split(",")
                        ship.start_coordinate = tuple(
                            int(i) for i in ship.start_coordinate)
                        ship.direction = input(
                            'From the bow in which direction is stern pointing,'
                            ' "(R)ight" or "(D)own": \n').lower()
                        break

                elif not duplicate_tile:
                    temp_ship.append(next_tile)
                    if len(temp_ship) == ship.length:
                        ship.coordinates = temp_ship
                        placement_process = False
                        return ship.coordinates
                # look to condense
                else:
                    if auto_placement:
                        ship.start_coordinate = (
                            random.randint(
                                0, 9), random.randint(
                                0, 9))
                        ship.direction = random.choice(["r", "d"])
                        break
                    elif not auto_placement:
                        print("There is already another ship here...")
                        ship.start_coordinate = input(
                            "Pick a new start coordinate for your "
                            f"{ship.name}?\nSeparate two numbers with a comma i.e 4,5: \n").split(",")
                        ship.start_coordinate = tuple(
                            int(i) for i in ship.start_coordinate)
                        ship.direction = input(
                            "From the bow in which direction is stern pointing?"
                            "(r)ight or (d)own: \n")
                        break

        return ship.coordinates

    @staticmethod
    def duplicate_tile_check(ship, occupied_tiles, next_tile):
        """
        Checks if a tile is occupied
        before allowing a ship to be placed across it.
        """
        for list in occupied_tiles:
            for _ in list:
                if next_tile in list:
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
            ship_log.update(
                dict(zip(self.fleet[i].coordinates, self.fleet[i].symbol_list)))
        return ship_log

    def initial_placement(self, ship, auto_placement=False):
        """
        If auto placement = False (Manually placed ships)
        Prints a board showing each ship in the chose location
        """
        if self.owner != "computer":
            for i in range(ship.length):
                self.board[ship.coordinates[i][0]
                           ][ship.coordinates[i][1]] = ship.symbol_list[i]
            if not auto_placement:
                if self.owner != "Computer":
                    self.clear_boards()

    def guess_checker(self, opponent, guess):
        """
        Takes guess and check against fleet dictionary.
        """
        result = self.map_of_fleet
        result = result.get(guess)
        ship = None
        if result:
            for i in range(5):
                ship = self.fleet[i]
                if result is self.fleet[i].symbol_list[0]:
                    break
        self.update_board(guess, result, opponent, ship)

    def update_ship_damage(self, ship):
        """"
        Checks through the ships damage tiles and updates as required
        """
        ship.damaged_tiles.append(True)
        if len(ship.damaged_tiles) == ship.length:
            ship.is_sunk = True
            print(f" sunk {self.owner}'s {ship.name}")
            self.ships_remaining()

    def update_board(self, guess, result, opponent, ship):
        """"
        Updates Board with latest hit or miss.
        """
        if self.owner == "Computer":
            if result is None:
                opponent.board.guess_board[guess[0]][guess[1]] = "X"
                opponent.board.clear_boards()
                print("Thats a miss capt'n.... nothing but water.\n")

            else:
                opponent.board.guess_board[guess[0]][guess[1]] = "%"
                opponent.board.clear_boards()
                print(f"Direct hit was made on {self.owner}'s {ship.name}\n")
                self.update_ship_damage(ship)

        else:
            if result is None:
                self.board[guess[0]][guess[1]] = "X"
                self.clear_boards()
                print("Sir permission to breathe? they missed us!.\n")
            else:
                self.board[guess[0]][guess[1]] = "%"
                self.clear_boards()
                print(
                    f"They hit our {ship} sir! We are are taking on water!\n")
                self.update_ship_damage(ship)

            # if self.owner != "Computer":
        #     self.user_display()

    def ships_remaining(self):
        """
        Reduces number of ships by one and ends game if all ships sunk.
        """
        game_over = False
        self.number_of_ships -= 1
        print(f"{self.owner} has {self.number_of_ships} remaining")
        if self.number_of_ships == 0:
            return True
        else:
            return game_over

    # Taken from https://www.delftstack.com/howto/python/python-clear-console/
    def clear_boards(self,):
        """"
        Clears the console
        """
        command = 'clear'
        if os.name in (
                'nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
        self.user_display()


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
    name = "Aircraft_carrier"
    length = 5
    symbol_list = ["A"] * length


class Battleship(Ship):
    """
    Creates an instance of the Battleship class.
    """
    name = "Battleship"
    length = 4
    symbol_list = ["B"] * length


class Cruiser(Ship):
    """
    Creates an instance of the Cruiser class.
    """
    name = "Cruiser"
    length = 3
    symbol_list = ["C"] * length


class Submarine(Ship):
    """
    Creates an instance of the Submarine class.
    """
    name = "Submarine"
    length = 3
    symbol_list = ["S"] * length


class Destroyer(Ship):
    """
    Creates an instance of the Destroyer class.
    """
    name = "Destroyer"
    length = 2
    symbol_list = ["D"] * length


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
        Computer fires at the player
        and the players board is updated accordingly.
        """

# Construction of the game


def is_fleet_sunk():
    if user.board.number_of_ships == 0 or computer.board.number_of_ships == 0:
        return False
    else:
        return True


user = Player(input("What is your name? \n"))
computer = Player("Computer")

play_game = True
while play_game:
    play_game = is_fleet_sunk()
    user.take_guess(computer.board.guess_checker)
    play_game = is_fleet_sunk()
    if play_game:
        input("press enter for computer turn")
        # Board.clear_boards()
        computer.take_guess(user.board.guess_checker)
        # The below is for testing only
        # computer.board.user_display()
    else:
        break


print("game_over")
