from mongoengine import *
import datetime
from .database import db

class User(Document):
    name = StringField(required=False)
    last_name = StringField(required=False)
    email = EmailField(required=False)
    password = StringField(required = False)
    cell = StringField()
   #Portfolio = EmbeddedDocumentField(document_type=Document)


class Log(Document):
    datetime = DateTimeField()


class Ticker(Document):
    symbol = StringField()
    timestamp = DateTimeField()
    time_series = ObjectIdField()
    real_price = LongField()


class Action():
    amount = LongField()
    ticker = ReferenceField(Ticker)
    user = ReferenceField(User)


class Script(Document):
    in_use = BooleanField()
    path = StringField()
    user = ReferenceField(User)