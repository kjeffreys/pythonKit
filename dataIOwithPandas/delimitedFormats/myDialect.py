'''
CSV files can have a variety of formatting flavors. To define a new
format with a different: 
1) delimiter, 2) string quoting convention, or 3) line terminator,
define a subclass of csv.Dialect
'''
import csv
import pandas as pd

f = 'csvFiles/example.csv'

class myDialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL

if __name__ == "__main__":
    reader1 = csv.reader(f, delimiter="|")
    print(reader1)
    reader2 = csv.reader(f, dialect=myDialect)
    print(reader2)