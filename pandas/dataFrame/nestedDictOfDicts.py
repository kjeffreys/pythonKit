import pandas as pd

'''
If a nested dict is passed to DataFrame, pandas will interpret
the outer dict keys as the columns and the inner keys as the row indices.

Prevents the need to unpack and assign with for loops.
'''
population = {'Nevada': {2001: 2.4, 2002: 2.9, 2003: 3.4}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6} }

def nestedDictsToDF(data=population):
    print("---nestedDictsToDF()---")
    frame = pd.DataFrame(data)

    return frame

if __name__ == "__main__":
    print(nestedDictsToDF())