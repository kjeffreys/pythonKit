import numpy as np
import pandas as pd

series = pd.Series(range(4), index=['d','a','b','c'])
frame = pd.DataFrame(np.arange(8).reshape((2,4)), index=['three','one'], columns=['d','a','b','c'])

'''
To sort lexographically by row or column index, use the sort_index() method,
which returns a new sorted object
'''
def sortSeries(series=series):
    print("---sortSeries()---")
    return series.sort_index()

'''
Default sorts by row index
'''
def sortDataFrame(df=frame):
    print("---sortDataFrame()---")
    return df.sort_index()

def sortDataFrameColumns(df=frame):
    print("---sortDataFrameColumns()---")
    return df.sort_index(axis='columns')

'''
Sorts are ascending by default. Can set to descending with option
'''
def sortColumnsDescending(df=frame):
    print("---sortColumnsDescending()---")
    return df.sort_index(axis='columns', ascending=False)

'''
Missing / NaN values are sorted to the end by default
'''
def sortSeriesByValues(series=pd.Series([4,-7,-3,np.nan,6,2])):
    print("---sortSeriesByValues()---")
    return series.sort_values()

'''
When sorting a DataFrame, you can use the data in one or more columns as the sort keys.
'''
def multiColSort():
    print("---multiColSort()---")
    df = pd.DataFrame({'b': [4,7,-3,2], 'a': [0,1,0,1]})
    print("df:")
    print(df)
    print("df.sort_values(by='b'):")
    print(df.sort_values(by='b'))
    print("df.sort_values(by=['a','b'")
    return df.sort_values(by=['a','b'])

if __name__ == "__main__":
    print(sortSeries())
    # index sorts by alpha, so following example is not ['one', 'two', 'three', 'four'], but ['four', 'one', 'three', 'two']
    print(sortSeries(series=pd.Series(range(4), index=['two','three','one','four'])))
    print(sortDataFrame())
    print(sortDataFrameColumns())
    print(sortColumnsDescending())
    print(sortSeriesByValues())
    print(multiColSort())
    