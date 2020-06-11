import pandas as pd
import numpy as np

series = pd.Series(np.arange(4.), index=['a','b','c','d'])

def getOriginalSeries(series=series):
    print("---getOriginalSeries()---")
    return series

def indexingAlternatives(series=getOriginalSeries()):
    print("---indexingAlternatives()---")
    print("series[0] =  {}".format(series[0]))
    print("series['a'] = {}".format(series['a']))
    print("series[1] =  {}".format(series[1]))
    print("series['b'] = {}".format(series['b']))
    print()
    print("series[1:4] =\n{}".format(series[1:4]))
    print("series[['b','c','d']] =\n{}".format(series[['b','c','d']]))
    print()
    print("series[[1,3]] =\n{}".format(series[[1,3]]))
    print("series[series < 2] =\n{}".format(series[series < 2]))

'''
Slicing with labels is unlike slicing in other Python data structures,
specifically that the end index ([:end]) is INCLUSIVE
'''
def slicingWithLabels(series=getOriginalSeries()):
    print("---slicingWithLabels()---")
    print("series['b':'c'] =\n{}".format(series['b':'c']))

def settingViaSlicing(series=getOriginalSeries()):
    print("---settingViaSlicing()---")
    series['b':'c'] = 100
    print("series['b':'c'] = 100\n{}".format(series))



if __name__ == "__main__":
    indexingAlternatives()
    slicingWithLabels()
    settingViaSlicing()