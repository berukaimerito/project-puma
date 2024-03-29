from db import db
from mongoengine import Document
from mongoengine import StringField, EmailField, EmbeddedDocumentField, ListField
from models.portfolio_model import PortfolioModel
from models.script_model import ScriptModel
# from api.models.script_model import ScriptModel
from werkzeug.security import generate_password_hash, check_password_hash
from utils import *


class UserModel(Document):
    username = StringField(required=False)
    email = EmailField(required=False)
    surname = StringField()
    password = StringField(required=False)
    portfolio = ListField(EmbeddedDocumentField(PortfolioModel))
    scripts = ListField(EmbeddedDocumentField(ScriptModel))
    
    
    def edit_user_pswd(self, pswd):
        new_pswd = generate_password_hash(pswd)
        self.password = new_pswd
        return True
    
    def edit_user_mail(self, email):
        self.email = email
        return True

    def edit_user_surname(self, surname):
        self.surname = surname
        return True

    def edit_user_name(self, username):
        self.username = username
        return True
        

    def add_portfolio(self, symbol):
        self.portfolio.append((PortfolioModel(symbol=symbol)))

    def add_script(self, symbol, pyscript, path):
        self.scripts.append((ScriptModel(symbol=symbol, pyscript=pyscript, path=path)))
    

    def delete_script(self, symbol):

        for script in self.scripts:
            if str(script["symbol"]) == symbol:
                print(str(script["symbol"]), symbol)
                self.scripts.remove(script)
        self.save()

    def find_pyscript_by_symbol(self, symbol):
        for script in self.scripts:
            if str(script.symbol) == str(symbol):
                return script.pyscript

    def edit_script(self, symbol,pyscript):

        for script in self.scripts:
            if str(script.symbol) == str(symbol):
                script.pyscript = pyscript
                print( script.pyscript )
                print( pyscript )
                print(script.pyscript==pyscript)

                return True


    @staticmethod
    def check_symbol(id, symbol):
        user = UserModel.objects(id=id).first()
        for i in user.scripts:
            if str(i.symbol) == str(symbol):
                return False
        return True

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password, method='sha256')

    @staticmethod
    def check_name(name):
        return True if UserModel.objects.filter(username=name).first() else False

    @staticmethod
    def check_mail(email):
        return False if UserModel.objects.filter(email=email).first() else True

    @staticmethod
    def getquery_name(username):
        return UserModel.objects.filter(username=username).first()

    @staticmethod
    def getquery_mail(email):
        return UserModel.objects.filter(email=email).first()

    @staticmethod
    def getquery_id(id):
        return UserModel.objects.filter(id=id).first()
