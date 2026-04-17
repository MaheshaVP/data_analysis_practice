#file handling in numpy

import numpy as np

a = np.array([10,20,30,40])
np.save('data.npy',a)

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,0])

np.savez('data.npz',array1=arr1, array2=arr2 )

data = np.load('data.npy')
print(data)

data = np.load('data.npz')
print(data['array1'])
print(data['array2'])

sales = np.array([100,200,300,400])
np.save('sales.npy',sales)

result = np.load('sales.npy')
print(np.sum(result))
print(np.mean(result))