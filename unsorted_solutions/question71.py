"""  Question 71:

Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.


Hints:
Use if/elif to deal with conditions.
"""


def binary_search(start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == num:
        return mid
    elif arr[mid] > num:
        return binary_search(mid+1, end)
    else:
        return binary_search(start, mid-1)


arr = list(map(lambda x: int(x), input("Enter sorted list: ").split(" ")))
num = int(input("Enter number to be search for: "))
print(binary_search(0, len(arr)-1))
