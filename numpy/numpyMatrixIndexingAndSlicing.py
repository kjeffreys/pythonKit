import numpy as np

exampleArr = np.arange(10)
twoDimArr = [ [0,1,2], [3,4,5], [6,7,8] ]

def showSlice(fromIndex, toIndex, arr=exampleArr):
    # print(arr[5])
    return arr[fromIndex:toIndex]

'''
Function that demonstrates how the original numpy array will be changed as the view is not a copy.
Appears to be implemented like a C/C++ array (pointer to memory with a type for iterating by size(type))
'''
def viewOnNumPyArray(fromIndex, toIndex, arr=exampleArr):
    print("Original array: {}".format(arr))
    print("Assigning slice...")
    print("arr_slice = arr[{}:{}]".format(fromIndex, toIndex))
    arr_slice = arr[fromIndex:toIndex]
    print("arr_slice = {}".format(arr_slice))
    print("Assigning to slice...arr_slice[0:3] = 10")
    arr_slice[:] = -5
    print("arr_slice = {}".format(arr_slice))
    print("Original array after slice assignment = {}".format(exampleArr))
    # this actually changes the numbers in the global variable exampleArr

    return arr

def getRowFrom2D(def)

if __name__ == "__main__":
    print(showSlice(5,9))
    viewOnNumPyArray(2,7)