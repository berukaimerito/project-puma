from flask import Blueprint
from extension import *

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.route('/')
@dashboard.route('/scripts')
def scripts_overview():
    return {'k': 'v'}

@dashboard.route('/chart')
def chart():
    return render_template('chart.html')