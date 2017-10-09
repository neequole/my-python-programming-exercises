# Using index
# def merge(start, mid, end):
#     ptr1 = start
#     ptr2 = mid + 1
#     tmp = []
#     while ptr1 <= mid and ptr2 <= end:
#         if arr[ptr1] <= arr[ptr2]:
#             tmp.append(arr[ptr1])
#             ptr1 += 1
#         else:
#             tmp.append(arr[ptr2])
#             ptr2 += 1
#     # Copy remaining
#     while ptr1 <= mid:
#         tmp.append(arr[ptr1])
#         ptr1 += 1
#     while ptr2 <= end:
#         tmp.append(arr[ptr2])
#         ptr2 += 1
#     # Move back the sorted portion
#     for index, elem in enumerate(tmp):
#         arr[start+index] = elem
#
#
# def merge_sort(start, end):
#     # Stop once we only have one element
#     if start < end:
#         # Perform merge sort to each half of the array
#         mid = (start + end) // 2
#         merge_sort(start, mid)
#         merge_sort(mid+1, end)
#         # Merge the halves after sorting
#         merge(start, mid, end)


# Using array
def merge(left, right, original):
    l_ptr = 0
    r_ptr = 0
    tmp = []
    while l_ptr < len(left) and r_ptr < len(right):
        if left[l_ptr] <= right[r_ptr]:
            tmp.append(left[l_ptr])
            l_ptr += 1
        else:
            tmp.append(right[r_ptr])
            r_ptr += 1
    # Copy remaining
    while l_ptr < len(left):
        tmp.append(left[l_ptr])
        l_ptr += 1
    while r_ptr < len(right):
        tmp.append(right[r_ptr])
        r_ptr += 1

    for index, elem in enumerate(tmp):
        original[index] = elem


def merge_sort(arr):
    arr_len = len(arr)
    # Stop once we only have one element
    if arr_len > 1:
        # Perform merge sort to each half of the array
        mid = arr_len // 2
        l = merge_sort(arr[0:mid])
        r = merge_sort(arr[mid:arr_len])
        # Merge the halves after sorting
        merge(l, r, arr)
    return arr


arr = [3, 4, 1, 2, 5]
print(arr)
merge_sort(arr)
print(arr)

arr1 = [3, 4, 8, 1, 7, 2, 6, 5]
print(arr1)
merge_sort(arr1)
print(arr1)
