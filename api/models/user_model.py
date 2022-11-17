from api.db import db
from mongoengine import Document
from mongoengine import StringField, EmailField, EmbeddedDocumentField
from api.models.portfolio_model import PortfolioModel
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(Document):
    username = StringField(required=False)
    mail = EmailField(required=False)
    cell = StringField()
    password = StringField(required=False)
    portfolio = EmbeddedDocumentField(PortfolioModel)

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password, method='sha256')


    @staticmethod
    def check_name(name):
        return True if UserModel.objects.filter(username=name).first() else False

    @staticmethod
    def check_mail(mail):
        return False if UserModel.objects.filter(mail=mail).first() else True
    @staticmethod
    def getquery_name(name):
        return UserModel.objects.filter(username=name).first()

    @staticmethod
    def getquery_mail(mail):
        return UserModel.objects.filter(mail=mail).first()


    @staticmethod
    def getquery_id(id):
        return UserModel.objects.filter(id=id).first()



