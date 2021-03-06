'''
File to demonstrate some uses of the N-dimensional array object from numpy
'''
import numpy as np

'''
Generate random numbers as the contents of a 2D array using numpy

Note: np.random.rand() can take more dimensions with more args
'''
def rand2Darray(dim1, dim2):
    data = np.random.rand(dim1, dim2)

    print("Data:\n{}".format(data))

    return data

def scalarMultiplyMatrix(array, scalar):
    print("\nData * 10:\n{}".format(array * 10))

def matrixAddToSelf(array):
    print("\nData + Data:\n{}".format(array + array))

def matrixSize(matrix):
    return matrix.shape

'''
Returns data type of the scalar components of the matrix (must be uniformly integers, floats, etc.)
'''
def matrixType(matrix):
    return matrix.dtype


if __name__ == '__main__':
    print("----rand2Darray()----")
    rand2Darray(3, 3)
    print("----scalarMultiplyMatrix()----")
    scalarMultiplyMatrix(rand2Darray(3,3), 10)
    print("----matrixAddToSelf()----")
    matrixAddToSelf(rand2Darray(2,5))
    print("----matrixSize()----")
    print(matrixSize(rand2Darray(1,7)))
    print("----matrixType()----")
    print(matrixType(rand2Darray(1,7)))
    print("----matrixType()----")
    print(matrixType(rand2Darray(1,7)))