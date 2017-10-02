"""  Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
"""


class Car(object):
    wheels = 4

    def __init__(self, wheels=None):
        self.wheels = wheels

honda = Car(5)
print(Car.wheels)
print(honda.wheels)

kia = Car()
print(Car.wheels)
print(kia.wheels)
kia.wheels = 4
print(kia.wheels)
