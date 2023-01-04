from abstractbot import Abc
class Bot(Abc):
    timestamp = ''

    def __init__(self, username, symbol, app):
        self.username = username
        self.symbol = symbol
        self.app = app
        self.on_going = None
        self.price= None

    def buy(self):
        pass

    def on_price_change(self, data, ts, price):
        print(type(price))
        self.yarraklama()
        print('ICERDEY====E=F=SF=E=DE=DE=DE=DE=DE=DE=D=E=ED=DE')

        # if price > 0.2 and not self.on_going:
        #     self.buy(ts, price)
        #     print('buyladim')
        # if self.on_going and price > 0.2:
        #     print(31)
        #     self.sell(ts, price)
        #     self.calculate_closed_script()
        #     # self.close_channels()

