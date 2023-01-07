import abc
import json
import requests


class Abc(abc.ABC):

    def __init__(self, username, symbol, app):
        self.username = username
        self.symbol = symbol
        self.app = app
        self.data = None

        # Flags
        self.buy_flag = None
        self.sell_flag = None

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

        # Indicator

        # Ai

    def run_once(function):
        def wrapper(*args, **kwargs):
            if not wrapper.has_run:
                wrapper.has_run = True
                return function(*args, **kwargs)

        wrapper.has_run = False
        return wrapper

    @run_once
    def buy(cls):
        cls.buy_flag = cls.on_going = True

    @run_once
    def sell(cls):
        cls.sell_flag = True
        cls.on_going = False

    def on_price_change(cls, data, ts, price):
        None

    def post_result(cls):
        pass

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
        if cls.buy_flag and not cls.sell_flag:
            cls.script_open_price = cls.close  # Profit
            cls.script_open_timestamp = cls.timestamp  # Data candle
            cls.buy_flag = False
            cls.post_buy_info()
        if cls.sell_flag and not cls.buy_flag:
            cls.script_close_price = cls.close
            cls.script_close_timestamp = cls.timestamp
            cls.post_result()
        print(cls.username , cls.symbol)
        cls.on_price_change(data, str(data['CandleStick']['timestamp']['$date']), float(data['CandleStick']['close']))
        print(" [x] Done")
        # ch.close()
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume_interval_2(cls, ch, method, properties, body):
        cls.ch = ch
        dic = cls.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume_interval_3(cls, ch, method, properties, body):
        cls.ch = ch
        dic = cls.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume_interval_4(cls, ch, method, properties, body):
        cls.ch = ch
        dic = cls.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume_interval_5(cls, ch, method, properties, body):
        cls.ch = ch
        dic = cls.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def calculate_closed_script(cls):
        cls.profit = ((cls.open_price - cls.close_price) / cls.close_price) * 100
        requests.post('http://127.0.0.1:5000/portfoliotracker',
                      json={'username': cls.username, 'symbol': cls.symbol, 'profit': cls.profit})

    def byte_to_dictionary(cls, str):
        data = json.loads(str)
        data['CandleStick'], data['Ticker'] = json.loads(data['CandleStick']), json.loads(data['Ticker'])
        cls.data = data
        return cls.data

    def post_buy_info(cls):
        requests.post('http://127.0.0.1:5000/portfoliotracker',
                      json={'username': cls.username, 'symbol': cls.symbol, 'Open price': cls.script_open_price,
                            'Open ts': cls.script_open_timestamp,'on_going':cls.on_going })

