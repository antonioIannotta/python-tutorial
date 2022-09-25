import numpy as np

n = 3
print(n ** 3)
a = np.array([1, 2, 3, 4])
print(a)
#This allows select only certain indexes from the array
print(a[[0, 1, 3]])
#This print the type of the array
print(a.dtype)
b = np.array([1.1, 2.2, 3.3, 4.4])
print(b.dtype)
#This is an array of characters
vowels = np.array(["a", "e", "i", "o", "u"])
print(vowels.dtype)
#This is useful when there's the will to create a matrix with numpy
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
)
print(matrix)
print(matrix[0])
print(matrix[1])
print(matrix[2])

for index in range(0, matrix.__len__()):
    print("Index: " + str(index))
    for element in matrix[index]:
        print(element)

#Now there's an exploration of possible methods on a numpy array

array = np.array([1, 2, 3, 4, 5, 6, 7])
#Thsi prints the sum of the array
print(array.sum())
#This prints the mean of the array
print(array.mean())

second_array = np.array([10, 11, 12, 13, 14, 15, 16])
#This is the sum bewteen the two arrays
print(array + second_array)
#This print the matrix between the two arrays
print(array * second_array)

#Create an array with a specified range






