import time

import requests
from functools import wraps
from datetime import timedelta
from db import db
from get_data import get_historical_kline
from flask import Flask, request, jsonify, json, make_response
from flask_socketio import SocketIO
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin
from dotenv import dotenv_values
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user_model import *
from utils import *
from common.encoder import MongoEncoder
from werkzeug.security import check_password_hash

config = dotenv_values()


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


puma = Flask(__name__, static_folder="static", template_folder="templates", instance_relative_config=True)
socketio = SocketIO(puma)

cors = CORS(puma, resource={
    r"/*": {
        "origins": "*"
    }
})

puma.config["MONGODB_SETTINGS"] = [
    {
        "db": "integration",
        "host": "localhost",
        "port": 27017,
        "alias": "default",
    }
]

puma.config['WTF_CSRF_ENABLED'] = False
puma.config["SECRET_KEY"] = "secretsecret"
puma.config["JWT_SECRET_KEY"] = "Dese.Decent.Pups.BOOYO0OST"
puma.config['JSON_SORT_KEYS'] = False
puma.config['CORS_HEADERS'] = 'Content-Type'
puma.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12)

db.init_app(puma)
jwt = JWTManager(puma)


@puma.route("/home")
@puma.route("/")
def welcome():
    r = {'is_claimed': 'True', 'rating': 3.5}
    r = json.dumps(r)
    loaded_r = json.loads(r)

    response = {
        "Message": "Welcome HOME",
        "Data": loaded_r

    }

    return response


