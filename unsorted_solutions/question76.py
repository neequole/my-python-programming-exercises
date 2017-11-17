"""  Question 76:
Please write a program to output a random number, which is divisible by 5 and 7,
between 0 and 10 inclusive using random module and list comprehension.


Hints:
Use random.choice() to a random element from a list.
"""
import random

num = None
while True:
    num = random.randrange(0, 11)
    if num % 5 == 0 and num % 7 == 0:
        break
print(num)
