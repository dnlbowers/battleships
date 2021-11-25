# This will generate the boards co-ordinates
#coordinates = [(row, column) for row in range(self.rows) for column in range(self.columns)]

#creates a dictionary of coordinates, will use later to place ships and check for hits
# {(row,column):"~" for row in range(self.rows) for column in range(self.columns)
#             if row != 0 and column != 0}
# for the player guess consider a class method to split the string https://youtu.be/rq8cL2XMM5M


class Board:
    """
    Creates Boards for both the user and the computer.
    """
    def __init__(self, size, name, num_of_ships):
        self.size = size
        self.name = name
        #think about making this a class variable(num_of_ships = 5) but may need
        #to move to ships class
        #sample - https://www.youtube.com/watch?v=BJ-VvGyQxho
        self.num_of_ships = num_of_ships

    #maybe make this a static method @staticmethod func with no params https://youtu.be/rq8cL2XMM5M


#this may be a subclass of board to place ships

class Ships(Board):
    """
    Creates a naval fleet to be placed on the board by the player.
    Give method for auto deployment of ships on the board.
    Auto deployment is optional for the player but mandatory for the computer.
    """
    def __init__(self, name):
        super().__init__(name)
        self.naval_fleet = {
            "Carrier": 5,
            "Battleship": 4,
            "Cruiser": 3,
            "Submarine": 3,
            "Destroyer": 2
    }

    def auto_deploy(self):
        """
        Auto deploys ships on the board.
        """
        coordinates = [(random.randint(0, 9), random.randint(0, 9))
            for _ in range(len(self.naval_fleet))]
        direction = [random.randint(0,1) for _ in range(len(self.naval_fleet))]
        
        print (direction)
        print (coordinates)


    #Possible method to place ships on the board:
    # def place_ship(self, ship, start_row, start_col, end_row, end_col):
    #     """
    #     Places a ship on the board.
    #     """
    #     if start_row == end_row:
    #         for col in range(start_col, end_col + 1):
    #             self.board[start_row][col] = ship
    #     elif start_col == end_col:
    #         for row in range(start_row, end_row + 1):
    #             self.board[row][start_col] = ship
    #     else:
    #         raise ValueError("Invalid ship placement.")


# Build boards
player_board = Board(10, "Player", 5)
pprint(player_board.build_board())



print(issubclass(Board, Player))
print(isinstance(player, Player))

 if next_tile[0] + i > 9:
                        print("Out of bounds")
                        placement_process = False
                        break
                    elif next_tile in occupied_tiles:
                        print("Tile occupied")
                        placement_process = False
                        break
#print(help(Ships))

# how do I put this into the class?
# # I want to be able to use the below to create a ship object for and add to the board.
# ship_keys = ["name", "length"]
# name_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
# length_list = [5, 4, 3, 3, 2]
# fleet = []
# ships=[]

# the logic to auto create fleet and auto place them on the board.
# for i in range(len(name_list)):
#     ship = Ship(name_list[i], length_list[i], (random.randint(0, 9), random.randint(0, 9)), random.choice(["r", "d"]), [])
#     fleet.append(ship)

#     print(ship.__dict__)
# print(fleet[0].build_ship())
# print(fleet[1].build_ship())

# logic for the user to maunally place ships.
# for p in range(len(name_list)):
#     start_position = input(f"From which coordinate to you wish to start you {name_list[p]}? Separate to numbers with a comma i.e 4,5 : ").split(",")
#     start_position = [int(i) for i in start_position]
#     test = Ship(name_list[p], length_list[p], start_position, (input("From the bow in which direction is stern pointing? (r)ight or (d)own: ")), [])
#     ships.append(test)
    
# print (ships[1].__dict__)
# print(start_position)

# Carrier =Ship("Aircraft Carrier",5, start_position, "d", [])
# Carrier.build_ship()
# print(Carrier.coordinates)

# start_position = input("Where would you like to place your Submarine? Separate to numbers with a comma i.e 4,5 : ").split(",")
# start_position = [int(i) for i in start_position]
# print(start_position)

# sub =Ship("Submarine", 3, start_position, "r", [])
# sub.build_ship()
# print(sub.coordinates)
# print(Carrier.coordinates)




# player_name = input("What is your name? ")
# player = Board(player_name)
# computer = Board("Computer")


# pprint(player.__dict__)
# pprint(computer.__dict__)

# print(player.name + ", place your ships!")

# Board.print_board(player)
# Board.print_board(computer)

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
