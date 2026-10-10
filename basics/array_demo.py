
from array import *

arr1 = array('i',[2,3,4,5])

arr2 = array(arr1.typecode, (n for n in arr1))

arr2[2] = 98

print(arr1)
print(arr2)

# print(arr1.buffer_info())

# for n in arr1:
#     print(n)

print(arr1.tolist())