import csv
import pandas as pd
from myDialect import myDialect
import os

f1 = 'csvFiles/myData.csv'

def writeCsv(f1=f1):
    with open(f1, 'w') as f:
        writer = csv.writer(f, dialect=myDialect)
        writer.writerow(('one','two','three'))
        writer.writerow(('1','2','3'))
        writer.writerow(('4','5','6'))
        writer.writerow(('7','8','9'))

if __name__ == "__main__":
    writeCsv()
    for file in os.walk('./csvFiles/'):
        print(file)
