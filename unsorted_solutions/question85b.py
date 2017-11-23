"""
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.
"""

nums = [5,6,77,45,22,12,24]
out = [x for x in nums if x % 2 != 0 ]
print(out)
