import pprint

path = 'example.txt'

def readLines(filePath):
    f = open(filePath)

    for line in f:
        print(line)

    f.close()

def readAndClean(filePath):
    lines = [line.rstrip() for line in open(filePath)]

    # print(lines) # prints array horizontally on one line
    pprint.pprint(lines) # prints each array entry on newline

'''
Performs autoclose of file
'''
def tryWithResources(filePath):
    with open(filePath) as f:
        lines = [line.rstrip() for line in f]

        #closes file upon exiting 'with' block.

if __name__ == '__main__':
    readLines(path)
    readAndClean(path)