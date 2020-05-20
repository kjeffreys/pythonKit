
someDict = {'a':1, 'b':2, 'c':3}

def generator1(n=10):
    print('Generating squares from 1 to {}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2

if __name__ == '__main__':
    for key in someDict: print(key)
    print('asList: ' + str(list(someDict)))
    print('asSet: ' + str(set(someDict)))
    print('asTuple: ' + str(tuple(someDict)))
    print()

    squares = generator1()
    for x in squares:
        print(x, end = ' ')

