from mongoengine import *


class User(Document):
    username = StringField()
    email = EmailField()
    password = StringField()
    # portfolio = ListField(EmbeddedDocumentField(PortfolioModel))



    @staticmethod
    def check_name(name):
        return True if User.objects.filter(username=name).first() else False

    @staticmethod
    def check_mail(mail):
        return False if User.objects.filter(mail=mail).first() else True

    @staticmethod
    def getquery_name(name):
        return User.objects.filter(username=name).first()

    @staticmethod
    def getquery_mail(mail):
        return User.objects.filter(mail=mail).first()

    @staticmethod
    def getquery_id(id):
        return User.objects.filter(id=id).first()









