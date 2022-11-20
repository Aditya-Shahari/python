import array

arr = array.array('i', [1, 3, 2, 7, 9, 10, 12])
flag = 0

for x in range(len(arr)):
    if arr[x] == 0 or arr[x] == 1:
        continue
    curr = arr[x]
    start = 2
    while start < curr:

        if curr % start == 0:
            flag = 1
            break
        start += 1
    if flag == 0:
        print(curr, end=" ")
    flag = 0