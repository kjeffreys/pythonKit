import numpy as np

exampleArr = np.arange(15).reshape((3,5))

def getArr(arr=exampleArr):
    return arr

def getTranspose(arr=exampleArr):
    return arr.T

def dotProduct(arr=np.random.randn(4,2)):
    print("{} :\n{}".format(arr.T.shape, arr.T))
    print("{} :\n{}".format(arr.shape, arr))
    print("{} :".format(np.dot(arr.T,arr).shape))
    return np.dot(arr.T, arr)

def permuteAxes(arr=np.arange(16).reshape(2,2,4)):
    print(arr)
    print("(transpose) ->")
    return arr.transpose()

def reorderAxes(arr=np.arange(16).reshape(2,2,4)):
    print(arr)
    print("reordering axes (1,0,2):")
    return arr.transpose(1,0,2) # (dim0, dim1, dim2) -> (dim1, dim0, dim2)

def swapAxes(arr=np.arange(16).reshape(2,2,4)):
    print(arr)
    print("swapaxes (1,2):")
    return arr.swapaxes(1,2)    

if __name__ == "__main__":
    print(getArr())
    print(getTranspose())
    print("-"*15)
    print("[arr, arr.T, np.dot(arr.T, arr)]:")
    print(dotProduct())
    print("-"*15)
    print(permuteAxes())
    print("-"*15)
    print(reorderAxes())
    print("-"*15)
    print(swapAxes())

