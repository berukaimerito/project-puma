from mongoengine import *

class Portfolio(EmbeddedDocument):
    symbol = StringField()
    amount = IntField()
    current_prices = FloatField()


class User(Document):
    name = StringField(required=False)
    last_name = StringField(required=False)
    email = EmailField(required=False)
    password = StringField(required=False)
    cell = StringField()
    portfolio = EmbeddedDocumentField(Portfolio)

    @staticmethod
    def check_name(name):
        return False if User.objects.filter(name=name).first() else True


class Log(Document):
    datetime = DateTimeField()


class Ticker(Document):
    symbol = StringField()
    timestamp = DateTimeField()


class Candles(Document):
    timestamp = StringField()
    length = StringField()
    high = StringField()
    low = StringField()
    open = StringField()
    close = StringField()


class Script(Document):
    in_use = BooleanField()
    path = StringField()
    user = ReferenceField(User)


class Action(Document):
    _type = BooleanField()
    amount = LongField()
    ticker = ReferenceField(Ticker)
    script = ReferenceField(Script)