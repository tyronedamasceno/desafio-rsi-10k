from flask import jsonify
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('email', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)

DOC_URL = 'github.com/tyronedamasceno/desafio-rsi-10k/blob/master/docs.md'


class HomeResource(Resource):
    def get(self):
        return jsonify(
            message='Welcome to Poti-API',
            documentation=f'Please, look Poti-API documentation at {DOC_URL}')

class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        return data

    def put(self):
        return {'tem put': 'nesse role'}


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
