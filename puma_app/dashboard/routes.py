from flask import Blueprint

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.route('/')
@dashboard.route('/scripts')
def scripts_overview():
    return {'k': 'v'}