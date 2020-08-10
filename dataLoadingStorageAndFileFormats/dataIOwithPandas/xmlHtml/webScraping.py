import math
import numpy as np
import pandas as pd
import re

stockHtmlPath = 'D:/dataFile/NASDAQ100.html'

'''
The html file downloaded from Wikipedia has 7 tables:
['Record values', 'Annual Returns', 'Components', 'Companies of the NASDAQ-100 index',
 'Nasdaq, Inc.', 'Major United States stock market indices', 'Major American stock market indices']
'''
def readHtml():
    tables = pd.read_html(stockHtmlPath)

    print(len(tables))
    
    for i, table in enumerate(tables):
        print("Table[{}] head:".format(i))
        print(table.head())
    return 1

def maxChangeHtml():
    print("---maxChangeHtml()---")
    tables = pd.read_html('NASDAQ-100 - Wikipedia.html')
    print(tables[1])
    tables[1].columns = ['one,','two','three','annual percentage diff']
    series = tables[1].iloc[:, [0,3]]
    print(series)
    fn = lambda x: re.sub(r'[^\x00-\x7F]+', '-', str(x))

    tables[1]['annual percentage diff'].apply(fn)
    series = pd.Series(tables[1].iloc[:, 3]).astype('float64')
    print("sorting series...")
    print()
    print()
    print(series)
    print()
    print()
    print(tables[1].iloc[:,3])

    print(tables[1].sort_values(by='annual percentage diff'))
    print(series.sort_values(by='annual percentage diff', ascending=True))

if __name__ == "__main__":
    readHtml()
    maxChangeHtml()