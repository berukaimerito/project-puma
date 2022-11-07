import os

from dotenv import load_dotenv
from pathlib import Path
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


API_KEY = 'YooZh5uicqICkpX4FnYYX5Aouw2J6Yp6QQkmqt5qJCPp40FNvAt8rJYvRdN9PmyB'
API_SECRET = 'VuLkeD8HVUjAHUE4Rk3RSHw6EnnpRlVtBUfVcaLbvi5K0DeScZSApdgUdg8MrCYe'
#MAYBE CREATE A CLASS AND PUT ALL FLASK.CONFIG variables here, register as a blueprint?
# from mongoengine import connect
# def initialize_db(app):
#     connect(host=app.config['MONGODB_SETTINGS'])

class ConfigClass(object):

    """" FLASK APPLICATION CONFIG """
    # Flask Settings
    API_TITLE = "puma_rest"

    SECRET_KEY = os.environ.get("SECRET_KEY")

    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")

    print(CELERY_BROKER_URL)
    print(SECRET_KEY)

    # Flask-MongoengineS
    MONGO_DB_URL = os.environ.get("MONGO_URI_SH")

    MONGO_SETTINGS = {
        'host': MONGO_DB_URL
    }

    print(MONGO_DB_URL)


    # FLASK-User settings for mail, etc.

    #Flask- Session






