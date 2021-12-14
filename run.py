import random
import os
from getch import pause


class InputMixin():
    """"
    Takes the coordinate input from the user.
    check its against several conditionals to ensure its valid
    returns valid coordinate or asked for new input
    """

    def coord_input_validator(self, input):
        """"
        Tests guess and placement input coordinates and
        checks against several conditions to ensure no errors
        will arise when using the data through the flow of
        the game.
        """
        valid_input = False
        while not valid_input:
            try:

                if len(input) < 2 or len(input) > 3:
                    raise ValueError
                elif len(input) == 2:
                    input = (tuple(int(i) for i in input))
                    return input

                elif len(input) < 4:
                    if "," in input:
                        input = input.split(",")
                        input = (tuple(int(i) for i in input))
                        return input
                    else:
                        input = self.coord_error_msg()
                        continue

            except ValueError:
                input = self.coord_error_msg()

    @staticmethod
    def coord_error_msg():
        """"
        Requests new input and offers guidance on
        what qualifies as a valid input
        """
        new_guess = input("You input is invalid. Please use two "
                          "numbers between 0 and 9 (row then column)\n"
                          "i.e 4,5 or 45: \n").strip(" ")

        return new_guess


class ClearDisplayMixin():
    """
    Contains a static function to be used across multiple classes
    """
    # Taken from https://www.delftstack.com/howto/python/python-clear-console/
    @staticmethod
    def clear_display():
        """"
        Clears the console
        """
        command = 'clear'
        if os.name in (
                'nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)


class Player(InputMixin, ClearDisplayMixin):
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
                'Type "(Q)uick" to place your ships randomly,\n'
                'or "(M)anual" to place your ships '
                'yourself\n').lower().strip(" ")
            if setup_type == "quick" or setup_type == "q":
                invalid_input = False
                return True
            elif setup_type == "manual" or setup_type == "m":
                invalid_input = False
                return False
            else:
                print(
                    'Not valid input please only type "Q" , M, "Quick",'
                    'or "Manual"\n(Letter casing does not matter): \n')

    def take_guess(self):
        """
        Sets the guess coordinates by input or random
        returns only original guesses
        """
        valid_guess = False
        while not valid_guess:
            if self.name == "Computer":
                # while valid_guess is False:
                guess_coordinate = (
                    random.randint(
                        0, 9), random.randint(
                        0, 9))
                previously_guessed = guess_coordinate in self.guesses
                if previously_guessed:
                    continue

                self.guesses.append(guess_coordinate)
                valid_guess = True
            else:
                guess_coordinate = input(
                    '"Sir! To which coordinate should we unload the '
                    'chamber?":\n Enter (row then column) eg 0,4 '
                    'or 04: \n').strip(" ")

                guess_coordinate = self.coord_input_validator(guess_coordinate)
                previously_guessed = guess_coordinate in self.guesses

                if previously_guessed:
                    print(
                        "Sir? has the war driven you crazy?\n"
                        "We've already fired there, "
                        "so with all due respect I repeat...")
                    continue
                else:
                    self.board.user_display()
                    self.guesses.append(guess_coordinate)
                    valid_guess = True

        return guess_coordinate

    def player_turn(self, opponent):
        """"
        Player fires at the computer and players visual for the opponents board
        updates with a result
        """
        print(f"{self.name}'s turn")
        guess = self.take_guess()
        guess_hit_check = opponent.board.guess_checker(guess)
        self.board.update_board(guess, guess_hit_check, opponent)
        if self.name != "Computer":
            self.board.user_display()

        else:
            opponent.board.user_display()


