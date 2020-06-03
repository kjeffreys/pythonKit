import numpy as np

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
    print("-"*15)
    print(permuteAxes())
    print("-"*15)
    print(reorderAxes())
    print("-"*15)
    print(swapAxes())  