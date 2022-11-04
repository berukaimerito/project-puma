from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask import Flask, render_template, Blueprint, jsonify, request, session, make_response
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_praetorian import Praetorian
from mongodb.models import Ticker
from mongodb.database import initialize_db
from mongodb.models import *
import config
from binance.client import Client
from binance.enums import *
from flask import Flask
from flask_cors import CORS, cross_origin
from datetime import timedelta
from functools import wraps 
import jwt

client = Client(config.API_KEY, config.API_SECRET)




puma_app = Flask(__name__)


#puma_app.secret_key 
puma_app.config['SECRET_KEY'] = b'somelongrandomstring'
CORS(puma_app)

puma_app.permanent_session_lifetime = timedelta(days=3)

puma_app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/test'
}

guard = Praetorian()

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request/args.get('token')
        if not token:
            return jsonify({'ALERT!': 'TOKEN is missing!'})
        try:
            payload = jwt.decode(token, puma_app['SECRET_KEY'])
        except: 
            return jsonify({'Alert': 'Invalid Token'})
    return decorated


initialize_db(puma_app)


@puma_app.route('/')
def main():
    return 'returned string'


@puma_app.route('/homepage')
def home_page():
    # GET TICKERS
    # GUIDE INFO , SIMPLE TEXT , SLIDES ---> interactive HTML
    pass


@puma_app.route('/login', methods=['GET', 'POST'])
def login():
    # form page to login
    # will check database if user exists or not
    pass


@puma_app.route('/register')
def register():
    # open a form page
    # check information filled in simultaneously
    # if information is not valid, do not allow user to register , a.k.a save in database
    # if user saved in database, contact with mail provider service to send a confirmation mail to the user
    pass


@puma_app.route("/dashboard")
def dashboard():
    # return only charts  { ACCES TICKER, REAL-TIME, HISTORICAL DATA }
    pass


@puma_app.route("/dashboard/{nick_name}")
def puma_dashboard_v2():
    # provide all user customized information
    # {TICKER, REAL-TIME. HISTORICAL, PORTFOLIO, IDE}
    # IF user clicks the start script
    pass



@puma_app.route("/chart")
def index():
    return render_template('chart.html')


@puma_app.route("/profile/settings")
def settings():
    # pass
    pass


@puma_app.route("/dashboard/actions")
def actions():
    pass




@puma_app.route("/dashboard")
def puma_dashboard():
    # PROVIDE PORTFOLIO, REAL-TIME, HISTORICAL DATA, WIDGET
    pass


@puma_app.route("/dashboard/charts/{currency}")
def puma_charts():
    pass


@puma_app.route("/dashboard/cryptocurrencies")
def puma_prices():
    #Selected 10 crypto (real time)
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

@puma_app.route("/history")
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
   # puma_app.run(debug=True)
    puma_app.run(debug=True , port=5001, host='0.0.0.0')