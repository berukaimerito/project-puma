import abc
import json


class Abc(abc.ABC):

    def buy(self):
        pass

    def sell(self):
        pass

    def check(self):
        pass

    def on_price_change(cls, data, ts, price): None

    def yarraklama(self):
        print('Yarraklandin')

    def byte_to_dictionary(self, str):
        data = json.loads(str)
        data['CandleStick'], data['Ticker'] = json.loads(data['CandleStick']), json.loads(data['Ticker'])
        self.data = data
        return self.data

    def consume_interval_1(self, ch, method, properties, body):
        self.ch = ch
        data = self.byte_to_dictionary(body.decode())
        self.on_price_change(data, str(data['CandleStick']['timestamp']['$date']), float(data['CandleStick']['close']))
        # ch.close()
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume_interval_2(self, ch, method, properties, body):
        self.ch = ch
        dic = self.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume_interval_3(self, ch, method, properties, body):
        self.ch = ch
        dic = self.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume_interval_4(self, ch, method, properties, body):
        self.ch = ch
        dic = self.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume_interval_5(self, ch, method, properties, body):
        self.ch = ch
        dic = self.byte_to_dictionary(body.decode())
        # Bot.on_price_change(dic)
        ch.basic_ack(delivery_tag=method.delivery_tag)
