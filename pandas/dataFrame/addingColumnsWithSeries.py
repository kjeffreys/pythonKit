import introDataFrame as idf

'''
When assigning lists or arrays to a df column, the length must match the df length.

When assigning a Series, the lables will be realigned to match the df's index, and insert
missing values in the ordered position of the index
'''
series = idf.pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])

def addSeriesColumn(frame=idf.addNullColumn()):
    print("---addSeriesColumn()---")

    frame['eastern'] = frame.state == 'Ohio'

    return frame

def updateSeriesColumn(frame=addSeriesColumn(), series=series):
    print("---updateSeriesColumn()---")

    frame['debt'] = series

    return frame

def deleteSeriesColumn(frame=addSeriesColumn()):
    print("---deleteSeriesColumn()---")

    del frame['eastern']

    return frame

'''
Note: The column returned from indexing a DataFrame is a "view" (like numpy views)
on the underlying data, not a copy. Thus any in-place modifications to the Series
will be reflected in the original DataFrame. The column can be explicitly copied with the
Series .copy() method
'''
def showColumns(frame=deleteSeriesColumn()):
    print("---showColumns()---")

    return frame.columns

if __name__ == "__main__":
    print(addSeriesColumn())
    print(updateSeriesColumn())
    print(deleteSeriesColumn())
    print(showColumns())