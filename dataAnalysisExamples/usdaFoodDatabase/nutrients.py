'''
To analyze nutrient data, the nutrients for each food are being assembled into
a single large table. This requires multiple steps:
1) Convert each list of food nutrients to a DataFrame
2) Add a column for the food id
3) Append the DataFrame to a list
4) Concatenate the two DataFrames together
'''
import json
import matplotlib.pyplot as plt
import pandas as pd

dbPath = "D:/datasets/usda_food/database.json"
db = json.load(open(dbPath))

infoKeys = ['description', 'group', 'id', 'manufacturer']
info = pd.DataFrame(db, columns=infoKeys)

nutrients = []

for rec in db:
    fnuts = pd.DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)

nutrients = pd.concat(nutrients, ignore_index=True)

if __name__ == "__main__":
    print(nutrients)
    # check for duplicates
    numDuplicates = nutrients.duplicated().sum()
    print("duplicates: {}".format(numDuplicates))
    # drop duplicates
    nutrients = nutrients.drop_duplicates().dropna()
    print(nutrients)

    # renaming 2 DF objs to distinguish
    colMapping = {'description': 'food', 'group': 'fgroup'}
    info = info.rename(columns=colMapping, copy=False)
    print(info.info())

    colMapping = {'description': 'nutrient', 'group': 'nutgroup'}
    nutrients.rename(columns=colMapping, copy=False)

    print(nutrients)

    # made the 2 DF info and nutrients, now to merge (4)
    ndata = pd.merge(nutrients, info, on='id', how='outer')
    print(ndata.info())

    print("ndata.iloc[30000]")
    print(ndata.iloc[30000])

    # plot of median values by food group and nutrient type
    result = ndata.groupby(['fgroup'])['value'].quantile(0.5)

    result['Zinc, Zn'].sort_values().plot(kind='barh')

    plt.show()