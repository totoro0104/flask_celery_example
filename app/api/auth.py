from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, current_user

from app.models import User


class Login(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument("account", type=str)
        parser.add_argument("passwd", type=str)

        args = parser.parse_args()
        account, passwd = args['account'], args['passwd']
        user = User.query.filter_by(username=account).first()
        if not user:
            return {
                'code': 0,
                'msg': 'Incorrect password or account!',
                'data': None
            }
        if user.verify_password(passwd):
            return {
                'code': 1,
                'data': {
                    'token': user.access_token(user.id),
                    'expiration': '12H'
                },
                'msg': 'Success'
            }
        else:
            return {
                'code': 0,
                'msg': 'Incorrect password or account!',
                'data': None
            }


class Test(Resource):
    @staticmethod
    @jwt_required()
    def get():
        data = {'uid': current_user.id}
        return {
            'data': data
        }
