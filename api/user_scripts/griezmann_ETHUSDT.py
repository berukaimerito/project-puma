from abstractbot import Abc







import time

class Bot(Abc):
    def on_price_change_1m(self, data, ts, price):
        if self.open < 1:
            self.buy()

            if self.open >1:

                self.sell()