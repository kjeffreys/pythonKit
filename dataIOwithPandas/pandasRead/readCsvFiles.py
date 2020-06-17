import pandas as pd

#fileRoot = 
f1 = "csvFiles/smallCsvFile.csv"
f2 = "csvFiles/sp500excelToCsv.csv"
f3 = "csvFiles/exampleCsv2.csv"
f4 = "csvFiles/multiIndex.csv"

'''
f1 and f2 are comma delimeted files, so they can be read with pandas.read_csv()

NOTE: For files larger than 5 rows, return df will only print a summary,
        i.e. Output: "head rows (5) ... tail rows (5)". 
                      [505 rows x 6 columns]
'''
def readFileIntoDataFrame(f=f1):
    print("---readFileIntoDataFrame()---")
    df = pd.read_csv(f)
    return df


'''
NOTE: Header=none will help with headerless csv files, but if used with csv files that have headers, the header
will be pushed down along with the other entries as if it is not a header.

NOTE: names= optional arg can be used to add headers to csv files without a header. It can also be used with 
        csv files that have a header, which will likely be an error pushing the intended headers down into the
        entries of the file.
'''
def readCsvHeaderOptions(f=f1, header=None):
    print("---readCsvHeaderOptions()---")
    # try None, names=['a','b','c','d','message']
    if header == None:
        df = pd.read_csv(f, header=None)
    else:
        df = pd.read_csv(f, names=header)
    return df

'''
Using the names=[...] argument from the previous function (see __main__ args), this function
returns a DataFrame where "message" column is the index of the returned DataFrame.
'''
def makeIndex(f=f3):
    print("---makeIndex()---")
    names=['a','b','c','d','message']
    df = pd.read_csv(f, names=names, index_col='message')
    return df

'''
To form a hierarchical index from multiple columns, pass a list of column numbers or names
'''
def hierarchicalIndex(f=f4):
    print('---hierarchicalIndex()---')
    df = pd.read_csv(f, index_col=['key1','key2'])
    return df

if __name__ == "__main__":
    print(readFileIntoDataFrame())
    print(readFileIntoDataFrame(f=f2))
    print(readCsvHeaderOptions()) # on csv WITH header row
    print(readCsvHeaderOptions(header=['a','b','c','d','message'])) # on csv WITH header row
    print(readCsvHeaderOptions(f=f3)) # on csv WITHOUT header row
    print(readCsvHeaderOptions(f=f3, header=['a','b','c','d','message'])) # on csv WITHOUT header row
    print(makeIndex())
    print(hierarchicalIndex())