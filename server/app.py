import bcrypt as bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from flask import Flask, render_template, Blueprint,jsonify, request


import csrf
from puma_db.database import initialize_db
from puma_db.models import *

puma_app = Flask(__name__)

puma_app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost/test'
}
initialize_db(puma_app)


#User Logged in
@puma_app.route('/')

@puma_app.route('dashboard/script')
def view():
    # Write script
    return 'user'


@puma_app.route('dashboard/portfolio')
def viewp():
    # View Portfolio
    return 'user'

@puma_app.route('dashboard/history')
def viewpppp():
    # History of scripts
    return 'user'


#
#
#
#
#
# #All users
# @puma_app.route('/charts/<symbol>')
# def view():
#     # View chart
#     return 'user'
#
# @puma_app.route('/register')
# def register():
#     # Register user
#     return 'user'
#
# @puma_app.route('/cryptocurrencies')
# def register():
#     # See the real time prices
#     return 'user'
#
#
#
#
#
#



# @puma_app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method =='POST':
#       this_user = User.objects.get(name=request.form['username'])
#       if request.form['username'] !=this_user.name:
#           return 'Invalid user'
#       elif bcrypt.check_password_hash(this_user.password, request.form['password']) == False:
#           return 'Invalid password'
#       else:
#           return '<h>Welcomeeeeee</h>'
#
#     return render_template('login.html', error=error)

@puma_app.route("/<usr>")
def user_logged_in(usr):
    return  f'Welcome {usr}'


@puma_app.route("/users" , methods=['POST'])
def portfolio():
    body = request.get_json()
    user = User(**body).save()
    id = user.id
    return {'id': str(id)} , 200



if __name__ == "__main__":
    puma_app.run(debug=True)

    #puma_app.run(debug=True , port=5001, host='0.0.0.0')