from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
bootstrap=Bootstrap()
moment=Moment()
db=SQLAlchemy()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main
    app.register_blueprint(main)
    from .auth import auth
    app.register_blueprint(auth,url_prefix='/auth')
    return app