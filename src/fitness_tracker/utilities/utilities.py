"""
Fitness Tracker application logic validation
helper methods.
"""


class Utilities:

    def __init__(self, prompt: str):
        self.prompt = prompt

    def get_integer(self):
        """
        Validates and returns integers from
        input statements.

        :return: Valid integer.
        """
        while True:
            try:
                return int(input(self.prompt))
            except ValueError:
                print("Please enter a number.")