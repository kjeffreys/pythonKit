'''
With DataFrame objects, drop rows or columns that are all NA
or containing any NAs can be done with dropna().

NOTE: dropna() by default drops any row containing missing a missing value.
'''
from numpy import nan as NA
import numpy as np
import pandas as pd

data = pd.DataFrame([ [1., 6.5, 3.], [1.,NA,NA], [NA,NA,NA], [NA,6.5,3.] ])

def origData(data=data):
    print("---origData()---")
    return data

def cleanedData(data=data):
    print("---cleanedData()---")
    cleaned = data.dropna()
    return cleaned

'''
Passing "how=all" will only drop rows that are ALL NA.
'''
def cleanEmptyRowsOnly(data=data):
    print("---cleanEmptyRowsOnly()---")
    cleaned = data.dropna(how='all')
    return cleaned

'''
To drop columns, pass axis=1
'''
def dropBadColumns(data=data):
    print("New matrix:")
    # add another row of all NA values
    data[3] = NA
    print(data)
    print("---dropBadColumns()---")
    return data.dropna(axis=1, how='all')

'''
A common filter case with time series data involves wanting to keep
only rows containing a certain number of observations. This can be indicated
with the thresh argument.

In this case, thresh=2 limits rows to a maximum of 2 "NA" values.
'''
def filterTimeSeries():
    print("---filterTimeSeries()---")
    df = pd.DataFrame(np.random.randn(7,3))
    print("df:")
    print(df)
    print("df.iloc[:4, 1] = NA:")
    df.iloc[:4, 1] = NA
    print(df)
    print("df.iloc[:2, 2] = NA:")
    df.iloc[:2, 2] = NA
    print(df)
    print("df.dropna():")
    print(df.dropna())
    print("df.dropna(thresh=2):")
    print(df.dropna(thresh=2))


if __name__ == "__main__":
    print(origData())
    print(cleanedData())
    print(cleanEmptyRowsOnly())
    print(dropBadColumns())
    print(filterTimeSeries())