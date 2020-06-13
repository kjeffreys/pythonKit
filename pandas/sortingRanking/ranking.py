'''
Ranking assigns ranks from 1-N, where N is the number of valid data points in an array (along one axis)

NOTE: By default, equal values are assigned a rank that is the average of the ranks of those values.
'''
import numpy as np
import pandas as pd

series = pd.Series([7, -5, 7, 4, 2, 0, 4])

def showRank(series=series):
    print("---showRank()---")
    return series.rank()

'''
NOTE: Rank starts at 1, not 0
'''
def showRankExplainedFurther(orig=series):
    print("showRankExplainedFurther()---")
    series = showRank()
    df = pd.DataFrame({'element': orig, 'rank': series})
    print("These tuples show mappings between elements and their sorted (ranked) positions as (pos, element):")
    return df

if __name__ == "__main__":
    print(showRank())
    print(showRankExplainedFurther())