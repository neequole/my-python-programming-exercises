"""  Question 41:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first
half values in one line and the last half values in one line.

Hints:
Use [n1:n2] notation to get a slice from a tuple.
"""


a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
half = len(a) // 2
print(a[:half])
print(a[half:])
