"""  Question 53:
Define a class named Shape and its subclass Square.
The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where
Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.
"""


class Shape(object):
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        # TODO: do we need to call init of superclass?
        # Credit to https://stackoverflow.com/questions/1385759/should-init-call-the-parent-classs-init
        # super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2


ditto = Shape()
print(ditto.area())

ice = Square(3)
print(ice.length)
print(ice.area())
