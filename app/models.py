from datetime import datetime, timedelta

from flask_login import UserMixin
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(16), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def access_token(self, expire_time=timedelta(hours=12)):
        data = {
            'uid': self.id
        }
        return create_access_token(identity=data, expires_delta=expire_time)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
