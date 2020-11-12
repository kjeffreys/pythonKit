import json
import pprint

jsonIndent = 4
jsonFP = "./requirementsGlossary.json"

def addRequirementsEntry(keyEntry="testKey", valueEntry="testValue"):
    '''
    glossary = {}
    glossary.update(loadGlossary())
    '''
    glossary = loadGlossary()
    print(glossary.items())
    glossary[keyEntry] = valueEntry
    print(glossary.items())
    print()
    
    with open(jsonFP, "w") as f:
        json.dump(glossary, f, indent=jsonIndent)

def updateRequirementsWithDict(dictArg={'dictSet_key1': 'dictSet_value1', 'dictSet_key2': 'dictSet_value2'}):
    
    glossary = loadGlossary()
    print(glossary.items())

    glossary.update(dictArg)
    print(glossary.items())

    with open(jsonFP, "w") as f:
        json.dump(glossary, f, indent=jsonIndent)


def loadGlossary(fp=jsonFP):
    with open(jsonFP, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    #addRequirementsEntry()
    updateRequirementsWithDict()