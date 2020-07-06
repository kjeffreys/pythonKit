import json

path = 'D:/datasets/bitly_usagov/example.txt'

# read/print first line of example.txt
def getFirstLine():
    print("---getFirstLine()---")
    line = open(path).readline()
    return line

'''
Reads the records within example.txt.
@return - record at index argument
'''
def recordsAtIndex(index=0):
    print("---recordsAtIndex({})---".format(index))
    # NOTE: able to use json even though it is reading a text file
    # NOTE: like .json, only works if the example.txt has valid json content
    records = [json.loads(line) for line in open(path)]

    return records[index]

if __name__ == "__main__":
    print(getFirstLine())
    print(recordsAtIndex())
    print(recordsAtIndex(1))

