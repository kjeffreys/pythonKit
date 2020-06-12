'''
This file shows how various NumPy ufunc (element-wise array methods)
work with pandas objects
'''
import numpy as np
import pandas as pd

frame = pd.DataFrame(np.random.randn(4,3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

def absVal(df=frame):
    print("---absVal()---")
    print("Original df:\n{}\n".format(df))
    return np.abs(df)

'''
A frequent operation is applying a function on 1-D arrays to each column/row.
For pd.DataFrame, this can be done with the apply() method

In this example, the function "fn" is applied to each column of the dataframe passed to minMaxDiff()

The result is a Series having the frame's columns as its index.
'''
def minMaxDiff(df=frame):
    print("---minMaxDiff()---")
    print("Original df:\n{}\n".format(df))

    fn = lambda x: x.max() - x.min()

    return frame.apply(fn)

'''
Same function as above but passing axis='columns' to apply the function
once per row instead of per column
'''
def minMaxDiffRows(df=frame):
    print("---minMaxDiffRows()---")
    print("Original df:\n{}\n".format(df))

    fn = lambda x: x.max() - x.min()

    return frame.apply(fn, axis='columns')

'''
The function applied to a DataFrame.apply() does not need to return a scalar value;
it can also return a series with multiple values.
'''
def minMaxColumns(df=frame):
    print("---minMaxColumns()---")
    print("Original df:\n{}\n".format(df))

    fn = lambda x: pd.Series([x.min(), x.max()], index=['min', 'max'])

    return frame.apply(fn)

'''
Apply a formatting string to each floating-point value in frame
(element-wise python function)

NOTE: 
pd.DataFrame.applymap()-
Apply a function to a Dataframe elementwise.
This method applies a function that accepts and returns a scalar to every element of a DataFrame.
'''
def hundredthsPlace(df=frame):
    print("---hundredthsPlace()---")
    print("Original df:\n{}\n".format(df))

    format = lambda x: '%.2f' % x

    return frame.applymap(format)


if __name__ == "__main__":
    print(absVal())
    print(minMaxDiff())
    print(minMaxDiffRows())
    print(minMaxColumns())
    print(hundredthsPlace())