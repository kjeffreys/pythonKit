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
    

if __name__ == "__main__":
    print(getArr())
    print(getTranspose())
    print("-"*15)
    print("[arr, arr.T, np.dot(arr.T, arr)]:")
    print(dotProduct())
    print("-"*15)
    print(permuteAxes())

