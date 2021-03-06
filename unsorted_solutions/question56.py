"""  Question 56:
Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.
"""


class CustomException(Exception):
    def __init__(self, msg):
        self.message = msg


err = CustomException('You got tricked!')
print(err)
print(err.message)
