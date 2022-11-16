from flask_restful import Resource
from api.stream import *
from flask_jwt_extended import jwt_required


class Home(Resource):

    @jwt_required()
    def get(self):
        return {'dsadasd':'31'}
