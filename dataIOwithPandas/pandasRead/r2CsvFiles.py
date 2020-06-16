import pandas as pd

f1 = 'csvFiles/whiteSpace.csv'
f2 = 'csvFiles/skipRows.csv'
f3 = 'csvFiles/missingValues.csv'

'''
The table in file f1 does not have a fixed delimeter, using whitespace to separate fields.

Since the fields are separated by a variable amount of whitespace, the following function
passes a regular expression (\s+) as a delimeter for read_csv.

Because there is one fewer column name than the number of data rows, read_csv infers that
the first column should be the DataFrame's index in this special case.
'''
def regExpDelimeter(f=f1, delimeter='\s+'):
    print("---regExpDelimeter()---")
    df = pd.read_csv(f, sep=delimeter)
    return df

def skipRowsRead(f=f2, rows=[0,2,3]): # removes rows with comments
    print("---skipRowsRead()---")
    df = pd.read_csv(f, skiprows=rows)
    return df

'''
NOTE: File creates NaN entries in the df in two ways.
'NA' -> NaN
'val,,val' (empty space b/w commas) -> NaN
'''
def missingValuesRead(f=f3):
    print("---missingValuesRead()---")
    df = pd.read_csv(f)
    return df

def booleanOp(f=f3):
    print("---booleanOp()---")
    df = pd.read_csv(f)
    return pd.isnull(df)

'''
In addition to NA and empty csv entries, read_csv can take a list or set of string to
consider as missing values
'''
def badValues(f=f3, missingVals=['NULL']):
    print("---badValues()---")
    df = pd.read_csv(f, na_values=missingVals)
    return df

'''
Differnt "N/A" sentinels can be specified for each column in a dict
'''
def sentinelsRead(f=f3):
    print("---sentinelsRead()---")
    sentinels = {'message': ['foo', 'NA'], 'something': ['two'] }
    df = pd.read_csv(f, na_values=sentinels)
    return df

if __name__ == "__main__":
    print(list(open(f1)))
    print(regExpDelimeter())
    print(skipRowsRead())
    print(missingValuesRead())
    print(booleanOp())
    print(badValues())
    print(sentinelsRead())

'''
Other frequently used read options in pandas.read_csv()
============================================================================================
Argument------------Description-------------------------------------------------------------
============================================================================================
path                String indicating filesystem location, URL, or file-like obj
============================================================================================
sep OR              Character sequence or regular expression to use to split fields in each
delimeter           row.
============================================================================================
header              Row number to use as column names; defaults to 0 (first row), but should
                    be None if there is no header row
============================================================================================
index_col           Column numbers or names to use as the row index in the result; can be
                    a single name/number or a list of them for a hierarchical index
============================================================================================
names               List of column names for the result, combine with header=None
============================================================================================
skiprows            Number of rows at beginning of file to ignore OR a list of row numbers
                    to skip
============================================================================================
na_values           Sequence of values to replace with NA.
============================================================================================
comment             Character(s) to split comments off the end of lines
============================================================================================
parse_dates         Attempt to parse data to datetime; False by default. If True, will
                    attempt to parse all columns. Otherwise can specify a list of column
                    numbers or name to parse. If element of list is tuple or list, will 
                    combine multiple columns together and parse to date.
                    (e.g. if date/time split across two columns)
============================================================================================
keep_date_col       If joining columns to parse date, keep the joined columns. False by
                    default.
============================================================================================
converters          Dict containing column number of name mapping to functions.
                    e.g. {'foo': f} would apply the function f to all values in the 'foo'
                    column.
============================================================================================
dayfirst            When parsing potentially ambiguous dates, treat as international format
                    e.g. 7/6/2012 -> June 7, 2012. False by default.
============================================================================================
date_parse          Function to use to parse dates
============================================================================================
nrows               Number of rows to read from beginning of the file
============================================================================================
iterator            Return a TextParser object for reading file piecemeal
============================================================================================
chunksize           For iteration, size of file chunks
============================================================================================
skip_footer         Number of lines to ignore at end of file.
============================================================================================
verbose             Print various parser output information, like the number of missing
                    values placed in non-numeric columns.
============================================================================================
encoding            Text encoding for Unicode, e.g. 'utf-8' for UTF-8 encoded text
============================================================================================
squeeze             If the parsed data only contains one column, return a Series.
============================================================================================
thousands           Separator for thousands, e.g. ',' or '.' in currency
============================================================================================
'''