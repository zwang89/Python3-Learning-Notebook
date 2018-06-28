import numpy as np

# create list contain 0, 15 and into 2d matrix that have 3 row five columns
matrix2D = np.arange(15).reshape(3, 5)

# print out the
print(matrix2D)

print(matrix2D.shape)

print(matrix2D.ndim)

myArray = np.array([1, 2, 3, 4, 5, 6])

twoDarray = myArray.reshape(2, 3)

initialmatrix = np.zeros((2, 4))
print(initialmatrix)

numList = np.linspace(0, 2, 9)
print(numList)

a = np.array([[1, 6], [0, 9]])
b = np.array([[7, 4], [2, 3]])

print(a * b)

print(a.sum())
print(a.max())
print(a.min())
print(a.sum(axis=0))

testMatrix = np.array([(2, 5, 8, 3), (1, 3, 6, 0), (6, 88, 9, 11)])
print(np.exp(testMatrix))
print(np.sqrt(testMatrix))

print(testMatrix[2, 3])
print(testMatrix[0:1, 2])