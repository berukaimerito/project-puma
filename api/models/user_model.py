from api.db import db
from mongoengine import Document
from mongoengine import StringField, EmailField, EmbeddedDocumentField
from api.models.portfolio_model import PortfolioModel


class UserModel(Document):
    name = StringField(required=False)
    last_name = StringField(required=False)
    email = EmailField(required=False)
    password = StringField(required=False)
    cell = StringField()
    portfolio = EmbeddedDocumentField(PortfolioModel)

    @staticmethod
    def check_name(name):
        return False if UserModel.objects.filter(name=name).first() else True
