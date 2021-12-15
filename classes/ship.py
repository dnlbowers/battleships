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
