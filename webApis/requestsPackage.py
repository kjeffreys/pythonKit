'''
Issues came up when using pandas.read_html() due to encoding differences between unicode and ascii 
(namely negative numbers '-' symbol was not recognized). Instead of dealing with encoding/decoding/re.sub()
fixes, it is also possible to get around issues with the requests package.
'''
import pandas as pd
import requests

'''
This method displays a query usings the requests package to find
the last 30 GitHub issues for pandas and Github with a 'GET' http request
'''
def last30Pandas():
    # requests limit already reached, problem with repo?
    url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

    resp = requests.get(url)

    # resp.json() returns a dictionary containing JSON parsed into native Python objects
    data = resp.json()

    for i in range(30):
        print("=" * 75)
        print("Issue {}:".format(i))
        print("=" * 75)
        print(data[i]['title'])

    return data

'''
Each elements in the data from the requests query above is a dictionary containing
all of the data found on a GitHub issue page (except for the comments). This can
be passed directly to a DataFrame and subsequently fields of interest can be extracted.
'''
def extractFields():
    issues = pd.DataFrame(last30Pandas(), columns=['number','title','labels','state'])

    return issues

if __name__ == "__main__":
    #print(last30Pandas())
    print(extractFields())