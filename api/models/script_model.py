from mongoengine import Document
from mongoengine import StringField, BooleanField, ReferenceField
from user_model import UserModel

class ScriptModel(Document):
    in_use = BooleanField()
    path = StringField()
    user = ReferenceField(UserModel)