'''
Some files with tabular data may require manual processing.

The following methods can be useful when retrieving a file
with malformed lines that corrupt read_csv.
'''
import csv # NOTE: python's built-in csv.reader

f1 = 'csvFiles/example.csv'

def readCsv():
    f = open(f1) 
    reader = csv.reader(f)

    # Iterating through the reader like a file yields tuples of values
    # with any quote characters removed:
    for line in reader:
        print(line)

'''
Read csv file into list of lines to process
'''
def getLines():
    with open(f1) as f:
        lines = list(csv.reader(f))
    return lines
'''
Split lines into header line and the data lines
'''
def splitLines():
    lines = getLines()
    header, values = lines[0], lines[1:]
    return [header, values]

'''
Create a dictionary of data columns using a dictionary
comprehension and the expression: zip(*values),
which transposes rwos to columns
'''
def makeDictionary():
    header, values = splitLines()

    dataDict = {h : v for h, v in zip(header, zip(*values))}

    return dataDict


if __name__ == "__main__":
    readCsv()
    print(makeDictionary())
