'''
A useful pd.Series feature is that index labels align for arithmetic

Series arithmetic is similar to a join on dB tables.
'''
import pandas as pd

dictionary = {'California':40000000, 'Texas': 29000000, 'Florida': 22000000, 'New York':19000000}
dict2 = {'California':40000000, 'Florida':22000000, 'Utah':3200000}

def addSeries(dict1=dictionary, dict2=dict2):
    print("---addSeries()---")
    series1 = pd.Series(dict1)
    series2 = pd.Series(dict2)

    return series1 + series2

def nameSeries(series=addSeries()):
    print("---nameSeries()---")
    series.name = 'Population'
    series.index.name = 'State'

    return series


if __name__ == "__main__":
    print(addSeries())
    print(nameSeries())