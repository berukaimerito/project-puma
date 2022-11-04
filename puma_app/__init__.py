from flask import Flask
from dashboard.routes import dashboard
from web.routes import web

def create_app():
    puma = Flask(__name__)
    puma.register_blueprint(dashboard)
    puma.register_blueprint(web)
    return puma


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)