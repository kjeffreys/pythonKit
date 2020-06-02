import numpy as np

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

dataMatrix =  np.random.randn(7,4)

def getNames(names=names):
    return names

def getData(matrix=dataMatrix):
    return dataMatrix

def getBoolArr(name='Bob', names=names, data=dataMatrix):
    newArr = names.copy()
    boolArr = (newArr == 'Bob')
    print("names == 'Bob':")
    return boolArr

def where(name='Bob', names=names, data=dataMatrix):
    print("data[names == 'Bob']:")
    newArr = names.copy()
    boolArr = newArr[newArr == 'Bob']
    return boolArr

if __name__ == "__main__":
    print("names = {}".format(getNames()))
    print("data = {}".format(getData()))
    print("----Processing data----")
    print(getBoolArr())
    print(where())