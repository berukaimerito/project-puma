import urllib.request
import json
from urllib.parse import urljoin, urlencode
import requests as r



BASE_URL = 'https://fapi.binance.com/'
def get_historical_kline(symbol, interval):
        params = {
            'symbol': symbol,
            'interval': interval,
        }
        url = urljoin(BASE_URL, '/fapi/v1/klines')
        response = r.request('GET', url, params=params).json()
        processed_candlestick = []
        for data in response:
            candlestick = {
                'time': data[0] ,
                'open': data[1],
                'high': data[2],
                'low': data[3],
                'close': data[4]
            }
            processed_candlestick.append(candlestick)



        print((processed_candlestick))
        return processed_candlestick




def get_all_symbols():
    response = urllib.request.urlopen(f'{BASE_URL}/fapi/v1/exchangeInfo').read()
    return list(map(lambda symbol: symbol['symbol'], json.loads(response)['symbols']))



