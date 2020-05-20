
def multBy3(x):
    return x * 3

def applyFnToList(exList, fn):
    return [fn(el) for el in exList]

def sortStringsWithLambdaKey():
    strings = ['aardvark', 'boar', 'cougar', 'dog', 'zebra', 'moose', 'chimpanzee', 'cheetah']
    print("preSort: " + str(strings))
    strings.sort(key=lambda x: len(set(list(x))))
    print("postSort: " + str(strings))

    # return dict comprehension mapping word -> len to better visualize the custom sort
    # remember that since keys are unique, if it is len -> word the dict will lose some of the values in the comprehension
    # (e.g. 'boar' is lost to 'moose' having 4 unique letters and taking the key)
    return { string : len(set(string)) for string in strings }
    

    

if __name__ == '__main__':
    num = 2
    print(multBy3(num)) # 6
    anon = lambda x: x * 3
    print(anon(num)) # 6
    print()

    print([anon(el) for el in list(range(10))]) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    print(applyFnToList(list(range(10)), anon)) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    print()

    print(sortStringsWithLambdaKey())
    print()
