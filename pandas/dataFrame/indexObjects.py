'''
pandas Index objects hold axis labels and metadata about pandas data structures.

Any array or other sequence of labels used when constructing a Series or DataFrame are internally
converted to an Index.

The following methods when printed demonstrate the contents of an Index object (e.g. Index(['a','b','c']))
and it's dtype (will be 'gcd type' so to speak if different types exist, e.g. for numbers and strings, dtype='object')

NOTE: Index objects are immutable.

'''
import sampleData as sd
import numpy as np


# sd.indexObjSeries = pd.Series(range(3), index=['a', 'b', 'c'])
def indexObjEx1(series = sd.indexObjSeries):
    print("---indexObjEx1()---")
    return series.index

def indexObjEx2(series = sd.indexObjSeries):
    print("---indexObjEx2()---")
    return series.index[1:]

def indexObjsAreImmutable(series = sd.indexObjSeries):
    print("---indexObjsAreImmutable()---")
    
    try:
        series[1] = 'y'
    except Exception as te:
        errMsg = "An exception of type {} occurred.".format(type(te).__name__)
        print(errMsg)
    finally:
        return -1

'''
Because Index objects are immutable, it is safe to share Index objects among multiple pandas data structures
'''
def safeWithImmutability():
    print("---safeWithImmutability()---")
    labels = sd.pd.Index(np.arange(3))
    print("labels = np.arange(3) = {}".format(labels))
    obj2 = sd.pd.Series([1.5,-2.5,0], index=labels)
    print("obj2 = pd.Series([1.5, -2.5, 0])")
    print("(obj2.index is labels) :")
    return obj2.index is labels


if __name__ == "__main__":
    print(indexObjEx1())
    print(indexObjEx2())
    print(indexObjsAreImmutable())
    print(safeWithImmutability())

