'''
Dropping one or more entries from an axis is easy if you already have an index array or list without those entries.
That can require data cleaning and set logic, and an alternative approach is to use the drop() method
and return a new object with the indcated value or values deleted from the axis.
'''
import sampleData as sd

def originalSeries(series=sd.series3):
    print("---originalSeries()---")
    return series

def dropRow(series=originalSeries()):
    print(series)
    print("---dropRow()---")
    newSeries = series.drop('c')
    return newSeries

def dropMultipleRows(series=originalSeries(), rows=['a', 'd', 'e']):
    print("---dropMultipleRows()---")
    newSeries = series.drop(rows)
    return newSeries

'''
For DataFrame, default args passed to drop() will drop rows

For columns, use axis=1 OR axis='columns'
'''
def dropColumn(dataFrame=sd.frame2):
    print("---original DataFrame---\n{}".format(dataFrame))
    print("---dropColumn()---")
    newDataFrame = dataFrame.drop('two', axis=1)
    # OR # newDataFrame = dataFrame.drop('two', axis='columns') 
    return newDataFrame

def dropMultipleColumns(dataFrame=sd.frame2):
    print("---dropMultipleColumns()---")
    newDataFrame = dataFrame.drop(['two', 'four'], axis='columns')
    # OR # newDataFrame = dataFrame.drop('two', axis=1) 
    return newDataFrame

def modifyInPlace(dataFrame=sd.frame2):
    print("---modifyInPlace()---")
    dataFrame.drop(['Ohio','Utah'], inplace=True)
    # OR # newDataFrame = dataFrame.drop('two', axis=1) 
    return dataFrame

if __name__ == "__main__":
    print(dropRow())
    print(dropMultipleRows())
    print(dropColumn())
    print(dropMultipleColumns())
    print(modifyInPlace())