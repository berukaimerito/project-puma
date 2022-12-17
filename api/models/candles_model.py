from mongoengine import Document
from mongoengine import StringField

class Candles(Document):
    timestamp = StringField()
    length = StringField()
    high = StringField()
    low = StringField()
    open = StringField()
    close = StringField()