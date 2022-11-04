
from flask import Blueprint

web = Blueprint('web', __name__)

@web.route("/")
@web.route("/index")
def index():
    return '<h1>Welcome home</h1>'