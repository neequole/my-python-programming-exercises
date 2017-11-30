"""  Question 92:

With a given list [12,24,35,24,88,120,155,88,120,155], write a program to
print this list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.
"""
from collections import OrderedDict

original_list = OrderedDict.fromkeys([12,24,35,24,88,120,155,88,120,155])
print(list(original_list.keys()))
