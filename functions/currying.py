'''
Currying is a Computer Science term named after mathematician Haskell Curry.

Refers to deriving new functions from existing ones with partial argument application
'''
import functools

# base function
def addNumbers(x, y):
    return x + y

if __name__ == '__main__':
    addFive = lambda y: addNumbers(5, y)
    print(addFive(10))

    addSix = functools.partial(addNumbers, 6)
    print(addSix(10))