

# unusual output
# absent on this day


import array
arr1 = array.array('i', [10, 20, 30, 40])
arr2 = array.array('i', [50, 60, 70, 80])
arr3 = array.array('i', [])
arr4 = array.array('i', [])

for x in range(len(arr1)):
    new = arr1[x] - arr2[x]
    arr3.append(new)

for y in range(len(arr1)):
    new1 = arr2[y] - arr1[y]
    arr3.append(new1)

print(arr3)
print(arr4)
