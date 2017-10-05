"""  Question 49:
Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.
"""


class American(object):
    @staticmethod
    def print_nationality():
        print('American')

American.print_nationality()
trump = American()
trump.print_nationality()
