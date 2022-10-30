from curses.ascii import US
from email.policy import default
from enum import unique
from sqlite3 import Date
from mongoengine import *
import datetime
from puma_db.database import *
#import mongoengine_goodjson as gj

#connect(host="mongodb://127.0.0.1:27017/test_2")

# class Status(Enum):
#     NEW = 'NEW'
#     ONGOING = 'ONGOING'
#     DONE = 'DONE'

class User(Document):
    name = db.StringField(required=True)
    # last_name = db.StringField(required=True)
    # name = db.StringField(unique=True)
    # email = db.EmailField(required=True)
    # password = db.StringField(required = True)
    cell = db.StringField()
   # Portfolio = EmbeddedDocumentField(document_type=Document)


class Log(Document):
    datetime = DateTimeField()



class Ticker(Document):
    ticker_symbol = StringField()
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
    #state = EnumField(Status, default=Status.NEW)


# user = User(name='Using MongoEngine')
# user.tags = ['mongodb', 'mongoengine']
# user.save()