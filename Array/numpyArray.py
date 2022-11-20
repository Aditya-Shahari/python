import numpy
# arr = numpy.array([10, 20, 30, 40, 50])
# print(type(arr[0]))   #<class 'numpy.int32'>

arr1 = numpy.array([10, 20, 30, 40])
arr2 = numpy.array([8, 7, 1, 50])
# for x in range(len(arr1)):
#     print(arr1[x] <= arr2[x])

arr3 = arr1 <= arr2
print(arr3)
print(type(arr3[2]))
print(type(arr3[2]))
print(arr1[0])