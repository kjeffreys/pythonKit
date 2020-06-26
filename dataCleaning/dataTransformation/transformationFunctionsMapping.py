import pandas as pd

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                        'corned beef', 'Bacon', 'pastrami', 'honey ham',
                        'nova lox'], 'ounces': [4,3,12,6,7.5,8,3,5,6]})

def origData(df=data):
    return df

'''
Adding a column to indicate the type of animal that each food is from.
'''
def meatByAnimal(df=data):
    print("---meatByAnimal()---")
    print("Original df:")
    print(df)
    meatToAnimal = {
        'bacon': 'pig',
        'pulled pork': 'pig',
        'pastrami': 'cow',
        'corned beef': 'cow',
        'honey ham': 'pig',
        'nova lox': 'salmon'
    }

    lowercaseDF = df['food'].str.lower()

    df['animal'] = lowercaseDF.map(meatToAnimal)
    print("Lowercased and mapped by animal source")
    return df

def mbaComprehension(df=data):
    print("---mbaComprehension()---")
    print("Original df:")
    print(df)
    meatToAnimal = {
        'bacon': 'pig',
        'pulled pork': 'pig',
        'pastrami': 'cow',
        'corned beef': 'cow',
        'honey ham': 'pig',
        'nova lox': 'salmon'
    }

    print("Lowercased and mapped by animal source")
    return df['food'].map(lambda x: meatToAnimal[x.lower()])

if __name__ == "__main__":
    #print(meatByAnimal())
    print(mbaComprehension())
