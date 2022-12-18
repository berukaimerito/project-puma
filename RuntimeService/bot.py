from dotenv import dotenv_values

config = dotenv_values()
from abstractbot import Abc
import json


class Bot(Abc):
    timestamp = ''




    def __init__(self, username, symbol, app):
        self.username = username
        self.symbol = symbol
        self.app = app





    @staticmethod
    def byte_to_dictionary(str):
        res = json.loads(str)
        res['CandleStick'] = json.loads(res['CandleStick'])
        res['Ticker'] = json.loads(res['Ticker'])
        return res

    # def buy(self):



    # def on_price_change(self,data):
    #     if data['CandleStick']['high']==30:
    #         buy()



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

    #
    # def __str__(self):
    #     return f'{self.username},{self.symbol}'
