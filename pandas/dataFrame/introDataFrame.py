'''
A DataFrame represents a rectangular table of data and contains ordered collection of columns.

Comparable to a table or a dict of Series
'''
import pandas as pd
import numpy as np

# dict used to construct a pd.DataFrame()
sample = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2] }

def createDataFrame(sample=sample):
    print("---createDataFrame()---")
    frame = pd.DataFrame(sample)

    return frame

def getFirstFive(frame=createDataFrame()):
    print("---getFirstFive()---")

    return frame.head()

def reorderColumns(sample=sample):
    print("---reorderColumns()---")

    return pd.DataFrame(sample, columns=['year', 'state', 'pop'])

def addNullColumn(sample=sample):
    print("---addNullColumn()---")
    frame = pd.DataFrame(sample, columns=['year', 'state', 'pop', 'debt'], 
                            index=['one', 'two', 'three', 'four', 'five', 'six'])

    return frame

'''
Get column with dict-like notation
'''
def getColumnV1(frame=addNullColumn()):
    print("---getColumnV1()---")

    return frame['state']

'''
Get column with attribute of the DataFrame obj
'''
def getColumnV2(frame=addNullColumn()):
    print("---getColumnV2()---")

    return frame.year

def getRow(frame=addNullColumn()):
    print("---getRow()---")

    return frame.loc['three'] # i.e. dataframeObj.loc[index name of row]

'''
Modify columns by assignment
'''
def updateColumn(frame=addNullColumn()):
    print("---updateColumn()---")

    frame['debt'] = 100

    return frame

def anotherColumnUpdate(frame=addNullColumn()):
    print("---anotherColumnUpdate()---")

    frame['debt'] = np.arange(6.)

    return frame



if __name__ == "__main__":
    print(createDataFrame())
    print(getFirstFive())
    print(reorderColumns())
    print(addNullColumn())
    print(getRow())
    print(updateColumn())
    print(anotherColumnUpdate())