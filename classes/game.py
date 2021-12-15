from getch import pause
import string
from .mixins import ClearDisplayMixin
from .player import Player


class Game(ClearDisplayMixin):
    """
    Creates objects and plays the game by
    calling objects of the other classes
    """

    def __init__(self):
        self.welcome_screen()

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
        prints game instructions in two pages
        with a pause between
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
            'Once in position, it\'s time to let rip!\n'
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
        offers the user a premature exit from the game.
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
                      "you have to go down with the ship!\n"
                      "Water is swirling around you, you've lost.")
                pause("Press any key to return to the main menu")
                self.restart_game(player, computer)
                break

    @staticmethod
    def name_input():
        """
        Take name input for human player and check its valid
        """
        valid_name = False
        while not valid_name:
            name = input("What is your seafaring name that you want to go "
                         "down in history with?\n")
            if len(name.strip(" ")) == 0:
                print("Whilst I appreciate your modesty, I am going to need "
                      "your name \n for the tombstone I made you on "
                      "the sea bed. So once again....")
                continue
            elif name.lower() == "computer":
                print("You may be robotic but you don't have my brain I will "
                      "not let you \ninsult me by claiming to be me!"
                      "Pick again human...")
                continue
            return string.capwords(name)

    def restart_game(self, player1, player2):
        """
        Deletes player object and their possessed ship, and boards
        """
        del(player1)
        del(player2)
        self.clear_display()
        self.welcome_screen()
