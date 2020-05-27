import itertools

firstLetter = lambda x: x[0]

names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']

for letter, names in itertools.groupby(names, firstLetter):
    print(letter, list(names))


'''
Error about itertools is inaccurate. Could not find problem online with pylint

Output:
A ['Alan', 'Adam']
W ['Wes', 'Will']
A ['Albert']
S ['Steven']

names - becomes the list of keys grouped into (i.e. names is the generator)
firstLetter - the key that forms determines the groupings in names
'''