@puma.route("/login", methods=['POST'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def user_login():
    data = request.json
    user_name, password = data['username'], data['password']
    b_name = UserModel.check_name(user_name)
    if b_name:
        user = UserModel.getquery_name(user_name)
        if check_password_hash(user.password, password):
            access_token = create_access_token(identity=json.dumps(user, cls=MongoEncoder))

            user_r = {
                "name": user.username,
                "surname": user.surname,
                "email": user.email,
                "password": user.password
            }

            return jsonify(user_r, access_token)

    msg = {'msg': 'Welcome'}
    return jsonify(msg)


@puma.route("/register", methods=['POST'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def register_user():
    data = request.json
    username, email, surname, password, confirm = data['username'], data['email'], data['surname'], data['password'], \
                                                  data['confirm']

    if UserModel.getquery_name(username) or UserModel.getquery_mail(email):
        msg = {'message': 'Username or email has already been created, aborting.'}
        r = jsonify(msg)
        r.headers.add('Access-Control-Allow-Origin', '*')
        return make_response(jsonify(msg, r), 200)

    if password != confirm:
        msg = {'message': 'Passwords does not match.'}

        return make_response(jsonify(msg), 200)

    user = UserModel(
        username=username,
        surname=surname,
        email=email,
        password=UserModel.hash_password(password)
    )
    user.save()
    # send_mail(user=email)

    msg = {'message': 'User has been created successfully.'}
    return make_response(jsonify(user, msg), 200)


@puma.route("/profile", methods=['DELETE', 'POST', 'PUT', 'GET'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
@jwt_required()
def edit():
    user_id = str_to_dict(get_jwt_identity())['_id']['$oid']
    user = UserModel.getquery_id(user_id)
    data = request.json
    new_name = data['username']
    new_pswd = data['password']

    if request.method == 'GET':
        user.delete()

    if request.method == 'PUT' and new_name:
        user.edit_user_name(new_name)
        user.save()
        return jsonify(user)

    if request.method == 'PUT' and new_pswd:
        user.edit_user_pswd(new_name)
        user.save()
        return jsonify(user)


@puma.route("/historical_klines", methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def default_chart():
    data = request.json
    symbol = data['symbol']
    interval = data['interval']
    return jsonify('')
    # return get_historical_kline(symbol, interval)


@puma.route('/dashboard', methods=['POST', 'GET', 'PUT', 'DELETE'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
@jwt_required()
def dash():
    data = request.json
    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)

    response = [{'symbol': i.symbol} for i in user.scripts]
    print(response)
    if request.method == 'DELETE':
        symbol = data['symbol']
        user.delete_script(symbol)


    return jsonify(response)









@puma.route('/portfoliotracker', methods=['POST'])
def portfolio_update():
    data = request.json
    user = UserModel.getquery_name(data['username'])
    user.add_portfolio(data['symbol'], data['Open price'], data['Open ts'], data['on_going'])
    user.save()
    return jsonify(data)


@puma.route('/dashboard/portfolio', methods=['GET'])
@jwt_required()
def portfolio():
    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)
    result = []
    if request.method == 'GET':
        for item in user.portfolio:
            item_dict = {
                'symbol': item.symbol,
                'buy_price': item.buy_price,
                'open_timestamp': item.open_timestamp,
                'on_going': item.on_going
            }
            if not item.on_going:
                print()
                # item_dict = {
                #     'close'
                #      'close_ts'
                # }

            # else:
            #     while True:
            #         profit = calculate_profit(user.portfolio)
            #
            #         socketio.emit('profits', {'profits': profit})
            #         time.sleep(3)
            result.append(item_dict)
            print(type(item_dict))

        print(type(result))
        return jsonify(result)


def calculate_profit(list_of_p):
    result = []
    for item in list_of_p:
        profit = calculate_item_profit(item)
        result.append({'symbol': item.symbol, 'profit': profit})
    pass


def calculate_item_profit(item):
    print(item.open_price)

    pass


import os


@puma.route('/scripts', methods=['POST', 'GET', 'PUT'])
@jwt_required()
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def scripts():
    # users get queue data

    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)

    if request.method == 'POST':  # POST /sciprts
        data = request.json
        symbol, script = data['symbol'], data['code']

        with open(f"user_scripts/{user.username}_{symbol}.py", "w") as user_script:
            user_script.write(f"{script}")
            print('script yazdi')
            path = f"user_scripts/{user.username}.py"
        if user.check_scripts(symbol):

            user.edit_script(symbol, script)
            user.save()



            #
            # user.update_script(symbol, script, path, True)
            # user.save()
        else:
            print(3111111111111111111111111111111111111111111111111111111111111111111111111111111)
            user.update_script(symbol, script, path, True)
            pass

        r = {'symbol': symbol, 'code': script}
        return make_response(jsonify(r))


@puma.route('/scripts/<symbol>/run', methods=['POST', 'GET', 'PUT'])
@jwt_required()
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
def script_run(symbol):
    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)
    data = {'userName': user.username,
            'symbol': symbol,
            }

    if user.check_scripts(symbol):
        requests.post("http://127.0.0.1:8000/create_queue", json=data, verify=False)
        return make_response(jsonify('Gonderdik komutanim'))

    return jsonify('Already running')


# @puma.route('/scripts/<symbol>/run', methods=['POST', 'GET', 'PUT'])
# @jwt_required()
# def run_script_start_rs_queues(symbol):

#     if request.method == 'POST':
#             user_id = get_id(str_to_dict(get_jwt_identity()))
#             user = UserModel.getquery_id(user_id)
#             data = {'userName': user.username, 'symbol': symbol }
#             requests.post("http://127.0.0.1:8000/create_queue", json=data, verify=False)
#             return "script run successfully"

@puma.route('/scripts-by/<symbol>', methods=['POST'])
@cross_origin(origin='*')
@jwt_required()
def getscript_by_symbol(symbol):
    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)

    data = request.json

    if request.method == 'POST':
        for i in user.scripts:
            if str(i.symbol) == str(symbol):
                r = {"currency": str(i.symbol), "code": str(i.pyscript)}
                return jsonify(r)


@puma.route('/scripts/<symbol>', methods=['POST', 'PUT'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
@jwt_required()
def execute_script(symbol):
    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)

    data = request.json

    if request.method == 'POST':
        new_script = data['code']
        user.edit_script(symbol, new_script)
        py_script = user.find_pyscript_by_symbol(symbol)
        user.save()

        with open(f"user_scripts/{user.username}_{symbol}.py", "w") as user_script:
            user_script.write(f"{new_script}")
            print('script yazdi')
            path = f"user_scripts/{user.username}.py"

        json_object = json.dumps({
            'userName': user.username,
            'symbol': symbol,
            'script': py_script
        })

        loaded_r = json.loads(json_object)

        return make_response(loaded_r)


socketio.start_background_task(target=socketio.run, app=puma)
puma.run(host="127.0.0.1", port=5000, debug=True)
