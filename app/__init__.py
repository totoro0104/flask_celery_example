from __future__ import absolute_import
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from celery import Celery

from config import config, Config
from celery_l import make_celery

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    return app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
celery = make_celery(app)
