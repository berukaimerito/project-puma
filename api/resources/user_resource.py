from flask_jwt_extended import create_access_token, jwt_required, current_user, get_jwt_identity
from flask import jsonify, json, make_response
from models.user_model import *
from utils import *
from common.encoder import MongoEncoder
from flask_restful import Resource, reqparse
from flask_mail import Mail
from werkzeug.security import generate_password_hash, check_password_hash


class User(Resource):
    # msg = Message('Hello from the other side!', sender =   'peter@mailtrap.io', recipients = ['paul@mailtrap.io'])

    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('username', type=str, required=True,
                        help='This field cannot be left blank')

    parser.add_argument('password', type=str, required=True,
                        help='This field cannot be left blank')

    def post(self):
        data = User.parser.parse_args()
        user_name, password = data['username'], data['password']
        b_name = UserModel.check_name(user_name)
        if b_name:
            user = UserModel.getquery_name(user_name)
            if check_password_hash(user.password, password):
                access_token = create_access_token(identity=json.dumps(user, cls=MongoEncoder))

                user_r = {
                    "name": user.username,
                    "surname": user.surname,
                    "email": user.email,
                    "password": user.password
                }

                return jsonify(user_r, access_token)

        return {'message': 'Wrong username or password.'}, 401


class UserRegister(Resource):
    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('username', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('email', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('surname', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('confirm password', type=str, required=True,
                        help='This field cannot be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()
        username, email, surname, password, confirm = data['username'], data['email'], data['surname'], data[
            'password'], data['confirm password']

        if UserModel.getquery_name(username) or UserModel.getquery_mail(email):
            msg = {'message': 'Username or email has already been created, aborting.'}
            return make_response(jsonify(msg), 200)

        if password != confirm:
            msg = {'message': 'Passwords does not match.'}
            return make_response(jsonify(msg), 200)

        user = UserModel(
            username=username,
            surname=surname,
            email=email,
            password=UserModel.hash_password(password)
        )
        user.save()
        msg = {'message': 'User has been created successfully.'}

        return make_response(jsonify(user, msg), 200)


class DeleteUser(Resource):

    @jwt_required()
    def delete(self):
        user_id = str_to_dict(get_jwt_identity())['_id']['$oid']
        UserModel.objects(id=user_id).delete()
        pass
