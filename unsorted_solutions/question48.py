"""  Question 48:
Write a program which can map() to make a list whose elements are square of
numbers between 1 and 20 (both included).

Hints:

Use map() to generate a list.
Use lambda to define anonymous functions.
"""


out = list(map(lambda x: x ** 2, range(1, 21)))
print(out)
