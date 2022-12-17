from mongoengine import Document
from mongoengine import StringField, BooleanField, ReferenceField
# from user_model import UserModel
from models.ticker_model import TickerModel
from mongoengine import EmbeddedDocument


class ScriptModel(EmbeddedDocument):
    
    in_use = BooleanField()
    path = StringField()
    symbol = StringField()
    pyscript = StringField()
    interval = StringField()


    def __str__(self):
        return f'{{"symbol" : "{self.symbol}", "script": "{self.pyscript}", "interval": "{self.interval}"}}'

