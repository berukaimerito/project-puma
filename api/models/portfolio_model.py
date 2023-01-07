from mongoengine import EmbeddedDocument
from mongoengine import StringField, IntField, FloatField, DateTimeField,BooleanField
from flask import jsonify, json


class PortfolioModel(EmbeddedDocument):
    symbol = StringField()
    profit = FloatField()
    buy_price = FloatField()
    sell_price = FloatField()
    open_timestamp = StringField()
    close_timestamp = StringField()
    on_going = BooleanField()
    def __repr__(self):
        return f'symbol:{self.symbol} amount:{self.amount}'
