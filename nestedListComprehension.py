allData = [ ['John', 'Emily', 'Michael', 'Mary', 'Steven'], ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
tupleList = [(1,2,3),(5,6,7), (10,11,12)]

def namesWithQualifier(listOfLists):
    namesQualified = []

    for names in listOfLists:
        moreThanTwoEs = [name for name in names if name.count('e') >= 2]

        namesQualified.extend(moreThanTwoEs)

    print(namesQualified)
    
    #return namesQualified

def nestedComprehensionConcise(listOfLists):
    result = [name for names in listOfLists for name in names if name.count('e') >= 2]

    print(result)

    #return result

def flattenListOfTuples(listOfTuples):
    flattened = [x for tup in listOfTuples for x in tup]

    print(flattened)

    #return flattened

def notFlattenedListOfLists(tupList):

    tupleToList = [ [x for x in tup] for tup in tupList ]
    print(tupleToList)

    #return tupleToList

if __name__ == '__main__':
    namesWithQualifier(allData)
    nestedComprehensionConcise(allData)
    flattenListOfTuples(tupleList)
    notFlattenedListOfLists(tupleList)