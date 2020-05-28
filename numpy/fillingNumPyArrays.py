import numpy as np
import pprint

'''
Demonstrations .zeros()
Fills a matrix with 0s
'''
def getZeros(dim1, dim2):
    return np.zeros((dim1,dim2), dtype=np.int64)

def getOnes(dim1, dim2, dim3):
    return np.ones((dim1,dim2,dim3))

if __name__ == '__main__':
    print(getZeros(3,3))
    print()
    print(pprint.pprint(getOnes(4,2,3)))