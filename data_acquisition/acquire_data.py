import config
from binance import Client
from celery import Celery


# import pulumi_cloudamqp as cloudamqp
#
# instance = cloudamqp.Instance("demo-instance",
#     plan="lemur",
#     region="amazon-web-services::us-west-2"
# )

## burada atadigimiz Celery objesi bir kutuphane

## simdi bunu api-routes da gizli ve hatta belki de admin rolunde
# @app.task() dicez ve sonra biz applikasyonu calistirinca arkaplanda async bir sekilde kaydetmeye baslicak

#app.task() yine filedan import
app = Celery('tasks', backend='redis://localhost', broker='pyamqp://guest:guest@rabbit:5672')

class AcquireData:

    ##celery ne diyecek olursak bizim icin rabbitmq ve flask iletisimin yapiyor
    # app = Celery('tasks', broker='rabbitmq://localhost:5672')
    # BROKER_URL = 'amqp://guest:guest@localhost:5672//'

    # bu task decorateri ayni zamanda method cagirmana olanak sagliyor
    @app.task
    def get_ticker(symbol, interval):

        client = Client(config.API_KEY, config.API_SECRET)

        one_min = Client.KLINE_INTERVAL_1MINUTE,
        thirty_min = Client.KLINE_INTERVAL_30MINUTE

        # should get all {symbols} from binance
        # store it in a own dictionary as keys: values , as keys being ofc {ticker_symbol} and v beign JSON? or just candlestick object.
        candlesticks = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, limit=100)

        processed_candlestick = []
        for data in candlesticks:
            candlestick = {
                'time': data[0] / 1000,
                'open': data[1],
                'high': data[2],
                'low': data[3],
                'close': data[4]
            }
            processed_candlestick.append(candlestick)
            # method to save in db.Ticker.TimeSeries[]

# results = [requests.get(f'http://127.0.0.1:5000/foo/{task_id}').json()
#            for task_id in task_ids]
# [{'Result': True}, {'Result': True}]