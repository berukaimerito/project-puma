
from crypt import methods
from flask import Flask, render_template, Blueprint,jsonify, Response
from flask import request
from puma_db.models import *
from puma_db.database import initialize_db

puma_app = Flask(__name__)

puma_app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost/test'
}

initialize_db(puma_app)

@puma_app.route("/")
def test():
    return "<h1>HOME</h1>"

ex = [  
    {
        "name": "Kaan",
        "nick_name": "Kosti",
        "portfolio": "['ETH': 442]" }
    ]

@puma_app.route("/home")
def home_page():
    return  jsonify(ex)
    # f'{Ticker.ticker_symbol} price is : {Ticker.real_p

@puma_app.route("/login")
def login():
    return jsonify(ex)

@puma_app.route("/register")
def register():
    return jsonify(ex)

@puma_app.route("/users")
def users():
   users = User.objects().to_json()
   return Response(users, mimetype="application/json", status=200)

@puma_app.route("/users" , methods=['POST'])
def user_save():
    body = request.get_json()
    user = User(**body).save()
    id = user.id
    return {'id': str(id)} , 200




if __name__ == "__main__":
    puma_app.run(debug=True , port=5001, host='0.0.0.0')


##TODO 

#API VISION 
# /home ---> 
# /dashboard ---> chart , portfolio, widget(runtime_service) a.k.a PYTHON IDE
# Design Patterns 
# DB Dockerize (Marcin)
# Endpoint 
# Real Time , Historical Data
# RabbitMQ
# SCAFFOLD
# UTILITIES