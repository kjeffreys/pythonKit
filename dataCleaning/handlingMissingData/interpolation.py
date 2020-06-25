'''
The same interpolation methods available for reindexing can be used in fillna
'''
import numpy as np
from numpy import nan as NA
import pandas as pd

df = pd.DataFrame(np.random.randn(6,3))

def usingFillna(df=df):
    print("---usingFillna()---")
    print(df)
    df.iloc[2:, 1] = NA
    print(df)
    df.iloc[4:, 2] = NA
    print(df)
    print("df.fillna(method='ffill')")
    print(df.fillna(method='ffill'))

def fillWithLimit(df=df):
    print("---fillWithLimit()---")
    print(df)
    df.iloc[2:, 1] = NA
    print(df)
    df.iloc[4:, 2] = NA
    print(df)
    print("df.fillna(method='ffill', limit=2)")
    print(df.fillna(method='ffill', limit=2))

'''
One example of value that may be best used for filling NA values is the mean or
median of a Series
'''
def fillWithMeanOfSeries():
    data = pd.Series([1., NA, 3.5, NA, 7])
    print("data:\n{}".format(data))
    data.fillna(data.mean())
    print("data.fillna(data.mean())")
    print(data.fillna(data.mean()))

if __name__ == "__main__":
    usingFillna()
    fillWithLimit()
    fillWithMeanOfSeries()