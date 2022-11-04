from mongoengine import *
import datetime
#from .database import db

# connect(host="mongodb://127.0.0.1:27017/test")

# class Status(Enum):
#     NEW = 'NEW'
#     ONGOING = 'ONGOING'
#     DONE = 'DONE'

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
   # state = EnumField(Status, default=Status.NEW)



# user = User(name='Kaan',last_name='Kosti',password='a')
# user.save()



# script1 =Script(in_use=True,path="neyin pathi bilmiyorum",user=user)
# script1.save()
disconnect(alias='default')