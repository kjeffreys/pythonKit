'''
Like values in a Series, axis labels can be similarly transformed by a function
or mapping of some form to produce new, differently labeled objects. It is also
possible to modify the axes in-place without creating a new data structure
'''
import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado',
                    'New York'], columns=['one','two','three','four'])

transform = lambda x: x[:4].upper()

'''
Like a Series, axis indexes have a map method
'''
def transformIndex(df=data,transform=transform):
    print("---transformIndex()---")
    
    print("Orig:")
    print(df)
    print("data.index.map(transform):")
    return df.index.map(transform)

'''
Assigning to df.index will change the index in-place
(Does not require inplace=True option like other numpy/pandas methods)
'''
def assignToIndex(df=data, transform=transform):
    print("---assignToIndex()---")
    print("Orig:")
    print(df)
    print("df.index.map(transform)")
    df.index = df.index.map(transform)
    return df

'''
To created transformed version of dataset without modifying the original,
use rename()
'''
def transformWithoutModification(df=data, transform=transform):
    print("df.rename():\n{}".format(df.rename(index=str.title, columns=str.upper)))
    print("df:\n{}".format(df))

'''
Rename can be used in conjunction with a dict object providing new values for
a subset of the axis labels
'''
def renameForSubset(df=data, transform=transform):
    print("---renameForSubset()---")
    return df.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'})

def renameInPlace(df=data, transform=transform):
    print("---renameInPlace()---")
    return df.rename(index={'OHIO': 'INDIANA'}, inplace=True)

if __name__ == "__main__":
    print(transformIndex())
    print(assignToIndex())
    print(transformWithoutModification())
    print(renameForSubset())
    print(renameInPlace())