'''
A Series is a 1D array-like object containg a sequnce of values (types similar to numpy types (.e.g. dtype: int64))
and an associated array of data labels, called its "index".
'''
import pandas as pd

listArg = [4,7,-5,3] #list to represent numpy like array
sampleIndex=['Ocelot', 'Aardvark', 'Zebra', 'Python']

def createSeries(arrayArg=listArg):
    print("---createSeries({})---".format(arrayArg))
    return pd.Series(arrayArg)

def getValues(arrayArg=listArg):
    print("---getValues( pd.Series({}) )---".format(listArg))
    series = pd.Series(arrayArg)
    return series.values

def getIndex(arrayArg=listArg):
    print("---getIndex( pd.Series({}) )---".format(listArg))
    series = pd.Series(arrayArg)
    return series.index

def addIndex(arrayArg=listArg, index=sampleIndex):
    print("---addIndex( series.index={} )---".format(index))
    series = pd.Series(arrayArg, index=index)
    return series

'''
Note: can change ordering as well as select subset of elements

"elements" is interpreted as a list of indices
'''
def selectElements(arrayArg=listArg, index=sampleIndex, elements=['Aardvark', 'Ocelot', 'Python']):
    print("---selectElements( series[{}] )---".format(elements))
    series = pd.Series(arrayArg, index=index)
    return series[elements]

if __name__ == "__main__":
    print(createSeries())
    print(getValues())
    print(getIndex())
    print(addIndex())
    print(selectElements())