#NumPy

import numpy as np

# print(np.__version__)

# my_list = [1,2,3,4]
# my_list = my_list * 2
# print(my_list)


array = np.array([1,2,3,4,5])
print(array)
print(type(array))

multi = array * 2
print(multi)

arr = np.array(4)
arr = np.array([1,2,3,4])
arr = np.array([[1,2,3,4],
               [4,5,6,7]])

arr = np.array([[[1,2,3,4],
               [4,5,6,7],
               [9,10,11,12]]])

print(arr.ndim)
print(arr)
print(arr.shape)

print(arr.dtype)