import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path("..") / ".env"
load_dotenv(dotenv_path=env_path)

MONGO_URI_SH= 'mongodb://localhost/test'
SECRET_KEY= 'ourvery7612secretkey'
CELERY_BROKER_URL= 'amqp://guest:guest@localhost:5672'
API_KEY = 'YooZh5uicqICkpX4FnYYX5Aouw2J6Yp6QQkmqt5qJCPp40FNvAt8rJYvRdN9PmyB'
API_SECRET = 'VuLkeD8HVUjAHUE4Rk3RSHw6EnnpRlVtBUfVcaLbvi5K0DeScZSApdgUdg8MrCYe'


class BaseConfig:
    """Base configuration"""
    BASE_DIR = Path(__file__).parent.parent

    TESTING = False

    # Flask Settings
    API_TITLE = "puma_rest"

    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Flask-Mongoengine
    MONGO_DB_URL = os.environ.get("MONGO_URI_SH")

    MONGO_SETTINGS = {
        'host': MONGO_DB_URL
    }

    SWAGGER = {
        'title': 'PUMA',
        'uiversion': 2
    }



class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}



