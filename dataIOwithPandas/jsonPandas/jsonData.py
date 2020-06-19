from config import *
import alpaca_trade_api as tradeapi
import json
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
        #temp = json.dumps(jjson)
        #print(temp)
        stockDict[ jjson['symbol'] ] = jjson
        stockListOfDicts.append(jjson)
    
    for k, v in enumerate(stockDict):
        print(k, v)

    print(stockDict.keys())
    print(stockDict.values())

    stocks = pd.DataFrame(stockListOfDicts)
    #stocks.reindex(['columns'])
    print(stocks)
    return stocks.reindex(columns=['symbol', 'from', 'open', 'high', 'low', 'close', 'volume', 'afterHours', 'preMarket'])

if __name__ == "__main__":
    print(updateMarch())