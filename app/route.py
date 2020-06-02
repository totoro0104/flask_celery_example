from flask_restful import Api

from app.api.auth import Token


def generate_routes(app):
    api = Api(app, prefix='/api')

    api.add_resource(Token, '/auth/token')
