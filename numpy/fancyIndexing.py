'''
Fancy indexing is a term from NumPy to describe indexing using integer arrays.

@author Kyle Jeffreys
'''
import numpy as np

def eightByFour():
    arr = np.empty((8,4))

    for i in range(8):
        arr[i] = i

    return arr

def selectSubset():
    arr = eightByFour()

    return arr[[4,3,0,7]]

'''
Works like slicing in typical python sequences
'''
def negativeIndexing():
    arr = eightByFour()

    return arr[[-1,-2,-7]]

def reshaping():
    arr = np.arange(32).reshape((8,4))

    return arr

'''
Returns 1D array. Positions are are the tuple pairs from the 2 inners arrays
(Uses fancy indexing. Fancy indexing always makes a copy of the array)
'''
def oneDimArrFromMultiIndexTuples():
    arr = reshaping()

    # [ (1,0) , (5,3) , (7,1) , (2,2)]
    newArr = arr[ [1,5,7,2], [0,3,1,2] ]

    return newArr

'''
The above function still uses fancy indexing. In order to get a rectangular region
formed by the subset of the matrix, one alternative is the following function
'''
def subsetMatrix():
    arr = reshaping()

    newarr = arr[ [1,5,7,2]][:, [0,3,1,2] ] # [0,3,1,2] reorders the elements displayed [4,5,6,7] -> [4,7,5,6]

    return newarr

if __name__ == "__main__":
    print(eightByFour())
    print("-" * 15)
    print(selectSubset())
    print("-" * 15)
    print(negativeIndexing())
    print("-" * 15)
    print(reshaping())
    print("-" * 15)
    print(oneDimArrFromMultiIndexTuples())
    print("-" * 15)
    print(subsetMatrix())