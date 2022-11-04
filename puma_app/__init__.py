from extension import *
from dashboard.routes import dashboard
from homepage.routes import homepage
from data_acquisition.routes import data_acquisiton

def create_app():

    puma = Flask(__name__)
    puma.register_blueprint(dashboard)
    puma.register_blueprint(homepage)
    puma.register_blueprint(data_acquisiton)
    puma.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/test'}
    puma.config['SECRET_KEY'] = secret_key
    csrf.init_app(puma)

    return puma

if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)