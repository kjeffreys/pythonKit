'''
File on NaN / null values propagated in pandas Series when there is no value for an assigned index
'''
import pandas as pd

dictionary = {'California':40000000, 'Texas': 29000000, 'Florida': 22000000, 'New York':19000000}

def nullValueFill(dictionary=dictionary):
    print("---nullValueFill()---")
    series = pd.Series(dictionary, index=['California', 'Florida', 'Georgia', 'Illinois', 'New York', 'Pennsylvania', 'Texas'])

    return series

def nullFunctions(dictionary=dictionary):
    print("---nullFunctions()---")
    series = pd.Series(dictionary, index=['California', 'Florida', 'Georgia', 'Illinois', 'New York', 'Pennsylvania', 'Texas'])
    print("---pd.isnull(series):---")
    print(pd.isnull(series))
    print("---pd.notnull(series):---")
    print(pd.notnull(series))
    print("---series.isnull():---")
    print(series.isnull())

if __name__ == "__main__":
    print(nullValueFill())
    print(nullFunctions())
