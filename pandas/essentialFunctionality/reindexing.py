import sampleData as sd

def getSeries(series= sd.reindexing1):
    print("---Original Series 1---")
    return series

'''
Calling reindex on the Series rearranges the data according to the new indexing
'''
def updateIndex(series=sd.reindexing1):
    print("---updateIndex()---")
    series = series.reindex(['a', 'b', 'c', 'd', 'e'])
    return series

'''
To perform interpolation or filling of values when reindexing, the method ffill
can forward fill values correlating to new index entries
'''
def updateFillIndex(series=sd.reindexing2):
    print("---Original Series 2---")
    print(series)
    print("---updateFillIndex()---")
    return series.reindex(range(6), method='ffill')

if __name__ == "__main__":
    print(getSeries())
    print(updateIndex())
    print(updateFillIndex())