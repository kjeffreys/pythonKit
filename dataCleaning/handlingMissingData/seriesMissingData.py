'''
NOTE: Descriptive statistics for pandas objects exclude missing data by default.
 
'''
import numpy as np
import pandas as pd

stringData = pd.Series(['aardvark','artichoke', np.nan, None, 'avocado'])

floatData = pd.Series([1, np.nan, 3.5, np.nan, 7])

'''
Using pandas.dropna() with a pd.Series will return the series with
only the non-null data and index values.
'''
def filterMissingData(data = stringData):
    print("---filterMissingData()---")
    series = data.dropna()
    return series

'''
An alternative way to filter using boolean indexing
'''
def filter2(data = floatData):
    return data[data.notnull()]

if __name__ == "__main__":
    print(stringData)
    print(filterMissingData())
    print(filter2())
    