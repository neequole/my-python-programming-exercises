"""  Question 51:
Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
"""
import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


pie = Circle(3)
print(pie.radius)
print(pie.area())
