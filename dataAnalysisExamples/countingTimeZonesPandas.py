import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

path = 'D:/datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]
df = pd.DataFrame(records)

def cleanData1():
    print("---cleanData1()---")
    cleanTZ = df['tz'].fillna('Missing')
    cleanTZ[cleanTZ == ''] = 'Unknown'
    tzCounts = cleanTZ.value_counts()
    return tzCounts

def visualizeSubset(setSize=10):
    cleanTZ = df['tz'].fillna('Missing')
    cleanTZ[cleanTZ == ''] = 'Unknown'
    tzCounts = cleanTZ.value_counts()
    subset = tzCounts[:10]

    sns.barplot(y=subset.index, x=subset.values)
    # matplotlib required to display seaborn plot
    plt.show()
    return subset

'''
Parsing info and getting stats about the 'agent'
field describing browsers. Listed in this dataset as 'a'
'''
def agentFieldStats():
    #getting first token in 'a' strings
    results = pd.Series([x.split()[0] for x in df.a.dropna()])
    print("results[:5]...\n{}".format(results[:5]))
    print("results.value_counts()[:8]...\n{}".format(results.value_counts()[:8]))

'''
Decomposing the top time zones into Windows and non-Windows users
by asserting that a user is on Windows if 'Windows' is in the agent string.
'''
def isWindows():
    cframe = df[df.a.notnull()]

    # compute a value for whether each row is Windows or not
    cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows',
                    'Not Windows')

    print("cframe['os'][:5]...\n{}".format(cframe['os'][:5]))

    # group the data by time zone column and the new list of OS
    byTzOs = cframe.groupby(['tz', 'os'])

    # group counts, analagous to value_counts(), can be computed with size()
    # NOTE: unstack() reshapes the data into a table
    #aggWithoutUnstack = byTzOs.size().fillna(0)
    #print(aggWithoutUnstack)

    aggCounts = byTzOs.size().unstack().fillna(0)
    return aggCounts

if __name__ == "__main__":

    #print(df.info())
    #print(df['tz'][:10])
    #print(cleanData1())
    #print(visualizeSubset())
    agentFieldStats()
    print(isWindows())
