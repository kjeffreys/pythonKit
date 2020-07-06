import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

path = 'D:/datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]
df = pd.DataFrame(records)
numberOfTimeZones = 3440

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
    aggCounts[aggCounts == ''] = 'Unknown'
    return aggCounts

'''
Extends isWindows() to also select top time zones among aggCounts
'''
def topTimeZones(numResults=10):
    indexer = isWindows().sum(1).argsort()

    return indexer[:numResults]

'''
Using "take" to select the rows in that order, then slicing off the last
10 rows(largest values)
'''
def pandasLargest1():
    print("---pandasLargest1()---")
    aggCounts = isWindows()
    indexer = topTimeZones(numberOfTimeZones)
    countSubset = aggCounts.take(indexer[-10:])
    return countSubset

'''
pandas has a convenience method called nlargest that performs the same
opearation as pandasLargest1()
'''
def pandasLargest2():
    print("---pandasLargest2()---")
    aggCounts = isWindows()
    return aggCounts.sum(1).nlargest(10)

def norm_total(group):
    group['normed_total'] = group.total / group.total.sum()
    return group

def stackedBarPlot():
    countSubset = pandasLargest1().stack()
    countSubset.name = 'total'
    countSubset = countSubset.reset_index()
    print("countSubset[:10]...\n{}".format(countSubset[:10]))
    sns.barplot(x='total', y='tz', hue='os', data=countSubset)
    plt.show()

    # Previous plot is not easy to see relative % of Windows users in
    # smaller groups, so the following normalizes the group %s to sum to 1
    results = countSubset.groupby('tz').apply(norm_total)
    sns.barplot(x='normed_total', y='tz', hue='os', data=results)
    plt.show()


if __name__ == "__main__":

    #print(df.info())
    #print(df['tz'][:10])
    #print(cleanData1())
    #print(visualizeSubset())
    agentFieldStats()
    #print(isWindows())
    print(topTimeZones())
    print(pandasLargest1())
    print(pandasLargest2())
    stackedBarPlot()
