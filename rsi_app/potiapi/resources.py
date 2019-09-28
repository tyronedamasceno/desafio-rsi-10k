from flask import jsonify
from flask_restful import Resource, reqparse

from rsi_app.potiapi.models import User as UserModel

registration_parser = reqparse.RequestParser()
register_required_fields = (
    'email', 'password', 'name', 'surname', 'birth_date', 'cpf'
)
for field in register_required_fields:
    registration_parser.add_argument(
        field, help='This field cannot be blank', required=True
    )

DOC_URL = 'github.com/tyronedamasceno/desafio-rsi-10k/blob/master/docs.md'


class HomeResource(Resource):
    def get(self):
        return jsonify(
            message='Welcome to Poti-API',
            documentation=f'Please, look Poti-API documentation at {DOC_URL}')

class UserRegistration(Resource):
    def post(self):
        data = registration_parser.parse_args()
        if UserModel.find_by_cpf(data['cpf']):
            return {'message': 'An user with this CPF already exists'}, 400
        new_user = UserModel(**data)
        try:
            new_user.save_to_db()
        except:
            return {'message': 'Something went wrong'}, 400
        return {'message': 'User successfully created'}, 201

    def put(self):
        data = registration_parser.parse_args()
        existent_user = UserModel.find_by_cpf(data['cpf'])
        if not existent_user:
            return {'message': 'Dont exists an user with this CPF'}, 400
        existent_user.update_info(data)
        return {'message': 'User successfully updated'}, 200


class User(Resource):
    def get(self, cpf):
        return {'isso': 'foi um get'}

    def delete(self, cpf):
        return {'naaaao': 'pq me deletas?'}


class UserLogin(Resource):
    def post(self):
        return {}


class UserLogout(Resource):
    def get(self):
        return {}


class Transfer(Resource):
    def post(self):
        return {'vai': 'transferindooo'}


class Extract(Resource):
    def post(self):
        return {'tamo': 'aqui'}
    
    def get(self, id_conta):
        return {'isso': 'foi um get'}

    def delete(self, id_conta):
        return {'naaaao': 'pq me deletas?'}     


class AccountRegistration(Resource):
    def post(self):
        return {'tamo': 'aqui'}


class Account(Resource):
    def get(self, id):
        return {'isso': 'foi um get'}

    def delete(self, id):
        return {'naaaao': 'pq me deletas?'}


class AccountDeposit(Resource):
    def post(self, valor):
        return {'oia': 'a grana entrando'}
