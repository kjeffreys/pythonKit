import numpy as np
import pandas as pd

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                        'k2': [1,1,2,3,3,4,4]})

def origData(df=data):
    print("---origData()---")
    return df

def showDuplicates(df=data):
    print("---showDuplicates()---")
    return df.duplicated()

def dropDuplicates(df=data):
    print("---dropDuplicates()---")
    return df.drop_duplicates()

'''
By default duplicate operations apply to all columns. Speicfy any subset
of columns to detect duplicates on the subset.
'''
def subsetCols(df=data):
    print("---subsetCols()---")
    df['v1'] = range(7)
    print(df)
    print("df.drop_duplicates(['k1'])")
    return df.drop_duplicates(['k1'])

if __name__ == "__main__":
    print(origData())
    print(showDuplicates())
    print(dropDuplicates())
    print(subsetCols())