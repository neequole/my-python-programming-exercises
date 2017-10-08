"""  Question 52:
Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
"""


class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


floor = Rectangle(5, 3)
print(floor.length)
print(floor.width)
print(floor.area())
