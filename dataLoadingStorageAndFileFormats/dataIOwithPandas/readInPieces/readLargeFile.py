import pandas as pd

f1 = '../pandasRead/csvFiles/sp500excelToCsv.csv'

'''
For larget files, the pandas display settings can be made more compact
'''
def compactDisplay(f=f1, maxDisplay=10):
    print("---compactDisplay()---")
    pd.options.display.max_rows = maxDisplay
    df = pd.read_csv(f)
    return df

'''
The display.max_rows only affects the amount displayed, not the amount read.

To only read a portion of the file iteself, specify with "nrows" optional argument
'''
def readNumLines(f=f1, num=15):
    print("---readNumLines()---")
    pd.options.display.max_rows = num # was still set to 6 from call with maxDisplay=6
    df = pd.read_csv(f1, nrows=num)
    return df

def readChunks(f=f1, chunksize=100):
    print("---readChunks()---")
    df = pd.read_csv(f, chunksize=chunksize)
    return df

'''
The TextFileReader object returned by read_csv (<pandas.io.parsers.TextFileReader object at 0x0000015D73D48CB4>)
can be used to iterate over the file according to the chunksize.
'''
def iterateChunks():
    chunker = readChunks()
    agg = pd.Series([])
    for piece in chunker:
        agg = agg.add(piece['Symbol'].value_counts(), fill_value=0)
    agg = agg.sort_values(ascending=False)

    return agg


if __name__ == "__main__":
    print(compactDisplay())
    print(compactDisplay(maxDisplay=6))
    print(readNumLines())
    print(readChunks())
    print(iterateChunks())