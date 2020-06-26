import numpy as np
import pandas as pd

data = pd.Series([1., -999.,2.,-999.,-1000.,3.])

def replaceNA(series=data):
    print("---replaceNA()---")
    print("Original Series:")
    print(series)
    print("series.replace(-999, np.nan)")
    print(series.replace(-999, np.nan))
    print("series.replace([-999,-1000], np.nan)")
    print(series.replace([-999,-1000], np.nan))
    print("series.replace([-999,-1000], [np.nan, 0])")
    return series.replace([-999,-1000], [np.nan, 0])

def replaceDict(series=data):
    print("---replaceDict()---")
    print("Original Series:")
    print(series)
    print("series.replace({-999: np.nan, -1000: 0})")
    print(series.replace({-999: np.nan, -1000: 0}))


if __name__ == "__main__":
    print(replaceNA())
    replaceDict()