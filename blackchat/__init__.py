


import os
import uuid
from flask import Flask
from flask import Blueprint
from flask import render_template
from flask_wtf.csrf import CSRFError, CSRFProtect
from flask_socketio import SocketIO
from flask_login import LoginManager
from flask_session import Session



socketio = SocketIO()
csrf = CSRFProtect()
login_manager = LoginManager()
sess = Session()

# custom imports
from blackchat.views import bp as blackchat_bp
from blackchat import events


def create_app():
    """Create an application."""

    SECRET_KEY = str(uuid.uuid4())
    WTF_CSRF_SESSION_KEY = str(uuid.uuid4())

    app = Flask(__name__)
    app.config.from_object('blackchat.config.DefaultConfig')
    # app.config.from_envvar('BLACKCHAT_SETTINGS')

    if os.environ['ENV'] in ('prod', 'production'):
        app.config.from_object('blackchat.config.ProductionConfig')
    elif os.environ['ENV'] in ('dev', 'development'):
        app.config.from_object('blackchat.config.DevelopmentConfig')
    elif os.environ['ENV'] in ('stage', 'staging'):
        app.config.from_object('blackchat.config.StagingConfig')
    elif os.environ['ENV'] in ('test', 'testing'):
        app.config.from_object('blackchat.config.TestingConfig')
    else:
        app.logger.info('using default config')

    app.logger.info('config: {}'.format(app.debug))
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['WTF_CSRF_SESSION_KEY'] = WTF_CSRF_SESSION_KEY
    app.secret_key = SECRET_KEY

    # NOTE: SESSION_TYPE defaults to null which does not work if using flask-session
    app.config['SESSION_TYPE'] = 'filesystem'

    if not app.debug:
        import logging
        from logging.handlers import TimedRotatingFileHandler
        # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
        file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'blackchat.log'), 'midnight')
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
        app.logger.addHandler(file_handler)

    @app.context_processor
    def utility_functions():
        def print_in_console(message):
            print(str(message))

        return dict(mdebug=print_in_console)

    app.register_blueprint(blackchat_bp)

    socketio.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    sess.init_app(app)

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def not_found(error):
        return render_template('500.html'), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        app.logger.error(e.description)
        return render_template('csrf_error.html', reason=e.description), 400

    return app
