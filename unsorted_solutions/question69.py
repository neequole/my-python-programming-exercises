""" Question 69:
Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints:
Use "assert expression" to make assertion.

"""

for i in [2, 4, 6, 8, 7]:
    assert i % 2 == 0, f"{i} is not even"
