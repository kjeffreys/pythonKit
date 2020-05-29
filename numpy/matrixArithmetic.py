import numpy as np

exampleMatrix = np.array([ [1.,2.,3.], [4.,5.,6.] ])
exampleSquareMatrix = np.array([ [1,2,3], [4,5,6], [15,17,19]])

def elementWiseMultiply(arr=exampleMatrix):
    print("*" * 50)
    print("arr * arr = ({})\n*\n({}) =\n".format(arr, arr))
    return (arr * arr)

def elementWiseAdd(arr=exampleMatrix):
    print("*" * 50)
    print("arr + arr = ({})\n+\n({}) =\n".format(arr, arr))
    return (arr + arr)

def identityMultiply(arr=exampleSquareMatrix):
    print("*" * 50)
    print("arr * I = ({})\n*\n({}) =\n".format(arr, np.eye(3,3,dtype=np.int64)))
    return (arr * np.eye(3,3,dtype=np.int64))

def getIdentyMatrixMult(dimSize):
    print("*" * 50)
    print(np.eye(dimSize,dimSize))
    print("*" * 50)
    print(np.identity(dimSize))

if __name__ == "__main__":
    print(elementWiseMultiply())
    print(elementWiseAdd())
    print(identityMultiply())
    getIdentyMatrixMult(3)
    


