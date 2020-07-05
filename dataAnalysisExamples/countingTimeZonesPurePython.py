import json
from collections import defaultdict
from collections import Counter
import pprint

path = 'D:/datasets/bitly_usagov/example.txt'
numRecords = 3560 # obtained from getNumRecords()

def getRecords():
    records = [json.loads(line) for line in open(path)]
    return records

def getNumRecords():
    print("---numRecords()---")
    records = [json.loads(line) for line in open(path)]
    return len(records)
'''
Extract a list of time zones using list comprehension.
NOTE: conditional resolves issue with mizzing 'tz' entries.
@param: numReturn - getTimeZones() will return the first < numReturn > timeZones
'''
def getTimeZones(numReturn=numRecords):
    print("---getTimeZones({})---".format(numReturn))
    # timeZones = [ rec['tz'] for rec in records ] # won't work b/c 'tz' is missing in some entries

    records = getRecords()

    timeZones = [rec['tz'] for rec in records if 'tz' in rec]

    return timeZones[:numReturn]

'''
Produces counts by time zone with a dict to store counts while iterating
through timeZones. This is a longer way using just Python standard library.
'''
def getCounts1(sequence):
    print("---getCounts1()---")
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def getCounts2(sequence):
    print("---getCounts2()---")
    counts = defaultdict(int) # values will initialize to 0

    for x in sequence:
        counts[x] += 1
    return counts

def topCounts(countDict=getCounts2(getTimeZones()), n=10):
    print("---topCounts()---")
    valueKeyPairs = [(count, tz) for tz, count in countDict.items()]
    valueKeyPairs.sort()
    return valueKeyPairs[-n:]

def usingCollectionsCounter():
    print("---usingCollectionsCounter()---")
    counts = Counter(getTimeZones())
    return counts.most_common(10)

if __name__ == "__main__":
    pprint.pprint(getTimeZones(10))
    pprint.pprint(getCounts1(getTimeZones()))
    pprint.pprint(getCounts2(getTimeZones()))
    #print(getNumRecords())

    # timeZones(3440) < records (3560), b/c 'tz' not in records[emptyIndex]
    pprint.pprint(len(getTimeZones()))
    
    pprint.pprint(topCounts())

    pprint.pprint(usingCollectionsCounter())