from flask_restful import Api

from app.api.auth import Login, Test


def generate_routes(app):
    api = Api(app, prefix='/api')

    # auth
    api.add_resource(Login, '/auth/login')
    api.add_resource(Test, '/auth/test')
