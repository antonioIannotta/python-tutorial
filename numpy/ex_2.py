import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)

print(arr[0, 3])
print(arr[:, 3])

print(arr[0])
arr[1] = 4
print(arr)