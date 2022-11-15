from flask_jwt_extended import create_access_token
from flask import jsonify, json
from api.models.user_model import *
from api.common.encoder import MongoEncoder
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash


class User(Resource):
    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('username', type=str, required=True,
                        help='This field cannot be left blank')

    parser.add_argument('password', type=str, required=True,
                        help='This field cannot be left blank')

    def get(self):
        pass

    def post(self):
        data = User.parser.parse_args()
        username_mail = data['username']
        password = data['password']
        b_name = UserModel.check_name(username_mail)
        if b_name:
            user = UserModel.getquery_name(username_mail)
            if check_password_hash(user.password, password):
                access_token = create_access_token(
                    identity=json.dumps(user, cls=MongoEncoder))
                return jsonify(access_token=access_token)

        # b_mail = UserModel.check_mail(username_mail)
        #
        # if b_mail:
        #     print('annanananananana')
        #     user = UserModel.getquery_mail(username_mail)
        #     if check_password_hash(user.password, password):
        #         access_token = create_access_token(
        #             identity=json.dumps(user, cls=MongoEncoder))
        #         return jsonify(access_token=access_token)

        return {'message': 'Wrong username or password.'}, 401


class UserRegister(Resource):
    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('username', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('mail', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('cell', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True,
                        help='This field cannot be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()
        username = data['username']
        mail = data['mai']
        cell = data['cell']
        password = data['password']
