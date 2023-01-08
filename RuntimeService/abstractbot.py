import time
from abc import ABC, abstractmethod
import json
import requests


class Abc(ABC):

    def called_once(method):
        def wrapper(self, args, kwargs):
            if not hasattr(self, 'called'):  # Check if the object has the 'called' attribute
                setattr(self, 'called', False)  # If not, set it to False
            if not self.called:  # Check if the method has already been called
                method(self, args, kwargs)  # Call the method
                self.called = True  # Set the 'called' attribute to True to mark that the method has been called

        return wrapper

    def __init__(self, username, symbol, app):
        self.username = username
        self.symbol = symbol
        self.app = app
        self.data = None

        self.called = False

        # Flags
        self.buy_flag = None
        self.sell_flag = False

        # Script
        self.script_open_price = None
        self.script_close_price = None
        self.script_open_timestamp = None
        self.script_close_timestamp = None
        self.finished = False
        self.profit = False
        self.on_going = False

        # on_price_change
        self.high = None
        self.low = None
        self.open = None
        self.close = None
        self.volume = None
        self.open_time = None
        self.close_time = None
        self.timestamp = None

        self.called_buy = False

        # Indicator

    def run_once(function):
        def wrapper(*args, **kwargs):
            if not wrapper.has_run:
                wrapper.has_run = True
                return function(*args, **kwargs)

        wrapper.has_run = False
        return wrapper

    def buy(cls):

        if cls.buy_flag == None:
            cls.buy_flag = cls.on_going = True

    def sell(cls):
        if cls.buy_flag == True:
            cls.sell_flag = True


    def on_price_change_1m(cls, data, ts, price):
        None

    def on_price_change_15m(cls, data, ts, price):
        None

    def on_price_change3_1h(cls, data, ts, price):
        None

    def on_price_change_4h(cls, data, ts, price):
        None

    def on_price_change_1D(cls, data, ts, price):
        None

    def post_buy_info(cls):
        print('post buy info')
        requests.post('http://127.0.0.1:5000/portfoliotracker',
                      json={'username': cls.username, 'symbol': cls.symbol, 'Open price': cls.script_open_price,
                            'Open ts': cls.script_open_timestamp, 'on_going': True})

    def post_result(cls):
        print('post result ici')
        if cls.on_going:

            cls.calculate_closed_script()
            print('girdi')
            requests.post('http://127.0.0.1:5000/portfolio_finish',
                          json={'username': cls.username, 'symbol': cls.symbol, 'Close ts': cls.script_close_timestamp,
                                'close_price': cls.script_close_price, 'on_going':False, 'profit': cls.profit})
            return
    def calculate_total(self):
        pass

    def consume_interval_1(cls, ch, method, properties, body):
        cls.ch = ch
        data = cls.byte_to_dictionary(body.decode())
        cls.high = float(data['CandleStick']['high'])
        cls.low = float(data['CandleStick']['low'])
        cls.open = float(data['CandleStick']['open'])
        cls.close = float(data['CandleStick']['close'])
        cls.volume = data['CandleStick']['volume']
        cls.open_time = data['CandleStick']['open_time']
        cls.close_time = data['CandleStick']['close_time']
        cls.timestamp = str(data['CandleStick']['timestamp']['$date'])

        if cls.buy_flag and cls.on_going:
            print('buy icerisi ')
            cls.script_open_price = cls.close  # Profit
            cls.script_open_timestamp = cls.timestamp  # Data candle
            cls.buy_flag = False
            cls.post_buy_info()
            print('bir kere girdim buy ici')
            if cls.sell_flag and cls.on_going:
                print('sell ici')
                cls.script_close_price = cls.close
                cls.script_close_timestamp = cls.timestamp
                cls.post_result()
                ch.close()
        cls.on_price_change_1m(data, str(data['CandleStick']['timestamp']['$date']),
                               float(data['CandleStick']['close']))
        print(" [x] Done")
        # ch.close()
        ch.basic_ack(delivery_tag=method.delivery_tag)



    def calculate_closed_script(cls):
        cls.profit = ((cls.open - cls.close) / cls.close) * 100
        return float(cls.profit)

    def byte_to_dictionary(cls, str):
        data = json.loads(str)
        data['CandleStick'], data['Ticker'] = json.loads(data['CandleStick']), json.loads(data['Ticker'])
        cls.data = data
        return cls.data

