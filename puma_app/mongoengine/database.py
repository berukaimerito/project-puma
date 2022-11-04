from flask_mongoengine import MongoEngine
from puma_app import app
db = MongoEngine()

def initialize_db(app):
    db.init_app(app)