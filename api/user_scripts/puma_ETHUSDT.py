from abstractbot import Abc
class Bot(Abc):
    def on_price_change(self, data, ts, price):
        print(price,31)
