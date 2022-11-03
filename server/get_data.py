import json
import urllib
from urllib.parse import urljoin, urlencode
import requests as r
import pandas as pd
import websocket
import datetime
import time



BASE_URL = 'https://fapi.binance.com'
wss = f'wss://stream.binance.com:9443'

def get_all_symbols():
    response = urllib.request.urlopen(f'{BASE_URL}/fapi/v1/exchangeInfo').read()
    return list(map(lambda symbol: symbol['symbol'], json.loads(response)['symbols']))

def get_data_for_view(symbol, interval, limit):
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }

    url = urljoin(BASE_URL, '/fapi/v1/klines')
    response = r.request('GET', url, params=params).json()

    converted = pd.DataFrame(data=response, columns=['opentime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                     'Quote asset volume',
                                                     'NumberOfTrades', 'Taker buy base asset volume',
                                                     'Taker buy quote asset volume', 'Ignore']
                             , dtype=float)

    out = converted[['close','volume']].to_json(orient='records')[1:-1].replace('},{', '} {')

    return out

def get_btc_dom(interval,limit):
    params = {
        'symbol': 'BTCDOMUSDT',
        'interval': '4h',
        'limit': 100
    }

    url = urljoin(BASE_URL, '/fapi/v1/klines')
    response = r.request('GET', url, params=params).json()
    converted = pd.DataFrame(data=response, columns=['opentime', 'open', 'high', 'low', 'dom', 'volume', 'closeTime',
                                                     'Quote asset volume',
                                                     'NumberOfTrades', 'Taker buy base asset volume',
                                                     'Taker buy quote asset volume', 'Ignore']
                             , dtype=float)


    out = converted[['dom']].to_json(orient='records')[1:-1].replace('},{', '} {')


print(get_all_symbols())