from mongoengine import EmbeddedDocument
from mongoengine import StringField, IntField, FloatField

class PortfolioModel(EmbeddedDocument):
    symbol = StringField()
    amount = IntField()
    profit = FloatField()