from mongoengine import Document
from mongoengine import StringField, DateTimeField

class TickerModel(Document):
    symbol = StringField()
    timestamp = DateTimeField()
