import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(16).reshape((4,4)))
df[:] = np.nan

def origData(df=df):
    print("---origData()---")
    return df

def fillHoles(df=df):
    print("---fillHoles()---")
    df2 = df.fillna(0)
    return df2

'''
Call fillna() with a dict of {colNo: colVal} for each column which will specify
that will have all NA values replaced by the specified corresponding value.
'''
def fillWithDict(df=df):
    print("---fillWithDict()---")
    df2 = df.fillna({ 1:0.5, 2:0 })
    return df2

def fillInPlace(df=df):
    print("---fillInPlace()---")
    _ = df.fillna(0, inplace=True)
    return df

if __name__ == "__main__":
    print(origData())
    print(fillHoles())
    print(fillWithDict())
    print(fillInPlace())