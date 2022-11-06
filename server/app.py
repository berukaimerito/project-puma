import flask
import flask_praetorian
from flask import \
    Flask, render_template, Blueprint, jsonify, request, redirect, session, flash, make_response
from flask_restful.utils.crypto import decrypt

from puma_db import models, database
from puma_db.models import Ticker
from puma_db.database import *
from puma_db.models import *
from RegisterForm import RegisterForm
from LoginForm import LoginForm
from flask_wtf.csrf import CSRFProtect
from flask_login import login_required, login_user, logout_user
from flask_login import LoginManager
import jwt
from datetime import datetime, timedelta
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from cryptography.fernet import Fernet

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

key = Fernet.generate_key()
crypter = Fernet(key)


login_manager = LoginManager()
csrf = CSRFProtect()
# guard = flask_praetorian.Praetorian()

puma_app = Flask(__name__)

puma_app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/test'
}
puma_app.config['SECRET_KEY'] = 'Detective ashe is on the case'

initialize_db(puma_app)
# csrf.init_app(puma_app)


# login_manager.init_app(puma_app)



@puma_app.route('/register/', methods=['GET', 'POST'])
def register():
    data = request.json
    if User.objects.filter(name=data['name']):
        return make_response('User already exists')
    else:
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = User(name=data['name'],password=hashed_password)
        new_user.save()
        return jsonify({'message' : 'New user created'})

import datetime
@puma_app.route('/login')
def login():
    data = request.json
    user = User.objects.filter(name=data['name']).first()
    if check_password_hash(user.password, data['password']):
        token = jwt.encode(
            {'name': user.name, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
            puma_app.config['SECRET_KEY'], "HS256")
        return jsonify({'token': token})


def token_required(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        data = jwt.decode(token, puma_app.config['SECRET_KEY'],algorithms=['HS256'])
        current_user = User.objects .filter(name=data['name']).first()
        return function(current_user, *args, **kwargs)
    return decorated

#User crud

@puma_app.route('/dashboard')
@token_required
def change_email(user):





    return jsonify({'dsadas': '321312'})

    pass




# def validate(data):
#     user = User.objects.filter(name=data['name']).first()
#
#     if user:
#         print(user.check_password(data['password']))
#
#         return make_response('HATALIIIIIIIIIIIIIIII', 401, {'WWW-Authenticate': 'Basic realm="Login Required'})

# @puma_app.route("/login", methods=['GET', 'POST'])
# def login1():
#      data = request.json
#      validate(data)
#      return make_response('hala hatali', 401, {'WWW-Authenticate': 'Basic realm="Login Required'})
     # if name:
     #     pass
     #
     # else:
     #    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required'})


    #
    # if not auth or not auth.username or not auth.password:
    #     return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required'})
    #
    # user = User.objects.filter(name=auth.username).first()
    # user = User(name="abc").save()
    #
    #
    # if not user:
    #     return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required'})
    #     #return jsonify({'message': 'No user found!'})
    #
    # if  check_password_hash(, auth.password):
    #     token = jwt.encode({'user': auth.username, 'exp':datetime.utcnow()+ timedelta(minutes=30) }, puma.config['SECRET_KEY'])
    #     return jsonify({'token': token}, 201)
    #
    # return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})


#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User(id=user_id)
#
#
#
# @puma_app.route('/register/', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm(request.form)
#     if form.validate_on_submit():
#         User(
#             name=form.name.data,
#             last_name=form.last_name.data,
#             email=form.email.data,
#             cell=form.cell.data,
#             password=form.password.data,
#         ).save()
#         flash(f'Account created for {form.name.data}')
#         return render_template('index.html')
#     return render_template('register.html', form=form)
#
#
# @puma_app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm(request.form)
#     if form.validate_on_submit():
#         access_token = create_access_token(identity=form.name)
#         return jsonify(access_token=access_token)
#
#     return render_template('login.html')
#
#
#









"""""""""""""""""""""""""""""""'"""""""

#
#


#


"""""""""""""""""""""""""""""""'"""""""


# @puma_app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(login.html)
#


@puma_app.route('/')
def main():
    return 'returned string'


@puma_app.route('/homepage')
def home_page():
    # GET TICKERS
    # GUIDE INFO , SIMPLE TEXT , SLIDES ---> interactive HTML
    pass


@puma_app.route("/dashboard")
def puma_dashboard():
    # provide all user customized information
    # {TICKER, REAL-TIME. HISTORICAL, PORTFOLIO, IDE}
    # IF user clicks the start script
    pass


@puma_app.route("/profile/settings")
def settings():
    # pass
    pass


@puma_app.route("/dashboard/actions")
def actions():
    pass


# @puma_app.route("/history")
# @cross_origin(origin='*',headers=['Content-Type','Authorization'])
# def history():
#     candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, limit=100)
#
#     processed_candlestick = []
#     for data in candlesticks:
#         candlestick = {
#             'time':  data[0] /1000,
#             'open': data[1],
#             'high': data[2],
#             'low': data[3],
#             'close': data[4]
#         }
#         processed_candlestick.append(candlestick)
#     return jsonify(processed_candlestick)

# @puma_app.route("/history/<symbol_name>")
# @cross_origin(origin='*',headers=['Content-Type','Authorization'])
# def history():
#     pass
#
#


# @puma_app.route("/dashboard")
# def puma_dashboard():
#     # PROVIDE PORTFOLIO, REAL-TIME, HISTORICAL DATA, WIDGET
#     pass


@puma_app.route("/dashboard/charts/{currency}")
def puma_charts():
    pass


@puma_app.route("/dashboard/cryptocurrencies")
def puma_prices():
    # Selected 10 crypto (real time)
    pass


@puma_app.route("/dashboard/portfolio")
def puma_dashboard_portfolio():
    # open portfolio in full page
    # provide portfolio settings
    # access ticker symbol, user information, actions
    pass


@puma_app.route("/dashboard/develop/{ticker_symbol}")
def puma_dev_env():
    # If user open IDE dialog, the state is now interactive.

    # portfolio could change

    # system can deliver messages

    # security is assured

    pass


@puma_app.route("/dashboard/scripts")
def scripts_overview():
    pass


@puma_app.route("/dashboard/scripts/<scrip_id>")
def script_overview():
    pass


if __name__ == "__main__":
    puma_app.run(debug=True)

    # puma_app.run(debug=True , port=5001, host='0.0.0.0')
