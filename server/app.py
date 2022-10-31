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


@puma_app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@puma_app.route('/')
def main():
    return 'annesi'










@puma_app.route("/users" , methods=['POST'])
def portfolio():
    body = request.get_json()
    user = User(**body).save()
    id = user.id
    return {'id': str(id)} , 200







if __name__ == "__main__":
    puma_app.run(debug=True)
    #puma_app.run(debug=True , port=5001, host='0.0.0.0')