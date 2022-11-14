
from mongoengine import *

class User(Document):
    name = StringField(required=False)
    last_name = StringField(required=False)
    email = EmailField(required=False)
    password = StringField(required=False)
    cell = StringField()
    #portfolio = EmbeddedDocumentField()
    @staticmethod
    def check_name(name):
        return False if User.objects.filter(name=name).first() else True




class Portfolio(Document):
    symbol = StringField()
    amount = IntField()
    current_prices = FloatField()


class Log(Document):
    datetime = DateTimeField()


class Ticker(Document):
    symbol = StringField()
    timestamp = DateTimeField()


# class Candles(Document):
#     timestamp,
#     length, --- interval
#     high,
#     low,
#     open,
 #     close

class Action(Document):
    _type = BooleanField()
    amount = LongField()
    ticker = ReferenceField(Ticker)
    # script = ReferenceField(Script)

class Script(Document):
    in_use = BooleanField()
    path = StringField()
    user = ReferenceField(User)


# user = User(name='rodri',last_name='alonso',password='a')
# user.save()

# signals.post_init.connect(update_modified)