class Board(InputMixin, ClearDisplayMixin):
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
                self.board[row].append("\U000025FD")
        return self.board

    def build_guess_board(self):
        """"
        Builds a the board for the user to track their guess results
        """
        self.guess_board = []
        for row in range(self.board_size):
            self.guess_board.append([])
            for _ in range(self.board_size):
                self.guess_board[row].append("\U000025FD")
        return self.guess_board

    def user_display(self):
        """
        Prints out the user view, their placement board
        and their guess board
        """
        self.clear_display()
        print((" ")*20 + f"These sea charts belong to Captain {self.owner}")
        print("    Map of your Fleet:              "
              "         Guess tracker:")
        print("    0  1  2  3  4  5  6  7  8  9             "
              "0  1  2  3  4  5  6  7  8  9")
        print("  +--+--+--+--+--+--+--+--+--+--           "
              "+--+--+--+--+--+--+--+--+--+--")
        for index, row in enumerate(zip(self.board, self.guess_board)):
            print(
                # Number rows on placement board
                f'{str(index) + " |":3s}',
                # print row by row with 3 spaces between
                ''.join(f'{str(x):3s}' for x in row[0]),
                # separate the two boards by 5 spaces
                ' ' * 5,
                # Number rows on guess board
                f'{str(index)+" |" :3s}',
                # print row by row with 3 spaces between
                ''.join(f'{str(x):3s}' for x in row[1]),
            )
        print("\n")

    def build_fleet(self):
        """
        Initializes one instance of each ship type.
        request starting postion and and intended placement direction
        called method to build the full ship
        returns a list of objects called fleet
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
                self.user_display()
                start_position = input(
                    f"From where would you like your {ship_obj_type[i].name} "
                    f"(which is {ship_obj_type[i].length} tiles long) to "
                    "start?\nPlease enter two numbers (row then column) "
                    "i.e 4,5 or 45: \n").strip(" ")

                start_position = self.coord_input_validator(start_position)
                direction = self.direction_input()
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
                            f"{ship.name}? \n Please enter two numbers "
                            "(row then column) i.e 4,5 or 45: \n").strip(" ")
                        ship.start_coordinate = self.coord_input_validator(
                            ship.start_coordinate)
                        ship.direction = self.direction_input()
                        break

                elif not duplicate_tile:
                    temp_ship.append(next_tile)
                    if len(temp_ship) == ship.length:
                        ship.coordinates = temp_ship
                        placement_process = False
                        return ship.coordinates

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
                            f"{ship.name}? \n Please enter two numbers "
                            "(row then column) i.e 4,5 or 45: \n").strip(" ")
                        ship.start_coordinate = self.coord_input_validator(
                            ship.start_coordinate)
                        ship.direction = self.direction_input()
                        break
        return ship.coordinates

    def direction_input(self):
        invalid_input = True
        while invalid_input:
            setup_type = input(
                "From the bow in which direction is stern "
                "pointing? (r)ight or (d)own: \n").lower().strip(" ")
            if setup_type == "right" or setup_type == "r":
                invalid_input = False
                return "right"
            elif setup_type == "down" or setup_type == "d":
                invalid_input = False
                return "down"
            else:
                print(
                    'Not a valid input please only type "R" , "D", "Right",'
                    'or "Down"\n(Letter casing does not matter):')

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
                dict(zip(self.fleet[i].coordinates,
                     self.fleet[i].symbol_list)))
        return ship_log

    def initial_placement(self, ship, auto_placement=False):
        """
        If auto placement = False (Manually placed ships)
        Prints a board showing each ship in the chosen location
        """
        if self.owner != "Computer":
            for i in range(ship.length):
                self.board[ship.coordinates[i][0]
                           ][ship.coordinates[i][1]] = ship.symbol_list[i]
            if not auto_placement:
                if self.owner != "Computer":
                    self.user_display()

    def guess_checker(self, guess):
        """
        Checks guess against fleet dictionary.
        Calls method to update ship damage
        """
        result = self.map_of_fleet
        result = result.get(guess)
        ship = None
        if result:
            for i in range(5):
                ship = self.fleet[i]
                if result is self.fleet[i].symbol_list[0]:
                    self.update_ship_damage(ship)
                    return True
        else:
            return False

    def update_ship_damage(self, ship):
        """"
        Checks through the ships damage tiles and updates as required
        """
        ship.damaged_tiles.append(True)
        if len(ship.damaged_tiles) == ship.length:
            self.ships_remaining()

    def update_board(self, guess, result, opponent):
        """"
        Updates Board with latest hit or miss.
        """
        if result is False:
            self.guess_board[guess[0]][guess[1]] = "\U0001F30A"
            opponent.board.board[guess[0]][guess[1]] = "\U0001F30A"
            if self.owner != "Computer":
                self.user_display()
            else:
                opponent.board.user_display()
            print(f"SPLASH!!! {self.owner} missed")
            pause()

        else:
            self.guess_board[guess[0]][guess[1]] = "\U0001F4A5"
            opponent.board.board[guess[0]][guess[1]] = "\U0001F4A5"
            if self.owner != "Computer":
                self.user_display()
            else:
                opponent.board.user_display()
            print(f"{self.owner} made a Direct hit!")
            pause()

    def ships_remaining(self):
        """
        Reduces number of ships by one.
        """
        self.number_of_ships -= 1
        return self.number_of_ships

    def is_fleet_sunk(self):
        if self.number_of_ships == 0:
            return False
        else:
            return True


class Ship:
    """
    Creates the ship class for later sub class of ships.
    """

    def __init__(self, start_coordinate, direction, coordinates):
        self.start_coordinate = start_coordinate
        self.direction = direction
        self.damaged_tiles = []
        self.coordinates = coordinates


class AircraftCarrier(Ship):
    """
    Creates an instance of the Aircraft_carrier class.
    """
    name = "Aircraft carrier"
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


class Game(ClearDisplayMixin):
    """
    Creates objects and plays the game
    """

    def welcome_screen(self):
        """"
        Displays title art, offers user to view the game rules and asks if
        they wish to begin the game
        """
        print("""
              ______   _______ __________________ _        _______
             (  ___ \\ (  ___  )\\__   __/\\__   __/( \\      (  ____ \\
             | (   ) )| (   ) |   ) (      ) (   | (      | (    \\/
             | (__/ / | (___) |   | |      | |   | |      | (__
             |  __ (  |  ___  |   | |      | |   | |      |  __)
             | (  \\ \\ | (   ) |   | |      | |   | |      | (
             | )___) )| )   ( |   | |      | |   | (____/\\| (____/\\
             |/ \\___/ |/     \\|   )_(      )_(   (_______/(_______/

                  _______          _________ _______  _______
                 (  ____ \\|\\     /|\\__   __/(  ____ )(  ____ \\
                 | (    \\/| )   ( |   ) (   | (    )|| (    \\/
                 | (_____ | (___) |   | |   | (____)|| (_____
                 (_____  )|  ___  |   | |   |  _____)(_____  )
                       ) || (   ) |   | |   | (            ) |
                 /\\____) || )   ( |___) (___| )      /\\____) |
                 \\_______)|/     \\|\\_______/|/       \\_______)
            """)
        options_menu = True
        while options_menu:
            options = input('              Press the "P" key to play,'
                            ' "S" for the back story\n                      '
                            '        or the "R" rules\n').lower().strip(" ")
            if options == "r":
                options_menu = False
                self.how_to_play()
            elif options == "s":
                self.story()
            elif options == "p":
                options_menu = False
                self.clear_display()
                self.set_players()
            else:
                print('Your input was not valid. Please press "P"'
                      'to play or "R" for the rules.')

    def story(self):
        """"
        prints a back story to set the scene
        """
        self.clear_display()
        print(
            'The scene begins you are in deep waters. Mid-sea battle, the \n'
            'command comes in over the radio that the war is over; '
            'the trouble is \nyou '
            'still have some ammunition left. There are rounds left in the\n'
            'chamber... it would be irresponsible to leave live rounds in the'
            '\nchamber....  In fact, definitely dangerous to do so....\n'
            '\n'
            'To be a good captain and save your own men from accidental\n'
            'onboard detonation, you agree to fire randomly into the sea. The'
            '\ntrouble is the other side\'s fleet captain had the same idea...'
            '\n'
            '\n'
            'With both sides racing to clear all their rounds (and some extra'
            '\nthat "slipped" into the torpedo chamber) the obvious winner is'
            '\nthe last man standing.\n'
            '\n'
            'The war may be over, but this battle has just begun!'
        )
        pause()
        self.clear_display()
        self.welcome_screen()

    def how_to_play(self):
        """
        prints game instructions
        """
        self.clear_display()
        print(
            'Setup Phase:\n'
            '\n'
            'Each players fleet has the following 5 ships, represented with \n'
            'the letter displayed below in square brackets: -\n'
            '\n'
            '[A] Aircraft carrier - 5 tiles in length\n'
            '[B] Battleship - 4 tiles in length\n'
            '[C] Cruiser - 3 tiles in length\n'
            '[S] Submarine - 3 tiles in length\n'
            '[D] Destroyer - 2 tiles in length\n'
            '\n'
            'Place your fate in the hands of the sea god Neptune. \n'
            'Press "q" or type "quick" to let the currents randomly\n'
            'position your ships before you anchor and fire.\n'
            '\n'
            'Or\n'
            '\n'
            'Before opening fire, choose to spite the sea god and\n'
            'place your ships by pressing "m" or typing "manual".\n'
            '\n'
            'Neptune\'s hand will always guide the computerized fleet\n'
            'only to reveal their location with the flames as you hit one.\n'
        )
        pause()
        self.clear_display()
        print(
            'Firing Round:\n'
            '\n'
            'Once in position, it\'s time to let a rip!\n'
            '\n'
            'Since the radar equipment was broken "accidentally" in the\n'
            'previous battle, you are firing blind and cannot see the other\n'
            "side's ships. Choose your coordinates on the map (row , column)\n"
            'and remember to yell "FIRE IN THE HOLD" (safety first after all).'
            '\n'
            '\n'
            'The results of your guess are indicated as follows:\n'
            '\n'
            'Hit = \U0001F4A5 \n'
            'Miss = \U0001F30A \n'
            '\n'
            'If a players ships are all sunk then the game is over, and the\n'
            'player with even a piece of a ship still above the water wins!\n'
            '\n'
        )
        pause()
        self.clear_display()
        self.welcome_screen()

    def set_players(self):
        """"
        Takes player name and creates player objects
        """
        user = self.name_input()
        user = Player(user)
        computer_player = Player("Computer")
        print("Let the battle commence!")
        self.firing_round(user, computer_player)

    def firing_round(self, player, computer):
        """"
        Loops back and fore between players allowing them to take there guess
        and marking the relevant boards.
        """
        play_round = True
        while play_round:

            player.player_turn(computer)
            play_round = computer.board.is_fleet_sunk()
            if play_round is False:
                print("Hoorah! You won! Neptune god of the seas "
                      "smiles upon you!")
                pause("Press any key to return to the main menu")
                self.restart_game(player, computer)
                break
            loop = input("Wanna run away like scared little sea sponge?\n"
                         "Type exit and I'll let you scurry under a rock, "
                         "otherwise just press enter.").strip(" ")
            if loop.lower() == "exit":
                self.restart_game(player, computer)
                break

            computer.player_turn(player)
            play_round = player.board.is_fleet_sunk()
            if play_round is False:
                print("GAMEOVER! Sorry captain, we're leaving, "
                      "you have to go down with the ship!")
                pause("Press any key to return to the main menu")
                self.restart_game(player, computer)
                break

    @staticmethod
    def name_input():
        """
        Take name in put for human player and check its valid
        """
        valid_name = False
        while not valid_name:
            name = input("What is your sea faring name that you want to go "
                         "down in history with?\n")
            if len(name.strip(" ")) == 0:
                print("Whilst I appreciate your modesty, I am going to need "
                      "your name \n for the tombstone I made you on "
                      "the sea bed. So once again....")
                continue
            elif name.lower() == "computer":
                print("You may be robotic but you don't have my brain I will "
                      "not let you \ninsult me by claiming to be me!"
                      "Pick a again human...")
                continue
            return name

    def restart_game(self, player1, player2):
        """
        Deletes player object and their possessed ship, and boards
        """
        del(player1)
        del(player2)
        self.clear_display()
        self.welcome_screen()


game = Game()
game.welcome_screen()