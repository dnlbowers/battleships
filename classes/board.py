import random
from getch import pause
from .mixins import InputMixin, ClearDisplayMixin
from .ship import AircraftCarrier, Battleship, Cruiser, Submarine, Destroyer


class Board(InputMixin, ClearDisplayMixin):
    """"
    Builds the boards where ships will be placed
    and gives object ability to function
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
        Builds a blank board using nested lists.
        will be used to store the shp objects
        """
        self.board = []

        for row in range(self.board_size):
            self.board.append([])
            for _ in range(self.board_size):
                self.board[row].append("\U000025FD")
        return self.board

    def build_guess_board(self):
        """"
        Builds a blank board using nested lists
        will be use to keep note of a players guess
        results
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
        and their guess board with headers and indexing
        """
        self.clear_display()
        print((" ") * 16 + f"These sea charts belong to Captain {self.owner}")
        print((" ") * 4 + "Map of your Fleet:              "
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
                # Randomized setup
                random_start = (random.randint(0, 9), random.randint(0, 9))
                random_direction = random.choice(["r", "d"])
                ship_instance = ship_obj_type[i](
                    random_start, random_direction, (random_start))

            else:
                # manual set up
                self.user_display()
                start_position = input(
                    f"From where would you like your {ship_obj_type[i].name} "
                    "to start?\n"
                    f"This ship requires {ship_obj_type[i].length} free tiles."
                    "\nPlease enter two numbers (row then column)\n"
                    "i.e 4,5 or 45: \n").strip(" ")

                # validates coodrinate input, calls directional input function
                # and creates ship object
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

                # works out which index in the start position tuple needs
                # to be increased based on direction
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

                # Check if ship will go over the board edge
                # and requests/generates new start coordinate if required
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
                            f"{ship.name}? \nPlease enter two numbers "
                            "(row then column) i.e 4,5 or 45: \n").strip(" ")
                        ship.start_coordinate = self.coord_input_validator(
                            ship.start_coordinate)
                        ship.direction = self.direction_input()
                        break

                # If next tile is unoccupied, add the coordinate to
                # a temporay list and if list is equal to the
                # ship length it is returned to the calling function
                elif not duplicate_tile:
                    temp_ship.append(next_tile)
                    if len(temp_ship) == ship.length:
                        ship.coordinates = temp_ship
                        placement_process = False
                        return ship.coordinates

                # If any tile in the process is occupied a new start coordinate
                # is requested/generated and the process starts again
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
                            f"{ship.name}? \nPlease enter two numbers "
                            "(row then column) i.e 4,5 or 45: \n").strip(" ")
                        ship.start_coordinate = self.coord_input_validator(
                            ship.start_coordinate)
                        ship.direction = self.direction_input()
                        break
        return ship.coordinates

    def direction_input(self):
        """"
        Requests user input to choose ship direction
        loops until valid input is entered
        handles incorrect inputs
        """
        invalid_input = True
        while invalid_input:
            ship_direction = input(
                "From the back of the boat, to which direction is the front "
                "end pointing?\nTo the (r)ight or (d)own: \n"
            ).lower().strip(" ")
            if ship_direction == "right" or ship_direction == "r":
                invalid_input = False
                return "right"
            elif ship_direction == "down" or ship_direction == "d":
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
            # miss uses unicode for ocean emoji
            self.guess_board[guess[0]][guess[1]] = "\U0001F30A"
            opponent.board.board[guess[0]][guess[1]] = "\U0001F30A"
            # Code will only ever show the human users view
            if self.owner != "Computer":
                self.user_display()
            else:
                opponent.board.user_display()
            print(f"SPLASH!!! {self.owner} missed")
            pause()

        else:
            # hit uses unicode for collision emoji
            self.guess_board[guess[0]][guess[1]] = "\U0001F4A5"
            opponent.board.board[guess[0]][guess[1]] = "\U0001F4A5"
            # Code will only ever show the human users view
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
