import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# prices = client.get_all_tickers()

# for price in prices:
#     print(price)

#attributes end date , start date, symbol, interval
def get_historical_data():

    csvfile = open('15minutes.csv', 'w', newline='')
    candlestick_writer = csv.writer(csvfile, delimiter=',')

    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Nov, 2021", "1 Nov, 2022")

    for candlestick in  candlesticks:
        candlestick[0] = candlestick[0] / 1000
        candlestick_writer.writerow(candlestick)

    csvfile.close()

get_historical_data()