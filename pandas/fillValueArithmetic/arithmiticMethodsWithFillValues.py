import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.arange(12.).reshape((3,4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4,5)), columns=list('abcde'))
df2.loc[1, 'b'] = np.nan

def joinLikeAdd(df1=df1, df2=df2):
    print("---joinLikeAdd()---")
    print(df1)
    print("+")
    print(df2)
    print("-" * 40)
    return df1 + df2

'''
Will fill 0 to NaN values on either left or right matrix operand
'''
def addWithFill(df1=df1, df2=df2):
    print("---addWithFill()---")
    return df1.add(df2, fill_value=0)

def reindexWithAddedColumns(df1=df1, df2=df2):
    print("---reindexWithAddedColumns()---")
    return df1.reindex(columns=df2.columns, fill_value=0)


if __name__ == "__main__":
    print(joinLikeAdd())
    print(addWithFill())
    print(reindexWithAddedColumns())
