import os
from flask import Flask
from flask import Blueprint


app = Flask(__name__)
app.config.from_object('blackchat.default_settings')
app.config.from_envvar('BLACKCHAT_SETTINGS')


from flask_socketio import SocketIO


socketio = SocketIO()

# blackchat_bp = Blueprint('blackchat', __name__)
from blackchat.views import bp as blackchat_bp
from blackchat import events

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    if not app.debug:
        import logging
        from logging.handlers import TimedRotatingFileHandler
        # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
        file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'blackchat.log'), 'midnight')
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
        app.logger.addHandler(file_handler)

    app.register_blueprint(blackchat_bp)

    socketio.init_app(app)
    return app
