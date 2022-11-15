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
        return True if UserModel.objects.filter(name=name).first() else False

    @staticmethod
    def check_mail(mail):
        return False if UserModel.objects.filter(email=mail).first() else True
    @staticmethod
    def getquery_name(name):
        return UserModel.objects.filter(name=name).first()

    @staticmethod
    def getquery_mail(mail):
        return UserModel.objects.filter(email=mail).first()




