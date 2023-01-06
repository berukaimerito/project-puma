from mongoengine import EmbeddedDocument
from mongoengine import StringField, IntField, FloatField, DateTimeField
from flask import jsonify, json


class PortfolioModel(EmbeddedDocument):
    symbol = StringField()
    profit = FloatField()
    buy_price = FloatField()
    sell_price = FloatField()
    open_timestamp = StringField()
    close_timestamp = StringField()
    def __repr__(self):
        return f'symbol:{self.symbol} amount:{self.amount}'
