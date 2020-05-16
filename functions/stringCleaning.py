import re

# List to represent data entries (such as Excel sheets by business stakeholders)
# Typically feautures non-uniform, erroneous entries
stringList = ['Alabama', 'Georgia!', 'georgia', 'FlOrida', 'south carolina##', 'West virginia?']

def stripDemo(entry):
    return entry.strip()

def regExpSubPunctuation(entry):
    result = re.sub('[!]','',entry)
    return result

def regExpSubNumbers(entry):
    result = re.sub('[#]','',entry)
    return result

def regExpSubQ(entry):
    result = re.sub('[?]','',entry)
    return result

def regExpSubAll(entry):
    result = re.sub('[!#?]','',entry)
    return result

def titleFormat(entry):
    return entry.title()

def cleanStrings(strings):
    result = []
    for value in strings:
        print("Starting value: {}".format(value))
        value = value.strip()
        print('After strip(): {}'.format(value))
        value = re.sub('[!#?]', '', value)
        print('After re.sub("[!#?]", "", value): {}'.format(value))
        value = value.title()
        print('After title(): {}'.format(value))
        result.append(value)
    return result

if __name__ == '__main__':
    print(cleanStrings(stringList))
    
    
