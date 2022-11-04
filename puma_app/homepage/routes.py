
from flask import Blueprint

homepage = Blueprint('homepage', __name__)

@homepage.route("/")
@homepage.route("/index")
def index():
    return '<h1>Welcome home</h1>'