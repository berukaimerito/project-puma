from mongoengine import Document
from mongoengine import BooleanField, LongField, ReferenceField
from script_model import ScriptModel
from ticker_model import TickerModel
class ActionModel(Document):
    _type = BooleanField()
    amount = LongField()
    ticker = ReferenceField(TickerModel)
    script = ReferenceField(ScriptModel)