'''
loc and iloc are explicit indexing operators.

Enable users to select a subset of rows/cols from a DataFrame with NumPy-like notation
using either axis labels(loc) or integers(iloc)
'''
import numpy as np
import pandas as pd

dataFrame = pd.DataFrame(np.arange(16).reshape((4,4,)), index=['Ohio','Colorado','Utah','New York'], columns=['one','two','three','four'])

def selectOneRowTwoCols(df=dataFrame):
    print("---selectOneRowTwoCols()---")
    return df.loc['Colorado', ['two','three']] #loc[rowSelection, colSelection]
    #written out for explicit demo
    #could do df=dataFrame, row='Colorado, cols=['two','three']...return df.loc[row, cols]

'''
Similar select using iloc ('integer loc')
'''
def ilocSelect(df=dataFrame):
    print("---ilocSelect()---")
    return df.iloc[2, [3,0,1]] #loc[rowSelection, colSelection]
    #written out for explicit demo
    #could do df=dataFrame, row='Colorado, cols=['two','three']...return df.loc[row, cols]

def ilocSelectRow(df=dataFrame):
    print("---ilocSelectRow()---")
    return df.iloc[2]

def ilocTwoRowsTwoCols(df=dataFrame):
    print("---ilocTwoRowsTwoCols()---")
    return df.iloc[ [0,3],[3,1,2] ]

def locSlicing(df=dataFrame):
    print("---locSlicing()---")
    return df.loc[:'Utah', 'two']

def ilocSlicing(df=dataFrame):
    print("---ilocSlicing()---")
    return df.iloc[1:, :3]

def ilocSliceAndFilter(df=dataFrame):
    print("---ilocSliceAndFilter()---")
    return df.iloc[1:, :3][df.three > 13]

if __name__ == "__main__":
    print(dataFrame)
    print(selectOneRowTwoCols())
    print(ilocSelect())
    print(ilocSelectRow())
    print(ilocTwoRowsTwoCols())
    print(locSlicing())
    print(ilocSlicing())
    print(ilocSliceAndFilter())

