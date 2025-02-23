from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=True):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config["SECRET_KEY"] = "dddffd_fdfd2Ds@@"

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    socketio.init_app(app)
    return app
