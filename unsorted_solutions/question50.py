"""  Question 50:
Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.
"""


class American(object):
    pass


class NewYorker(American):
    pass


donald = American()
trump = NewYorker()
print(donald)
print(trump)
