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
from flask import Flask, request, jsonify, make_response, render_template
from flask_jwt_extended import JWTManager, get_jwt_identity
from models.user_model import UserModel
from flask_jwt_extended import jwt_required
from flask_cors import CORS,cross_origin
from dotenv import dotenv_values
from flask_jwt_extended import create_access_token, jwt_required, current_user, get_jwt_identity
from flask import jsonify, json, make_response
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
            
            return jsonify(user_r, access_token)
    
    msg = {'msg': 'Welcome'}
    return jsonify(msg)

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


@puma.route("/profile", methods =['DELETE', 'POST', 'PUT', 'GET'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
@jwt_required()
def edit():

    user_id = str_to_dict(get_jwt_identity())['_id']['$oid']
    user = UserModel.getquery_id(user_id)
    data  =  request.json
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
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def default_chart():

    data = request.json
    symbol = data['symbol']
    interval = data['interval']
    return get_historical_kline(symbol, interval)



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
        return jsonify(response)
    
    all_scripts =jsonify(symbol)
    return all_scripts

@puma.route('/dashboard/portfolio', methods=['GET'])
@jwt_required()
def portfolio():

    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)
    port=[]
    if request.method == 'GET':
        for script in user.scripts:
            port.append({script.symbol,script.profit})
        return jsonify(port)
    return jsonify(user)

@puma.route('/scripts', methods=['POST', 'GET', 'PUT'])
@jwt_required()
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def scripts():

    # users get queue data
    if request.method == 'GET':
        val  = "fun()"
        r = {'code': val}
        return jsonify(r)

    if request.method == 'POST':
         data = request.json
         symbol,script = data['symbol'],data['code']
         user_id = get_id(str_to_dict(get_jwt_identity()))
         user = UserModel.getquery_id(user_id)
         data = {'userName': user.username,
            'symbol': symbol,
            }
         with open(f"user_scripts/{user.username}.py", "w") as user_script:
            user_script.write(f"{script}")
            path = f"user_scripts/{user.username}.py"

            user.add_script(symbol, script, path)
            user.save()

            r ={'symbol': symbol, 'code': script}
            return make_response(jsonify(r))
    
    return jsonify()
 


@puma.route('/scripts/<symbol>/run', methods=['POST', 'GET', 'PUT'])
@jwt_required()
def run_script_start_rs_queues(symbol):

    if request.method == 'POST':
            user_id = get_id(str_to_dict(get_jwt_identity()))
            user = UserModel.getquery_id(user_id)
            data = {'userName': user.username, 'symbol': symbol }
            requests.post("http://127.0.0.1:8000/create_queue", json=data, verify=False)
            return "script run successfully"

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
                r = {"currency": str(i.symbol),"code": str(i.pyscript)}
                return jsonify(r)

@puma.route('/scripts/<symbol>', methods=['POST', 'PUT'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
@jwt_required()
def execute_script(symbol):

    user_id = get_id(str_to_dict(get_jwt_identity()))
    user = UserModel.getquery_id(user_id)
    
    data = request.json

               
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

            return make_response(loaded_r)

puma.run(host="127.0.0.1", port=5000, debug=True)