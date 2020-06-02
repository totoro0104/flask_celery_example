from sqlalchemy import or_
from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models import User


class Token(Resource):
    @staticmethod
    def get():
        account = request.args.get('account', None)
        passwd = request.args.get('passwd', None)
        if account and passwd:
            user = User.query.filter(or_(User.username == account,
                                         User.phone == account)).first()
            if user.verify_password(passwd):
                return {
                    'token': user.access_token(),
                    'expiration': '12H'
                }
            else:
                return {
                    'msg': 'Incorrect password'
                }
        else:
            return {
                    'msg': 'Missing account or password'
                }

    @staticmethod
    @jwt_required
    def post():
        user = User.query.get(get_jwt_identity()['uid'])
        return {
            'token': user.access_token(),
            'expiration': '12H'
        }
