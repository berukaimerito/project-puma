import bcrypt
from flask_restful.utils.crypto import decrypt
from mongoengine import *
import datetime
from wtforms import PasswordField
from wtforms.validators import DataRequired
from flask_security import UserMixin
from werkzeug.security import check_password_hash

# from .database import db

connect(host="mongodb://127.0.0.1:27017/test")

# class Status(Enum):
#     NEW = 'NEW'
#     ONGOING = 'ONGOING'
#     DONE = 'DONE'

from cryptography.fernet import Fernet

key = Fernet.generate_key()
crypter = Fernet(key)


class User(Document, object):
    name = StringField(required=False)
    last_name = StringField(required=False)
    email = EmailField(required=False)
    password = StringField(required=False)
    cell = StringField()



    @staticmethod
    def check_name(name):
        return False if User.objects.filter(name=name).first() else True




    @property
    def mail(self):
        return self.__email

    @mail.setter
    def mail(self, mail):
        self.__email = mail

        # if self.password.decode('utf8') == password:
        #     return True

    # portfolio = ListField(EmbeddedDocumentField('Portfolio'))
    # Portfolio = EmbeddedDocumentField(document_type=Document)


class Portfolio(Document):
    symbol = StringField()
    amount = IntField()
    current_prices = FloatField()

    # def check_password(self, value):
    #     """Check password."""
    #     return bcrypt.check_password_hash(self._password, value)


class Log(Document):
    datetime = DateTimeField()


class Ticker(Document):
    symbol = StringField()
    timestamp = DateTimeField()
    # timeseries: [
    #     {
    #         'oneMinute': ObjectIdField,
    #         'fifteenMinute': ObjectIdField,
    #         'oneHour':ObjectIdField,
    #         'oneDay': ObjectIdField,
    #     }
    # ]
    real_price = LongField()


# ticker = Ticker(symbol='BTCUSDT',
#                 timestamp='200'
#
#                 )


class Action(Document):
    _type = BooleanField()
    amount = LongField()
    ticker = ReferenceField(Ticker)
    # script = ReferenceField(Script)


class Script(Document):
    in_use = BooleanField()
    path = StringField()
    user = ReferenceField(User)


# state = EnumField(Status, default=Status.NEW)


# user = User(name='Kaan',last_name='Kosti',password='a')
# user.save()

# p = Portfolio(symbol='Btcusdt', amount=15, current_prices =2424124124213123123213123123124)
# p.save()
#
# script1 =Script(in_use=True,path="neyin pathi bilmiyorum",user=user)
# script1.save()
disconnect(alias='default')
