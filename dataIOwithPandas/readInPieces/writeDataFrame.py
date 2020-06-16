import pandas as pd
import os
import sys

inFile = '../pandasRead/csvFiles/sp500excelToCsv.csv'
outFile = 'csvFiles/localSp500.csv'

'''
Write DataFrames to files with to_fileType()
'''
def writeDataFrame(inFile=inFile, outFile=outFile):
    print("---compactDisplay()---")
    df = pd.read_csv(inFile)

    # check if directory exists
    if not os.path.exists('csvFiles'):
        os.makedirs('csvFiles')
    
    df.to_csv(outFile)
    return df

def writeWithSeparators(inFile=inFile, sep='|'):
    print("---writeWithSeparators()---")
    df = pd.read_csv(inFile)
    
    return df.to_csv(sys.stdout, sep=sep)

'''
Missing values appear as empty strings ( entry1|entry2|||entry5) in the output.
They can be denoted by a different sentinel value
'''
def fillEmptyVals(inFile=inFile, sep='|'):
    print("---fillEmptyVals()---")
    df = pd.read_csv(inFile)
    
    return df.to_csv(sys.stdout, na_rep='NULL')

if __name__ == "__main__":
    print(writeDataFrame())
    print(writeWithSeparators())
    print(fillEmptyVals())