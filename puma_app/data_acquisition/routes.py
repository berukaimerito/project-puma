import config
from extension import *

client = Client(config.API_KEY, config.API_SECRET)  

data_acquisiton = Blueprint('data_acquisition', __name__)

@data_acquisiton.route("/history")
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def history():
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, limit=100)

    processed_candlestick = []
    for data in candlesticks:
        candlestick = {
            'time':  data[0] /1000,
            'open': data[1],
            'high': data[2],
            'low': data[3],
            'close': data[4]
        }
        processed_candlestick.append(candlestick)
    return jsonify(processed_candlestick)