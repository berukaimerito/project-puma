from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask import Flask, render_template, Blueprint,jsonify, request
from puma_db import models, database
from puma_db.models import Ticker
from puma_db.database import initialize_db
from puma_db.models import *
puma_app = Flask(__name__)

puma_app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost/test'
}
initialize_db(puma_app)



@puma_app.route('/')
def main():
    return 'returned string'

@puma_app.route('/homepage')
def home_page():

    # GET TICKERS
    #GUIDE INFO , SIMPLE TEXT , SLIDES ---> interactive HTML
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


@puma_app.route("/dashboard/{user_id}")
def puma_dashboard():
    # provide all user customized information 
    # {TICKER, REAL-TIME. HISTORICAL, PORTFOLIO, IDE}
    # IF user clicks the start script 
    pass


@puma_app.route("/dashboard/script/{user_id}/{ticker_symbol}/{session_id}")
def puma_dev_env():
    # open a IDE dialog
    # start all scripting services
    pass


@puma_app.route("/users")
def provide_register():
    # If user is not logged in, provide him a button to register
    pass

@puma_app.route("/users/{user_id}")
def user_account():
    
    # return the whole user page HTML
    # If anything selected , redirect to that method ? or route
    pass

@puma_app.route("/profile/{user_id}/settings")
def user_settings():

    # pass
    pass

@puma_app.route("/profile/{user_id}/actions")
def user_actions():

    pass

    # pass

@puma_app.route("/profile/{user_id}/scripts")
def user_scripts_overview():

    pass


@puma_app.route("/dashboard/{user_id}")
def puma_dashboard():

    #PROVIDE PORTFOLIO, REAL-TIME, HISTORICAL DATA, WIDGET 
    pass


@puma_app.route("/dashboard/{user_id}/tickers?={ticker_symbol}")
def puma_dashboard():
    pass

@puma_app.route("/portfolio/{user_id}")
def puma_dashboard_portfolio():
    # open portfolio in full page
    # provide portfolio settings
    # access ticker symbol, user information, actions 
    pass




@puma_app.route("/dashboard/{user_id}/develop/tickers?={ticker_symbol}/scripts?={scripts_id}")
def puma_dev_env():

    # If user open IDE dialog, the state is now interactive.

    # portfolio could change

    # system can deliver messages 

    # security is assured



    pass



if __name__ == "__main__":
    puma_app.run(debug=True)
    #puma_app.run(debug=True , port=5001, host='0.0.0.0')