import json
import pandas as pd

obj = '''
{"name": "Wes",
 "placesLived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
 {"name": "Katie", "age": 38, "pets": ["sixes", "Stache", "Cisco"]}]
}
'''

def originalJson():
    print("---originalJson()---")
    return obj

'''
Converts the JSON string into Python dict of dicts
'''
def getPythonObj(pyObj=obj):
    print("---getPythonObj()---")
    result = json.loads(pyObj)
    print(result)
    print("=" * 70)
    return result

def workingWithJsonLoadsObj():
    print()
    print("---workingWithJsonLoadsObj()---")
    newDictObj = getPythonObj()

    for k in newDictObj:
        print("{}: {}".format(k, newDictObj[k]))

'''
You can pass a list of dicts (which were previously nested JSON objs in this case)
to the DataFrame constructor and select a subset of the data fields.
'''
def getSiblings():
    print("---getSiblings()---")
    result = json.loads(obj)
    df = pd.DataFrame(result['siblings'], columns=['age', 'name'])
    return df


if __name__ == "__main__":
    print(originalJson())
    print(getPythonObj())
    workingWithJsonLoadsObj()
    print(getSiblings())