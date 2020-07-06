'''
The US Dept. of Agriculture makes available a db of food nutrient information.

The json file accessed for this information contains records for each food item,
with each food having a number of identifying attributes along with two lists
of nutrients and portion sizes.

The following program demonstrates the json formatting and does work to wrangle
the data into a more usable form.
'''
import json
import pandas as pd

dbPath = "D:/datasets/usda_food/database.json"
db = json.load(open(dbPath))

def getNutrients(entryNo=0):
    print("---getNutrients({})---".format(entryNo))
    nutrients = pd.DataFrame(db[entryNo]['nutrients'])
    return nutrients

def extraFieldSubset():
    print("---extraFieldSubset()---")
    infoKeys = ['description', 'group', 'id', 'manufacturer']
    info = pd.DataFrame(db, columns=infoKeys)
    print("info.info()")
    print(info.info())
    print("info[:5]")
    print(info[:5])

    # see the distribution of food groups with value_counts
    print("group counts (value_counts())")
    print(pd.value_counts(info.group)[:10])




if __name__ == "__main__":
    # number of records (foods)
    print(len(db))
    # keys of each food
    print(db[0].keys())
    # 'nutrients' is a list of dicts, one for each nutrient
    print(db[0]['nutrients'][0])
    print(getNutrients())
    print(extraFieldSubset())
