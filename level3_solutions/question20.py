"""  Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n.

Hints:
Consider use yield
"""


def foo(n):
    i = 0
    while i < n:
        if i % 7 == 0:
            yield i
        i += 1

for i in foo(100):
    print(i)
