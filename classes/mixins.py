import os


class InputMixin():
    """"
    Takes the coordinate input from the user.
    check its against several conditionals to ensure its valid
    returns valid coordinate or asks for new input
    """

    def coord_input_validator(self, input):
        """"
        Tests coordinates input by the user and
        checks against several conditions to ensure its valid
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
        Advices input is invalid,
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
