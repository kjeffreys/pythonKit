'''
This file demonstrates how some common sequences can be converted into ndarray objects
'''
import numpy as np

def convertList(exList=[6,7.5,8,0,1]):
    ndarray1 = np.array(exList)

    print(ndarray1)

'''
Nested sequences, e.g. list of equal-length lists, will be converted into multidimensional array
'''
def convertNestedLists(exList=[ [1,2,3], [4,5,6], [20,30,100] ]):
    ndarray2 = np.array(exList)
    
    print(ndarray2)

if __name__ == '__main__':
    print("Converting list to numpy array object (ndarray)...")
    convertList()
    convertList(list(range(2,12)))
    print("Converting nested lists to numpy multidimensinal object (ndarray)...")
    convertNestedLists()

