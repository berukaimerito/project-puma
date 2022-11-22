from mongoengine import EmbeddedDocument
from mongoengine import StringField, IntField, FloatField
from flask import jsonify, json
class PortfolioModel(EmbeddedDocument):
    symbol = StringField()
    amount = IntField()
    profit = FloatField()




    def __repr__(self):
        return f'symbol:{self.symbol} amount:{self.amount}'