from abstractbot import Abc

class Bot(Abc):
    def on_price_change(self, data, ts, price):

        if self.open > 1:
            self.buy()
