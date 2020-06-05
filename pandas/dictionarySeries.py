'''
Pandas Series behave like fixed-length, ordered dicts with a mapping of index values to data values.

A Series can be created from a dictionary.
'''
import pandas as pd

dictionary = {'California':40000000, 'Texas': 29000000, 'Florida': 22000000, 'New York':19000000}

def dictToSeries(dictionary=dictionary):
    print("---dictToSeries()---")
    series = pd.Series(dictionary)

    return series

def reorderKeysOnCreate(dictionary=dictionary):
    print("---reorderKeysOnCreate()---")
    series = pd.Series(dictionary, index=sorted(dictionary))

    return series

def nullValueFill(dictionary=dictionary):
    print("---nullValueFill()---")
    series = pd.Series(dictionary, index=['California', 'Florida', 'Georgia', 'Illinois', 'New York', 'Pennsylvania', 'Texas'])

    return series

def nullFunctions(dictionary=dictionary):
    print("---nullFunctions()---")
    series = pd.Series(dictionary, index=['California', 'Florida', 'Georgia', 'Illinois', 'New York', 'Pennsylvania', 'Texas'])
    print("pd.isnull(series):")
    print(pd.isnull(series))

if __name__ == "__main__":
    print(dictToSeries())
    print(reorderKeysOnCreate())
    print(nullValueFill())
    print(nullFunctions())
