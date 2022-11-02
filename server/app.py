from flask import Flask, render_template, Blueprint, jsonify, request, redirect
from puma_db import models, database
from puma_db.models import Ticker
from puma_db.database import initialize_db
from puma_db.models import *
from Forms import RegisterForm
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

puma_app = Flask(__name__)

puma_app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/test'
}
puma_app.config['SECRET_KEY'] = 'Detective ashe is on the case'
initialize_db(puma_app)
csrf.init_app(puma_app)


@puma_app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        User(
            name=form.username.data,
            last_name=form.last_name.data,
            email=form.email.data,
            cell=form.cell.data,
            password=form.password.data,
        ).save()

        return render_template('index.html')
    return render_template('register.html', form=form)


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
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        User(name=username, password=password).save()

        return render_template('index.html')

    return render_template('register.html')


# def register11():
#     """Register new user."""
#     form = RegisterForm(request.form)
#     if form.validate_on_submit():
#         User.create(
#             username=form.username.data,
#             email=form.email.data,
#             password=form.password.data,
#             active=True,
#         )
#         flash("Thank you for registering. You can now log in.", "success")
#         return redirect(url_for("public.home"))
#     else:
#         flash_errors(form)
#     return render_template("public/register.html", form=form)
#


# @puma_app.route('/register')
# def registe1r():
#     # open a form page
#     # check information filled in simultaneously
#     # if information is not valid, do not allow user to register , a.k.a save in database
#     # if user saved in database, contact with mail provider service to send a confirmation mail to the user
#     pass
#

@puma_app.route("/dashboard")
def dashboard():
    # return only charts  { ACCES TICKER, REAL-TIME, HISTORICAL DATA }
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
