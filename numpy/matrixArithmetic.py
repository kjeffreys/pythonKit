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

def elementWiseDivide(arr=exampleMatrix, dividend=1):
    print("*" * 50)
    print("{} / arr = 1 /\n({}) =\n".format(dividend, arr))
    return dividend / arr

def elementWiseExponent(arr=exampleMatrix, exponent=2):
    print("*" * 50)
    print("arr ** {} = ({})\n(to the power {}) =\n".format(exponent, arr, exponent))
    return (arr ** exponent)

def booleanArrayComparison(arr1=exampleMatrix, arr2=np.array([ [4,2,1], [1,6,20] ])):
    print("*" * 50)
    print("arr1 = {}".format(arr1))
    print("arr2 = {}".format(arr2))
    print("arr1 < arr2 =\n")
    return arr1 < arr2

if __name__ == "__main__":
    print(elementWiseMultiply())
    print(elementWiseAdd())
    print(identityMultiply())
    getIdentyMatrixMult(3)
    print(elementWiseDivide())
    print(elementWiseExponent())
    print(booleanArrayComparison())
    


