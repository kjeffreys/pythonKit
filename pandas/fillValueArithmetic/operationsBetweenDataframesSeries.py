'''
Similar operations exist between pandas Series and DataFrames 
as that of NumPy arrays with different dimensions
'''
import numpy as np
import pandas as pd

frame = pd.DataFrame(np.arange(12.).reshape((4,3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon']) 

'''
Taking arr1, arr1[0] = array([0.,1.,2.,3.]).
arr1 - arr1[0] performs subtraction once for each row, known as broadcasting
'''
def broadcastingSubtraction(df=frame, series=frame.iloc[0]):
    print("---broadcastingSubraction()---")
    print(df)
    print("-")
    print(series)
    print("-" * 40)
    return df-series

'''
If an index value is not found in either the DataFrame's colummns or the Series's index,
the objects will be reindexed to form the union
'''
def unfoundIndexValue(df=frame, series=pd.Series(range(3), index=['b','e','f'])):
    print("---unfoundIndexValue()---")
    print(df)
    print("+")
    print(series)
    print("-" * 40)
    return df+series

def broadcastingColumnWise(df=frame, series=frame['d']):
    print("---broadcastingColumnWise()---")
    print(df)
    print("-")
    print(series)
    print("-" * 40)
    return df.sub(series, axis='index') # OR axis = 0...equivalent methods to match along DF's row axis and broadcast across all columns

if __name__ == "__main__":
    print(broadcastingSubtraction())
    print(unfoundIndexValue())
    print(broadcastingColumnWise())