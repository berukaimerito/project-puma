import json
import requests
from functools import wraps
from utils import *
from datetime import timedelta
from db import db
from config import API_SECRET, API_KEY
from get_data import get_historical_kline
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity
from utils import *
from flask import Flask, request, jsonify, make_response
from flask_jwt_extended import JWTManager, get_jwt_identity
from flask_restful import Api
from flask_wtf.csrf import CSRFProtect
from models.user_model import UserModel
from flask_jwt_extended import jwt_required
from resources.user_resource import User, UserRegister, DeleteUser
from resources.homepage import Home
from flask import Flask
from flask import Flask
from flask_cors import CORS,cross_origin
from dotenv import dotenv_values
from flask_jwt_extended import create_access_token, jwt_required, current_user, get_jwt_identity
from flask import jsonify, json, make_response
from models.user_model import *
from utils import *
from common.encoder import MongoEncoder
from werkzeug.security import generate_password_hash, check_password_hash

config = dotenv_values()


# def send_mail(user):
#     msg = Message('Hello from the other side!', sender='fec0f6c31ed308@mailtrap.io', recipients = [user])
#     msg.body = f"Hey {user}, sending you this email from my Flask app, lmk if it works"
#     mail.send(msg)
#     return "Message sent!"



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
cors = CORS(puma, resource={
    r"/*":{
        "origins":"*"
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

puma.config['MAIL_SERVER']='smtp.mailtrap.io'
puma.config['MAIL_PORT'] = 2525
puma.config['MAIL_USERNAME'] = 'fec0f6c31ed308'
puma.config['MAIL_PASSWORD'] = 'c259b7cf222ee6'
puma.config['MAIL_USE_TLS'] = True
puma.config['MAIL_USE_SSL'] = False



# csrf = CSRFProtect()
# csrf.init_app(puma)
db.init_app(puma)
jwt = JWTManager(puma)

# @puma.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response   


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
        #  response = {
        # "Status": status.HTTP_200_OK,
        # "Message": "Welcome HOME",
        # "Data": loaded_r
        #
        #  }
        #
 
        return response


@puma.route('/<username>/password', methods = ['GET', 'PUT'])
@jwt_required()
def change_password():
    pass

@puma.route("/login", methods = ['POST'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
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
            response =jsonify(user_r, access_token)
            return response

    return {'message': 'Wrong username or password.'}, 401

@puma.route("/register", methods = ['POST'] )
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def register_user():
    data = request.json
    username, email, surname, password, confirm = data['username'], data['email'], data['surname'], data['password'], data['confirm']

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
    #send_mail(user=email)

    msg = {'message': 'User has been created successfully.'}
    return make_response(jsonify(user, msg), 200)

@jwt_required()
@puma.route("/edit", methods =['DELETE'])
def delete():
    user_id = str_to_dict(get_jwt_identity())['_id']['$oid']
    UserModel.objects(id=user_id).delete()
    pass

@puma.route("/historical_klines", methods=['POST', 'GET'])
def default_chart():
    data = request.json
    symbol = data['symbol']
    interval = data['interval']
    return get_historical_kline(symbol, interval)


main_page_currencies = ['BTCUSDT', 'AVAXUSDT', 'ETHUSDT', 'DOGEUSDT', 'MATICUSDT']


@puma.route("/currencies", methods=['GET'])
def live_currencies_main(symbol):
    return main_page_currencies


@puma.route("/dashboard/currencies", defaults={'symbol': 'BTCUSDT', 'interval': '4h'}, methods=['POST', 'GET'])
def live_currencies_dashboard(symbol):

    currencies = ['BTCUSDT', 'AVAXUSDT', 'ETHUSDT']
    currencies.insert(0, symbol)
    currencies.pop()



@puma.route('/dashboard/portfolio', methods=['POST', 'GET'])
@jwt_required()
def portfolio():

    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)

    for script in user.scripts:
        print(script)
        user.add_portfolio(script.symbol)
    
    response = {

    }
    return jsonify(user.portfolio)




@puma.route('/dashboard', methods=['POST', 'GET', 'PUT', 'DELETE'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
@jwt_required()
def dash():
    data = request.json
    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)
    if user.scripts:
        response = [{'symbol': i.symbol} for i in user.scripts]
        if request.method == 'DELETE':
            symbol = data['symbol']
            user.delete_script(symbol)
            return jsonify(symbol)
        return jsonify(response)
    
    return jsonify('No scripts')


# @puma.route('/dashboard', methods=['POST', 'GET', 'PUT'])
# @jwt_required()
# def dash():
#     data = request.json
#     user_id = get_id(str_to_dict(get_jwt_identity()))
#     user = UserModel.getquery_id(user_id)
#
#     if request.method == 'GET':
#         if user.scripts:
#             response = [{'symbol': i.symbol, 'interval': i.interval} for i in user.scripts]
#             json_string = json.dumps(response)
#             return json_string
#         else:
#             return jsonify('No scripts yet')
#
# if request.method == 'DELETE':
#     f = furl("/abc?def='ghi'")
#     print(f.args[symbol])



@puma.route('/scripts', methods=['POST', 'GET', 'PUT'])
@jwt_required()
def scripts():
    # users get queue data
    data = request.json
    symbol,script = data['symbol'],data['code']
    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)
    data = {'userName': user.username,
            'symbol': symbol,
            }
    if request.method == 'POST' and user.check_symbol(user_id, symbol):
        user.add_script(symbol, script)
        user.save()
        #
        # json_object = json.dumps(data)
        # loaded_r = json.loads(json_object)

        requests.post("http://127.0.0.1:8000/create_queue", json=data, verify=False)

        r ={'symbol': symbol, 'code': script}
        return make_response(jsonify(r))
    
    return {''}
 
   

@puma.route('/scripts/<symbol>', methods=['POST', 'GET', 'PUT'])
@jwt_required()
def execute_script(symbol):

    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)
    
    data = request.json

    if request.method == 'GET':
        for i in user.scripts:
            if str(i.symbol) == str(symbol):
                r = {"currency": str(i.symbol),"code": str(i.pyscript)}
                return make_response(jsonify(r))
               
    if request.method == 'POST':
        new_script = data['code']
        user_script = user.find_pyscript_by_symbol(symbol)
        user.edit_script(symbol, new_script)
        py_script = user.find_pyscript_by_symbol(symbol)
        user.save()

        if user.edit_script:
            json_object = json.dumps({
                'userName': user.username,
                'symbol': symbol,
                'script': py_script

            })

            loaded_r = json.loads(json_object)
            requests.post("http://127.0.0.1:8000/create_queue", json=loaded_r)
            return make_response(loaded_r)


# @puma.route('/dashboard/scripts/<scripts_id>')
# def scripts():
#     pass
# @puma.route('/dashboard/scripts')
# def scripts():
#     pass


#
#
# @puma.route("/dashboard/currencies", methods=['POST', 'GET'])
# @jwt_required()
# def index():
#     return '<h1>Welcome homepage</h1>'



puma.run(host="127.0.0.1", port=5000, debug=True)



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
