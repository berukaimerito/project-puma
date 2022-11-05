from functools import wraps
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
from passlib.hash import pbkdf2_sha256 as sha256
from binance import Client
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS, cross_origin
import flask_cors
import string
import secrets
from datetime import datetime, timedelta
from flask_cors import CORS 
from flask_bcrypt import Bcrypt
import config
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful_swagger_2 import Api
from flask_mongoengine import MongoEngine
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import jwt

client = Client(config.API_KEY, config.API_SECRET)  
alphabet = string.ascii_letters + string.digits
secret_key = ''.join(secrets.choice(alphabet) for i in range(16))
csrf = CSRFProtect()
db = MongoEngine()
cors = flask_cors.CORS()


def tokenReq(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
            try:
                jwt.decode(token, secret_key)
            except:
                return jsonify({"status": "fail", "message": "unauthorized"}), 401
            return f(*args, **kwargs)
        else:
            return jsonify({"status": "fail", "message": "unauthorized"}), 401
    return decorated


puma = Flask(__name__)


puma.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/test'}
puma.config['SECRET_KEY'] = secret_key
puma.config['JWT_SECRET_KEY'] = 'someverysecretstring'
puma.config["WTF_CSRF_ENABLED"] = False

csrf.init_app(puma)
db.init_app(puma)
cors.init_app(puma)
bcrypt = Bcrypt(puma)
jwt_m = JWTManager(puma)
api = Api(puma)
cors = CORS(puma, resources={r'/*': { 'origins': '*' }})



@puma.route("/")
@puma.route("/index")
def index():
    return '<h1>Welcome home</h1>'

    # # auth = request.authorization
    # # if auth and auth.password == 'password':
    # token = jwt.encode({'user': auth.username, 'exp':datetime.datetime.utcnow()+ datetime.timedelta(minutes=30) }, puma.config['SECRET_KEY'])

@puma.route("/login", methods = ['POST'])
def login():

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username != "test" or password != "test": ## QUERY 
        return jsonify({"msg": "Bad credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

 
@puma.route("/register")
def register():
    pass

@puma.route('/scripts')
@tokenReq
def scripts_overview():
    return {'k': 'v'}

@puma.route('/chart')
def chart():
    return render_template('chart.html')


client = Client(config.API_KEY, config.API_SECRET)  

@puma.route("/history")
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
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