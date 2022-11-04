from flask_mongoengine import MongoEngine
db = MongoEngine()

def initialize_db(puma_app):
    db.init_app(puma_app)
