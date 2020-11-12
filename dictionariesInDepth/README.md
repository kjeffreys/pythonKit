Quick lists vs dicts REVIEW:

lists - ordered collections of objects
dictionaries - unordered collection where items are stored and fetched by key, 
instead of by positional offset.

dictEx1 = {} # empty dict
dictEx2 = {'name': 'Bob', 'age': 40}
dictNested = {'cto': {'name': 'David', 'age': 44}}

dictAlternateConstruction = dict(name='Bob', age=40)
dictAlternateConstructionNest = dict( [ ('name', 'David'), ('age', 40) ])

dictZippedKeyValue = dict(zip(keyslist, valueslist))

dictCopyPartial = dict.fromkeys( ['name', 'age'] )

'key' in dictEx # boolean check

dictEx.keys()
dictEx.values()
dictEx.items()
dictEx.copy()
dictEx.clear()

# !!!!
dictEx.update(dict2) # merge by keys

dictEx.get(key, default?) # fetch by key, if absent default (or None)

dictEx.pop(key, default?) # remove/retrieve by key, if absent default (or error)

dictEx.setdefault(key, default?)
# e.g. when retrieving a value, get the value at the key, or the default value
# e.g. (cont'd) car = {"model": "Mustang"}
# e.g. (cont'd) x = car.setdefault("model", "Jeep")
# if model is a K-V entry in the dict, then x = car['model']
# if model is not a K-V entry in the dict, then x = "Jeep"
# likely use case is when populating values based on dictionary retrievals not known

