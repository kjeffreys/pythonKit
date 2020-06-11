import pandas as pd
import numpy as np

dataFrame = pd.DataFrame(np.arange(16).reshape((4,4,)), index=['Ohio','Colorado','Utah','New York'], columns=['one','two','three','four'])

def selectColumn(colName='two'):
    print("---selectColumn()---")
    return dataFrame[colName]

def showIndex(methodArg=selectColumn()):
    df=methodArg
    print(df)
    print("---showIndex()---")
    return df.index

def selectMultipleCols(cols=['one', 'four']):
    print("---selectMultipleCols()---")
    return dataFrame[cols]

def selectRows(df=dataFrame):
    print("---selectRows()---")
    return df[:2]

'''
Filters resulting rows (similar to sql WHERE)
'''
def booleanSelectRows(df=dataFrame, col='one'):
    print("---booleanSelectRows()---")
    return df[ df[col] > 9]

def booleanElementIndexing(df=dataFrame, val=8):
    print("---booleanElementIndexing()---")
    return df <= val

def booleanAssignment(df=dataFrame, val=8):
    print("---booleanAssignment()---")
    df[ df <= val] = 100
    return df

if __name__ == '__main__':
    print(dataFrame)
    print("-" * 30)
    print(showIndex())
    print(showIndex(methodArg=selectMultipleCols()))
    print(selectRows())
    print(booleanSelectRows())
    print(booleanElementIndexing())
    print(booleanAssignment())
