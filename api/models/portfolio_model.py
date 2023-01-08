from mongoengine import EmbeddedDocument
from mongoengine import StringField, IntField, FloatField, DateTimeField,BooleanField
from flask import jsonify, json


class PortfolioModel(EmbeddedDocument):
    symbol = StringField()
    buy_price = FloatField()
    open_timestamp = StringField()
    on_going = BooleanField()

    profit = FloatField()

    close_price = FloatField()
    close_timestamp = StringField()
    def __repr__(self):
        return f'symbol:{self.symbol} amount:{self.amount}'


    def calculate_profit(self):
        self.buy_price-self.close_price


