arr = [3, 4, 8, 1, 7, 2, 6, 5]
n = len(arr)

# Lightest to bottom
# for i in range(0, n-1):
#     for j in range(n-1, i, -1):
#         if arr[j] < arr[j-1]:
#             tmp = arr[j-1]
#             arr[j-1] = arr[j]
#             arr[j] = tmp

# Heaviest to top
for i in range(n-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp


print(arr)
