import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    TESTING = True
    SECRET_KEY='KEY'
    WTF_CSRF_ENABLED = False
    FLASK_DEBUG=1
    SQLALCHEMY_TRACK_MODIFICATIONS=True

class DevelopmentConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = r'sqlite:///X:\库\code\web_learn_flask\test\data.db'

class TestingConfig( Config):
    SQLALCHEMY_DATABASE_URI = r'sqlite:///X:\库\code\web_learn_flask\test\test_data.db'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}