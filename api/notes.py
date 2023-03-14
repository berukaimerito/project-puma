# def get_ticker(symbol, interval):
#
#
#
#     client = Client(config.API_KEY, config.API_SECRET)
#     one_min = Client.KLINE_INTERVAL_1MINUTE,
#     thirty_min = Client.KLINE_INTERVAL_30MINUTE
#
#
#     # store it in a own dictionary as keys: values , as keys being ofc {ticker_symbol} and v beign JSON? or just candlestick object.
#     candlesticks = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, limit=100)
#
#     processed_candlestick = []
#     for data in candlesticks:
#         candlestick = {
#             'time': data[0] / 1000,
#             'open': data[1],
#             'high': data[2],
#             'low': data[3],
#             'close': data[4]
#         }
#         processed_candlestick.append(candlestick)
#
#         # method to save in db.Ticker.TimeSeries[]
#
#     return processed_candlestick
