"""  Question 93:

Define a class Person and its two child classes: Male and Female.
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.

"""


class Person(object):
    def get_gender(self):
        raise NotImplementedError


class Male(Person):
    def get_gender(self):
        print('Male')


class Female(Person):
    def get_gender(self):
        print('Female')

alpha_person = Person()
alpha_male = Male()
alpha_female = Female()

try:
    print(alpha_person.get_gender())
except NotImplementedError:
    pass

alpha_male.get_gender()
alpha_female.get_gender()
