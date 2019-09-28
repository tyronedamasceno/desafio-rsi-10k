from flask import jsonify
from flask_restful import Resource

from rsi_app import DEPOSIT_TRANSACTION, TRANSFER_TRANSACTION
from rsi_app.potiapi.models import User as UserModel, Account as AccountModel
from rsi_app.potiapi.request_parsers import (
    account_registration_parser, user_registration_parser,
    account_deposit_parser
)

DOC_URL = 'github.com/tyronedamasceno/desafio-rsi-10k/blob/master/docs.md'


class HomeResource(Resource):
    def get(self):
        return jsonify(
            message='Welcome to Poti-API',
            documentation=f'Please, look Poti-API documentation at {DOC_URL}')

class UserRegistration(Resource):
    def post(self):
        data = user_registration_parser.parse_args()
        if UserModel.find_by_cpf(data['cpf']):
            return {'message': 'An user with this CPF already exists'}, 400
        new_user = UserModel(**data)
        try:
            new_user.save_to_db()
        except:
            return {'message': 'Something went wrong'}, 400
        return {'message': 'User successfully created'}, 201

    def put(self):
        data = user_registration_parser.parse_args()
        existent_user = UserModel.find_by_cpf(data['cpf'])
        if not existent_user:
            return {'message': 'Dont exists an user with this CPF'}, 404
        existent_user.update_info(data)
        return {'message': 'User successfully updated'}, 200


class User(Resource):
    def get(self, cpf):
        if isinstance(cpf, (str, bytes)):
            try:
                cpf = int(cpf.replace('.', '').replace('-', ''))
            except ValueError:
                return {'message': 'Invalid CPF'}, 400
        
        user = UserModel.find_by_cpf(cpf)
        if not user:
            return {'message': 'Dont exists an user with this CPF'}, 404
        return user.to_dict(), 200

    def delete(self, cpf):
        if isinstance(cpf, (str, bytes)):
            try:
                cpf = int(cpf.replace('.', '').replace('-', ''))
            except ValueError:
                return {'message': 'Invalid CPF'}, 400

        user = UserModel.find_by_cpf(cpf)
        if not user:
            return {'message': 'Dont exists an user with this CPF'}, 404
        user.delete_user()
        return {'message': 'User successfully deleted'}, 204


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
        data = account_registration_parser.parse_args()

        if AccountModel.find_by_id(data['id']):
            return {'message': 'An account with this ID already exists'}, 400
        if not UserModel.find_by_cpf(data['cpf']):
            return {'message': 'This CPF does not belong to a registered user'}, 400
        new_account = AccountModel(**data)
        try:
            new_account.save_to_db()
        except:
            return {'message': 'Something went wrong'}, 400
        return {'message': 'Account successfully created'}, 201


class Account(Resource):
    def get(self, id):
        account = AccountModel.find_by_id(id)
        if not account:
            return {'message': 'Dont exists an account with this ID'}, 404
        return account.to_dict(), 200

    def delete(self, id):
        account = UserModel.find_by_id(id)
        if not account:
            return {'message': 'Dont exists an account with this ID'}, 404
        account.delete_account()
        return {'message': 'Account successfully deleted'}, 204


class AccountDeposit(Resource):
    def post(self):
        data = account_deposit_parser.parse_args()
        account = AccountModel.find_by_id(data['conta'])
        if not account:
            return {'message': 'Dont exists an account with this ID'}, 404
        if isinstance(data['valor'], (str, bytes)):
            try:
                data['valor'] = float(data['valor'].replace(',', '.'))
            except ValueError:
                return {'message': 'Invalid deposit value'}, 400

        if data['valor'] < 0:
            return {'message': 'Invalid deposit value'}, 400

        account.update_balance(data['valor'])
        # create_transaction(DEPOSIT_TRANSACTION, conta, valor, now)
        return {'message': 'Deposit successfully'}
