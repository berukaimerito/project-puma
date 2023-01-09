import os
import random
import json
import requests
import asyncio
from datetime import timedelta
from db import db
from common.utils import *
from common.encoder import MongoEncoder
from common.get_data import get_historical_kline
from dotenv import dotenv_values
from flask import Flask, request, jsonify, json, make_response
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user_model import *
from werkzeug.security import check_password_hash


config = dotenv_values()




puma = Flask(__name__, static_folder="static", template_folder="templates", instance_relative_config=True)

cors = CORS(puma, resource={
    r"/*": {
        "origins": "*"
    }
})

puma.config["MONGODB_SETTINGS"] = [
    {
        "db": "v1",
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

    return get_historical_kline(symbol, interval)


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
        os.remove(f"user_scripts/{user.username}_{symbol}.py")

    return jsonify(response)


@puma.route('/portfolio_finish', methods=['POST'])
def portfolio_finish():
    data = request.json
    user,symbol,profit,close_ts,close_price,on_going= UserModel.getquery_name(data['username']),data['symbol'],data['profit'],data['Close ts'],data['close_price'],data['on_going']
    print('apideyim',user,symbol,close_ts,close_price,on_going)
    user.check_transaction(symbol,profit,close_ts,close_price,on_going)
    print('if blogu ici')
    return jsonify(data)


@puma.route('/portfoliotracker', methods=['POST'])
def portfolio_update():
    data = request.json
    print('portfolio tracker')
    user = UserModel.getquery_name(data['username'])
    user.add_portfolio(data['symbol'], data['Open price'], data['Open ts'], data['on_going'])
    user.save()
    return jsonify(data)


from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor()

@puma.route('/dashboard/portfolio', methods=['GET'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
@jwt_required()
def get_portfolio():

    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)

    portfolio = user.portfolio
    item_dicts = []
    for item in portfolio:
        item_dict = {
            'symbol': item.symbol,
            'open_price': item.buy_price,
            'open_timestamp': item.open_timestamp,
            'on_going': item.on_going,
            'profit': item.profit
        }
        if item.on_going:
            executor.submit(update_profit(item_dict))
        item_dicts.append(item_dict)
    return jsonify(item_dicts)

import asyncio

async def update_profit(item):
    while True:
        # code to update the profit value goes here
        profit = random.randint(0, 100)
        item.update(set__profit=profit)
        await asyncio.sleep(0.2)

# @puma.route('/dashboard/portfolio', met
# hods=['GET'])

# def get_portfolio():

#     portfolio = []


#     # Retrieve portfolio items from database
#     portfolio_items = user.portfolio

#     # Iterate through each portfolio item and create a dictionary representation
#     for item in portfolio_items:
#         item_dict = {
#             'symbol': item.symbol,
#             'open_price': item.buy_price,
#             'open_timestamp': item.open_timestamp,
#             'on_going': item.on_going,
#             'profit': item.profit
#         }
#         # If the item is ongoing, update the profit value every 0.2 seconds
#         if item.on_going:
#             while True:
#         # update profit value here
#                 item_dict['profit'] = update_profit(item_dict)
#         portfolio.append(item_dict)

#     return jsonify(portfolio)

@puma.route('/update-profit', methods=['POST'])
def update_profit_route():
    asyncio.run(run_update_profit())
    return "Updating profit in the background"


async def update_profit():
    while True:
        # code to update the profit value goes here
        user = UserModel.objects(username='your_username').first()
        portfolio = user.portfolio
        for item in portfolio:
            if item.on_going:
                updated_profit = compute_profit(item.buy_price)
                item.update(set__profit=updated_profit)
        await asyncio.sleep(0.2)


def compute_profit(bought, current):
    pass
   




        


        #     def update_profit():
        #         # Calculate the new profit value
        #         new_profit = calculate_profit(item)
        #         # Update the profit value in the dictionary
        #         item_dict['profit'] = new_profit
        #     # Use the setInterval function to call update_profit every 0.2 seconds
        #     setInterval(update_profit, 200)
        # else:
        #     # If the item is not ongoing, set the profit value in the dictionary to the current profit value
        #     item_dict['profit'] = item.profit
        # # Append the dictionary to the portfolio list
        # portfolio.append(item_dict)

    # Return the portfolio list as a JSON response
   # return jsonify(portfolio)


# @puma.route('/dashboard/portfolio', methods=['GET'])
# @cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
# @jwt_required()
# def display_portfolio():
#     # Get the user's portfolio data from the database
#     user_id = get_id(str_to_dict(get_jwt_identity()))
#     user = UserModel.getquery_id(user_id)
#     result = []

#     if request.method == 'GET':
#         for item in user.portfolio:
#             item_dict = {
#                 'symbol': item.symbol,
#                 'open_price': item.open_price,
#                 'open_timestamp': item.open_timestamp,
#                 'on_going': item.on_going,
#             }

#             # If the item is not live, append the close price and profit to the item dict
#             if not item.on_going:
#                 item_dict['close_price'] = item.close_price
#                 item_dict['profit'] = item.profit
#                 item_dict['close_timestamp'] = item.close_timestamp

#             # If the item is live, get the live profit data from the websocket
#             else:
#                 live_profit = get_live_profit(item.symbol)
#                 item_dict['profit'] = live_profit

#             result.append(item_dict)

#         return jsonify(result)



# def get_live_profit(symbol):
#     # Connect to the websocket and get the live profit data for the given symbol
#     sio = socketio.Client()
#     sio.connect('http://localhost:5000')
#     live_profit = sio.emit('get_live_profit', {'symbol': symbol})
#     sio.disconnect()
#     return live_profit

# @socketio.on('get_live_profit')
# def update_profit(data):
#     symbol = data['symbol']
#     while True:
#         # Get the latest profit data for the symbol
#         profit = get_latest_profit(symbol)
#         # Emit the profit data back to the client
#         emit('profits', {'symbol': symbol, 'profit': profit})
#         time.sleep(0.1)


def get_latest_profit():
    # Return a random value between 3 and 30 as the profit
    return random.uniform(3, 30)


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

        else:
            user.add_script(symbol,script,path,False)
            user.save()

        r = {'symbol': symbol, 'code': script}
        return make_response(jsonify(r))



def send_queue(data):
    print("SENT usagum")
    response = jsonify("Queue sent")
    requests.post("http://127.0.0.1:8000/create_queue", json=data, verify=False)
    return response


json_list = []
queues = set()


@puma.route('/scripts/<symbol>/run', methods=['POST', 'GET', 'PUT'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
@jwt_required()
def script_run(symbol):

    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)
    data = {'userName': user.username,
            'symbol': symbol,
            }
    queue = json.dumps(data, sort_keys=True)

    if not queues:
        queues.add(queue)
        print('now')
        if user.check_scripts(symbol):
            send_queue(data)
            return jsonify(data), 200
    else:
        if queue in queues:
            return jsonify('EXISTS'), 401
        else:
            if user.check_scripts(symbol):
                send_queue(data)
                return jsonify(data),200
    
    return jsonify(data)


@puma.route('/scripts/<symbol>/stop', methods=['POST', 'GET', 'PUT'])
@cross_origin(origin='*', headers=['Content- Type', 'Authorization'])
@jwt_required()
def script_stop(symbol):

    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)

    data = {'userName': user.username,
            'symbol': symbol,
            }
    
    requests.post("http://127.0.0.1:8000/stop_queue", json=data, verify=False)
    return jsonify(data)

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


#socketio.start_background_task(target=socketio.run, app=puma)
if __name__ == '__main__':
    puma.run(host="127.0.0.1", port=5000, debug=True)

