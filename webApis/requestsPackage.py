'''
Issues came up when using pandas.read_html() due to encoding differences between unicode and ascii 
(namely negative numbers '-' symbol was not recognized). Instead of dealing with encoding/decoding/re.sub()
fixes, it is also possible to get around issues with the requests package.
'''
import requests

'''
This method displays a query usings the requests package to find
the last 30 GitHub issues for pandas and Github with a 'GET' http request
'''
def last30Pandas():
    url = 'https://api/github.com/repos/pandas-dev/pandas/issues'

    resp = requests.get(url)

    # resp.json() returns a dictionary containing JSON parsed into native Python objects
    data = resp.json()

    for i, v in enumerate(data):
        print("Issues {}:".format(i))
        print(v['title'])

    return resp.headers

if __name__ == "__main__":
    print(last30Pandas())