"""  Question 97:

Please write a program which prints all permutations of [1,2,3]


Hints:
Use itertools.permutations() to get permutations of list.
"""


from itertools import permutations


print(list(permutations([1, 2, 3])))
