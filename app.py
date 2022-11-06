import os
import gunicorn
from pathlib import Path
from datetime import timedelta, datetime
from functools import wraps
import string
import config
import secrets
from flask import (
    Flask,
    render_template, 
    Blueprint,
    jsonify,
    request,
    redirect, 
    session,
    flash,
    make_response,
    url_for,
    redirect
 )
from binance import Client
from flask_wtf.csrf import CSRFProtect
import flask_cors
from flask_cors import CORS 
from flask_bcrypt import Bcrypt
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful_swagger_2 import Api
from flask_mongoengine import MongoEngine
import jwt

env_path = Path(".") / ".pumavenv"

client = Client(config.API_KEY, config.API_SECRET)  
alphabet = string.ascii_letters + string.digits
secret_key = ''.join(secrets.choice(alphabet) for i in range(16))
csrf = CSRFProtect()
db = MongoEngine()
cors = flask_cors.CORS()


puma = Flask(__name__, static_folder="static", template_folder="templates")


puma.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/test'}
puma.config['SECRET_KEY'] = secret_key
puma.config['JWT_SECRET_KEY'] = 'someverysecretstring'
puma.config["WTF_CSRF_ENABLED"] = False

csrf.init_app(puma)
db.init_app(puma)
cors.init_app(puma)
bcrypt = Bcrypt(puma)
api = Api(puma)
cors = CORS(puma, resources={r'/*': { 'origins': '*' }})


@puma.route("/")
@puma.route("/index")
def index():
    return '<h1>Welcome home</h1>'

@puma.route('/scripts')
def scripts_overview():
    return {'k': 'v'}

@puma.route('/chart')
def chart():
    return render_template('chart.html')


@puma.route('/register/', methods=['GET', 'POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(name=data['name'],password=hashed_password)
    new_user.save()
    return jsonify({'message' : 'New user created'})


@puma.route('/login')
def login():
    # s
    data = request.json
    user = User.objects.filter(name=data['name']).first()

    if check_password_hash(user.password, data['password']):
        token = jwt.encode(
            {'username': user.name, 'exp': datetime.utcnow() + timedelta(minutes=45)},
            puma.config['SECRET_KEY'], "HS256")

        return jsonify({'token': token})



@puma.route("/history")
def history():
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, limit=100)

    processed_candlestick = []
    for data in candlesticks:
        candlestick = {
            'time':  data[0] /1000,
            'open': data[1],
            'high': data[2],
            'low': data[3],
            'close': data[4]
        }
        processed_candlestick.append(candlestick)
    return jsonify(processed_candlestick)


if __name__ == "__main__":
   puma.run(host="127.0.0.1", port=5000, debug=True)