"""  Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""


class Printer(object):
    def __init__(self, s=None):
        self.s = s

    def get_string(self):
        self.s = input("Input anything: ")

    def print_string(self):
        print(self.s)


def test():
    """ Test function """
    p = Printer()
    # Ensure there is no string yet
    assert not p.s
    p.get_string()
    assert p.s
    p.print_string()


test()
