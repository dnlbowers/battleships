import random
from .mixins import InputMixin, ClearDisplayMixin
from .board import Board


class Player(InputMixin, ClearDisplayMixin):
    """
    Creates a player object and gives it
    the ability to makes guesses, take a turn,
    choose setup type, and Initializes a board
    object belonging to the player
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
        Asks human player if they wish to set the ships up manually
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
                    'Not a valid input, please only type "Q" , "M", "Quick",'
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
                    'chamber?":\nEnter (row then column) eg 0,4 '
                    'or 04: \n').strip(" ")

                guess_coordinate = self.coord_input_validator(guess_coordinate)
                previously_guessed = guess_coordinate in self.guesses

                if previously_guessed:
                    print(
                        "Sir? has the war driven you crazy?\n"
                        "We've already fired there, "
                        "so with all due respect I repeat..."
                        )
                    continue
                else:
                    self.board.user_display()
                    self.guesses.append(guess_coordinate)
                    valid_guess = True

        return guess_coordinate

    def player_turn(self, opponent):
        """"
        Player take a guess and the relevant
        board gets updated with the result
        """
        print(f"{self.name}'s turn")
        guess = self.take_guess()
        guess_hit_check = opponent.board.guess_checker(guess)
        self.board.update_board(guess, guess_hit_check, opponent)
        if self.name != "Computer":
            self.board.user_display()

        else:
            opponent.board.user_display()
