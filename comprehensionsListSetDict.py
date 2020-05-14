'''
@author Kyle Jeffreys
Comprehensions allow user to evaluate an expression AND filter with elements of a collection
'''

exampleList = ['1', '22', '333', '4444', '666666']
'''
List comprehensions are a python language feature that allow a user
to form a new list by filtering the elements of a collection,
transforming the elements passing the filter in one concise expression.
Below is the basic form
'''
# Using list comprehension to filter for string > len(2)
def listComprehensionOne(exampleList):
    newList = [el.upper() for el in exampleList if len(el) > 2]

    print(newList)

'''
Doing the above method without list comprehension
'''
def nonComprehensionOne(exampleList):
    result = []
    for el in exampleList:
        if len(el) > 2:
            result.append(el.upper())

    print(result)

def setComprehensionOne(exampleList):
    lengthsAsSet = {len(x) for x in exampleList}

    print(lengthsAsSet)

def setMappingFunction(exampleList):
    functionalMappingToSet = set(map(len, exampleList))

    print(functionalMappingToSet)

def dictComprehensionOne(exampleList):
    locationMapping = {val : i for i,val in enumerate(exampleList)}

    print(locationMapping)

if __name__ == '__main__':
    listComprehensionOne(exampleList)
    nonComprehensionOne(exampleList)
    setComprehensionOne(exampleList)
    setMappingFunction(exampleList)
    dictComprehensionOne(exampleList)
    