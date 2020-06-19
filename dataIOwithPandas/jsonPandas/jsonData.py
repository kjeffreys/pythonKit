from config import *
import alpaca_trade_api as tradeapi
import json
import numpy as np
import pandas as pd

def updateMarch():
    api = tradeapi.REST(API_KEY, SECRET_KEY, api_version='v1')
    params={'apiKey' : api.polygon._api_key}
    myTickers = ['A', 'AA', 'BA', 'BAC', 'JPM', 'Z', 'ZTS']
    stockListOfDicts = []
    stockDict = {}

    for i,v in enumerate(myTickers):
        myURL = 'https://api.polygon.io/v1/open-close/{}/{}'.format(v, '2020-03-20')
        resp = api.polygon._session.request('GET', myURL, params=params)

        jjson = resp.json() # json method on response of requests library already converts to a string, not a json object 
        print(jjson)
        print()
        #temp = json.dumps(jjson)
        #print(temp)
        stockDict[ jjson['symbol'] ] = jjson
        stockListOfDicts.append(jjson)
    
    for k, v in enumerate(stockDict):
        print(k, v)

    print(stockDict.keys())
    print(stockDict.values())
    print()

    stocks = pd.DataFrame(stockListOfDicts)
    #stocks.reindex(['columns'])
    print(stocks)
    print()
    return stocks.reindex(columns=['symbol', 'from', 'open', 'high', 'low', 'close', 'volume', 'afterHours', 'preMarket'])

'''
The pandas.read_json can automatically convert JSON datasets in specific arrangements into a Series or DataFrame.
'''
def usingPandasDotReadJson():
    api = tradeapi.REST(API_KEY, SECRET_KEY, api_version='v1')
    params={'apiKey' : api.polygon._api_key}
    myTickers = ['A', 'AA', 'BA', 'BAC', 'JPM', 'Z', 'ZTS']
    frames = []
    stockDict = {}
    frames = pd.DataFrame()

    for i, v in enumerate(myTickers):
        myURL = 'https://api.polygon.io/v1/open-close/{}/{}'.format(v, '2020-03-20')
        resp = api.polygon._session.request('GET', myURL, params=params)

        jsonRes = resp.json()
        if i == 0:
            df = pd.DataFrame(jsonRes,index=[i], columns=['symbol', 'high', 'from'])
            print(df)
        else:
            df2 = pd.DataFrame(jsonRes,index=[i], columns=['symbol', 'high', 'from'])
            print(df2)
            frames.append(df2, ignore_index=True)
            print("=" * 75)
            print(frames)

    return

def useDictForDataFrame():
    api = tradeapi.REST(API_KEY, SECRET_KEY, api_version='v1')
    params={'apiKey' : api.polygon._api_key}
    myTickers = ['A', 'AA', 'BA', 'BAC', 'JPM', 'Z', 'ZTS']
    listOfDicts = []

    for i, v in enumerate(myTickers):
        myURL = 'https://api.polygon.io/v1/open-close/{}/{}'.format(v, '2020-03-20')
        resp = api.polygon._session.request('GET', myURL, params=params)

        jjson = resp.json() # json method on response of requests library already converts to a string, not a json object 
        print(jjson)
        pyObj = json.loads(json.dumps(jjson)) # identity like conversion to show request library .json() method converts to python obj
        listOfDicts.append(pyObj)

    df = pd.DataFrame(listOfDicts)
    print(df)

    df2 = df
    df2.index = df['symbol']
    del df2['status']
    return df2
        


if __name__ == "__main__":
    #print(updateMarch())
    #print(usingPandasDotReadJson())
    print(useDictForDataFrame())