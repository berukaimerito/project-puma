import datetime
import json
from functools import wraps
from pathlib import Path

import requests
from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import UserModel
from flask_jwt_extended import jwt_required
from api.db import db

env_path = Path("..") / ".pumavenv"


#
def token_required(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401
        data = jwt.decode(token, puma.config['SECRET_KEY'], algorithms=['HS256'])
        current_user = UserModel.objects.filter(id=data['id']).first()
        return function(current_user, *args, **kwargs)

    return decorated


from resources.user_resource import User, UserRegister, DeleteUser
from resources.homepage import Home
from api.config import API_SECRET,API_KEY
puma = Flask(__name__, static_folder="static", template_folder="templates", instance_relative_config=True)

api = Api(puma)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

api.add_resource(User, "/login")
api.add_resource(UserRegister, "/register")
api.add_resource(Home, "/homepage")
api.add_resource(DeleteUser, "/delete")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

puma.config["MONGODB_SETTINGS"] = [
    {
        "db": "test",
        "host": "localhost",
        "port": 27017,
        "alias": "default",
    }
]

puma.config['WTF_CSRF_ENABLED'] = False
puma.config["SECRET_KEY"] = "secretsecret"
puma.config["JWT_SECRET_KEY"] = "Dese.Decent.Pups.BOOYO0OST"

csrf = CSRFProtect()
csrf.init_app(puma)
db.init_app(puma)
jwt = JWTManager(puma)


# jwt = JWT(app, authenticate, identity)  # Auto Creates /auth endpoint


#
# from binance import ThreadedWebsocketManager
#
# twm = ThreadedWebsocketManager(api_key=API_KEY, api_secret=API_SECRET)
# # start is required to initialise its internal loop
# twm.start()
#

# def handle_socket_message(msg):
#     print(f"message type: {msg['e']}")
#     print(msg)
#


# @user.route('/<user_id>', defaults={'username': None})
# @user.route('/<user_id>/<username>')
# def show(user_id, username):
#     pass
#
from binance import Client

@puma.route("/dashboard/chart", defaults={'symbol': 'AVAXUSDT', 'interval': '4h'}, methods=['POST','GET'])

def default_chart(symbol, interval):
    # print(symbol,interval)
    # data = request.json
    return redirect(url_for('display_charts',symbol=symbol,interval=interval))
    # return redirect(url_for('charts', symbol=symbol,interval=interval))
@puma.route("/dashboard/chart/<symbol>/<interval>")
def display_charts(symbol,interval):


    client = Client(API_KEY,API_SECRET)
    one_m = Client.KLINE_INTERVAL_1MINUTE,
    thirty_min = Client.KLINE_INTERVAL_30MINUTE


    # store it in a own dictionary as keys: values , as keys being ofc {ticker_symbol} and v beign JSON? or just candlestick object.
    candlesticks = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, limit=100)

    processed_candlestick = []
    for data in candlesticks:
        candlestick = {
            'time': data[0] / 1000,
            'open': data[1],
            'high': data[2],
            'low': data[3],
            'close': data[4]
        }
        processed_candlestick.append(candlestick)

        # method to save in db.Ticker.TimeSeries[]

    return processed_candlestick





#
#
# @puma.route("/dashboard/currencies", methods=['POST', 'GET'])
# @jwt_required()
# def index():
#     return '<h1>Welcome homepage</h1>'
#
#
# @puma.route("/dashboard/script", methods=['POST', 'GET'])
# @jwt_required()
# def index():
#     return '<h1>Welcome homepage</h1>'
#
#
# @puma.route("/dashboard/script/<script_id>", methods=['POST', 'GET'])
# @jwt_required()
# def index():
#     return '<h1>Welcome homepage</h1>'


puma.run(host="127.0.0.1", port=5000, debug=True)


@puma.route('/settings/password')
@token_required
def change_password(user):
    data = request.json
    pswrd = data['password']
    if user:
        user.update(password=generate_password_hash(pswrd, method='sha256'))
        return jsonify('Password change in silly level')
    else:
        return jsonify('Not success')

#
#


# @puma.route('/register', methods=['GET', 'POST'])
# def register():
#     data = request.json
#     if UserModel.objects.filter(name=data['name']):
#         return make_response('User already exists')
#     else:
#         hashed_password = generate_password_hash(data['password'], method='sha256')
#         new_user = UserModel(name=data['name'],password=hashed_password)
#         new_user.save()
#         return jsonify({'message' : 'New user created'})
#

#
# @puma.route('/login')
# def login():
#     data = request.json
#     user = UserModel.objects.filter(name=data['name']).first()
#     if check_password_hash(user.password, data['password']):
#          token = jwt.encode(
#              {'id':  json.dumps(str(user.id), default=str)[1:-1], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
#              puma.config['SECRET_KEY'], "HS256")
#          return jsonify({'token': token})
