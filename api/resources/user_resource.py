from flask_jwt_extended import create_access_token, jwt_required, current_user, get_jwt_identity
from flask import jsonify, json
from models.user_model import *
from common.encoder import MongoEncoder
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash


class User(Resource):
    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('username', type=str, required=True,
                        help='This field cannot be left blank')

    parser.add_argument('password', type=str, required=True,
                        help='This field cannot be left blank')

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
        mail = data['mail']
        cell = data['cell']
        password = data['password']

        if UserModel.getquery_name(username) or UserModel.getquery_mail(mail):
            return {'message': 'Username or email has already been created, aborting.'}, 400

        user = UserModel(
            username=username,
            mail=mail,
            cell=cell,
            password=UserModel.hash_password(password)
        )
        user.save()

        return {'message': 'user has been created successfully.'}, 201


from utils import *


class DeleteUser(Resource):

    @jwt_required()
    def get(self):
        user_id = str_to_dict(get_jwt_identity())['_id']['$oid']
        UserModel.objects(id=user_id).delete()
        pass
