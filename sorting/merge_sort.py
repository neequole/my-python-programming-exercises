def merge(start, mid, end):
    ptr1 = start
    ptr2 = mid + 1
    tmp = []
    while ptr1 <= mid and ptr2 <= end:
        if arr[ptr1] <= arr[ptr2]:
            tmp.append(arr[ptr1])
            ptr1 += 1
        else:
            tmp.append(arr[ptr2])
            ptr2 += 1
    # Copy remaining
    while ptr1 <= mid:
        tmp.append(arr[ptr1])
        ptr1 += 1
    while ptr2 <= end:
        tmp.append(arr[ptr2])
        ptr2 += 1
    # Move back the sorted portion
    for index, elem in enumerate(tmp):
        arr[start+index] = elem


def merge_sort(start, end):
    # Stop once we only have one element
    if start < end:
        # Perform merge sort to each half of the array
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        # Merge the halves after sorting
        merge(start, mid, end)


#arr = [3, 4, 1, 2, 5]
#print(arr)
#merge_sort(0, len(arr)-1)
#print(arr)

arr = [3, 4, 8, 1, 7, 2, 6, 5]
print(arr)
merge_sort(0, len(arr)-1)
print(arr)
