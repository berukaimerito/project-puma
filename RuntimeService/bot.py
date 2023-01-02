from abstractbot import Abc
import requests
import json

#config = dotenv_values()


class Bot(Abc):
    timestamp = ''

    def __init__(self, username, symbol, app):
        self.username = username
        self.symbol = symbol
        self.app = app
        self.data = None
        self.open_price = None
        self.close_price = None
        self.open_timestamp = None
        self.close_timestamp = None
        self.on_going = False
        self.profit = False
        self.finished = False

    def sell(self, ts, price):
        self.on_going = False
        self.close_timestamp = str(ts)
        self.close_price = float(price)
        print('sell ici')

    def buy(self, ts, price):
        self.on_going = True
        self.open_timestamp = str(ts)
        self.open_price = float(price)

        print('buy ici')

    def on_price_change(self, data, ts, price):
        print((price))
        if price > 0.4 and not self.on_going:
            self.buy(ts, price)
        if self.on_going and price > 0.4:
            self.sell(ts, price)
            self.calculate_closed_script()
            # self.close_channels()
    # def calculate_current_percentage(self):
    #     self.profit

    def calculate_closed_script(self):
        self.profit = ((self.open_price - self.close_price) / self.close_price) * 100
        requests.post('http://127.0.0.1:5000/portfoliotracker',
                      json={'username': self.username, 'symbol': self.symbol, 'profit': self.profit})


    def consume_interval_1(self,ch, method, properties, body):
        dic = Bot.byte_to_dictionary(body.decode())
        #self.on_price_change(dic)
        print(body.decode())
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)


    def consume_interval_2(self,ch, method, properties, body):
        dic = Bot.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)


    def consume_interval_3(self,ch, method, properties, body):
        dic = Bot.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)


    def consume_interval_4(self,ch, method, properties, body):
        dic = Bot.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)


    def consume_interval_5(self,ch, method, properties, body):
        dic = Bot.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    
    # def __str__(self):
    #     return f'{self.username},{self.symbol}'
