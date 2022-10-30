import numpy as np

arr1 = np.arange(10)
print(arr1)

arr2 = np.square(arr1)
print(arr2)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = np.array([[-1, -2, -3, -6], [5, 1, 2, 5]])
print(a + b)

print(a.reshape(2, 4))
a_copy = a.flatten()
print(a_copy)

print(a.transpose())


