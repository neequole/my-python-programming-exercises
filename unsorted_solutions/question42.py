"""  Question 42:
Write a program to generate and print another tuple whose values are even
numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

Hints:
Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.
"""

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
out = tuple([num for num in a if num % 2 == 0])
print(out)
