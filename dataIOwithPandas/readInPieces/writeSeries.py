import numpy as np
import pandas as pd
import sys

def writeSeries1():
    dates = pd.date_range('1/1/2000', periods=7)

    # create a TimeSeries
    ts = pd.Series(np.arange(7), index=dates,dtype=object)
    print(ts)
    ts.to_csv("csvFiles/tseries.csv")
    return ts.to_csv(sys.stdout)

if __name__ == "__main__":
    print(writeSeries1())