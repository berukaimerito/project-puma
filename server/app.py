
from crypt import methods
from flask import Flask, render_template, Blueprint,jsonify, request
from puma_db import models, database
 

from puma_db.models import Ticker
from server.puma_db.database import initialize_db

puma_app = Flask(__name__)

puma_app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost/test'
}
initialize_db(puma_app)

@puma_app.route("/")
def test():
    return "<h1>Test</h1>"

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

@puma_app.route("/portfolio" , methods=['POST'])
def portfolio():
    ticker = request.get_json()
    ex.append(ticker)
    return {'id': len(ex)}, 200

if __name__ == "__main__":
    puma_app.run(debug=True , port=5001, host='0.0.0.0')