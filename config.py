import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    JWT_SECRET_KEY = 'hard to guess string'
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Token'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://' + os.path.join(basedir, 'data-test.sqlite')
    RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
