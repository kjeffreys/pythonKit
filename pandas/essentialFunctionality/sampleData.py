import pandas as pd
import numpy as np

reindexing1 = pd.Series([4.5, 7.2, -5.3, 4.6], index=['d', 'b', 'a', 'c'])
reindexing2 = pd.Series(['blue', 'purple', 'yellow'], index=[0,2,4])
series3 = pd.Series(np.arange(5.), index=['a','b','c','d','e'])

frame1 = pd.DataFrame(np.arange(9).reshape((3,3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
frame2 = pd.DataFrame(np.arange(16).reshape((4,4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one','two','three','four'])





