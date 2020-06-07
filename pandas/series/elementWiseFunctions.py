'''
Using NumPy functions or Numpy-like operations, e.g. filtering with a boolean array,
scalar multiplication, or applying math functions, preserves the index-value link 
of pd.Series objects.
'''
import numpy as np
import pandas as pd

listArg = [4,7,-5,3] #list to represent numpy like array
sampleIndex=['Ocelot', 'Aardvark', 'Zebra', 'Python']

def greaterThan(arr=listArg, index=sampleIndex, operand=0):
    print("---greaterThan({})---".format(operand))
    series = pd.Series(arr, index=index)

    return series[series > operand]

def multiplyBy(arr=listArg, index=sampleIndex, operand=2):
    print("---multiplyBy({})---".format(operand))
    series = pd.Series(arr, index=index)

    return (series * 2)

def exponentialFunction(arr=listArg, index=sampleIndex):
    print("---exponential Fn(~2.74^series)---")
    series = pd.Series(arr, index=index)

    return (np.exp(series))

def hasKey(arr=listArg, index=sampleIndex, key='Aardvark'):
    print("---hasKey({})---".format(key))
    series = pd.Series(arr, index=index)

    return key in series

if __name__ == "__main__":
    print(greaterThan(operand=3))
    print(multiplyBy())
    print(exponentialFunction())
    print(hasKey())
    print(hasKey(key='Zebra'))
    print(hasKey(key='Giraffe'))