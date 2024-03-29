from flask.json import JSONEncoder
from bson import json_util
from mongoengine.base import BaseDocument
from mongoengine.queryset.base import BaseQuerySet

class MongoEncoder(JSONEncoder):
    def default(self,obj):
        if isinstance(obj,BaseDocument):
            return json_util._json_convert(obj.to_mongo())
        elif isinstance(obj,BaseQuerySet):
            return json_util._json_convert(obj.as_pymongo())
        return JSONEncoder.default(self, obj)