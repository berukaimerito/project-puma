import abc

class Abc(abc.ABC):

    def buy(self):
        pass
    #connection to API
    def sell(self):
        pass

    def check(self):
        pass


    def on_price_change(cls, ts, price): None


