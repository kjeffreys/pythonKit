
path = 'example.txt'

def readTen(filePath):
    f = open(filePath)

    print("f.read(10): {}".format(f.read(10)))

    print("f.tell(): {}".format(f.tell()))
    print()
    f.close()

def readTenBinary(filePath):
    f = open(filePath, 'rb')

    print("f.read(10): {}".format(f.read(10)))

    print("f.tell(): {}".format(f.tell()))
    print()

    f.close()

'''
Python has the read, seek, and tell like C.
'''
def seekAndRead(filePath):

    with open(filePath) as f:
        print("f.seek(5): {}".format(f.seek(5)))
        print("f.read(10): {}".format(f.read(10)))

if __name__ == '__main__':
    readTen(path)
    readTenBinary(path)
    seekAndRead(path)