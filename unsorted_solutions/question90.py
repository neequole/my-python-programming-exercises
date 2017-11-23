"""  Question 90:

By using list comprehension, please write a program to print the list after
removing the value 24 in [12,24,35,24,88,120,155].

Hints:
Use list's remove method to delete a value.
"""

nums = [12,24,35,24,88,120,155]
# nums.remove(24)
# print(nums)
out = list(filter(lambda x: x != 24, nums))
print(out)
