from abstractbot import Abc
import requests
import json
# config = dotenv_values()
class Bot(Abc):
    def on_price_change(self, data, ts, price):

        if price > 0.2 and not self.on_going:
            self.buy(ts, price)

        if self.on_going and price > 0.2:
            print(31)
            self.sell(ts, price)
            self.calculate_closed_script()


