
from abstractbot import Abc

import time


class Bot(Abc):

    def on_price_change(self, data, ts, price):

        if self.open > 1:

            print(self.buy_flag, self.sell_flag)

            self.buy()
            if self.open > 1:
                self.sell()
