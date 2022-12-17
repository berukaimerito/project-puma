from mongoengine import Document, DateTimeField


class LogModel(Document):
    datetime = DateTimeField()
