import array

arr = array.array('i', [1, 2, 3, 4, 6, 8, 10])

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(arr[i], end=" ")