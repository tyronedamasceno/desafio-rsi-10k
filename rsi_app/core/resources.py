from flask_restful import Resource


class User(Resource):
    def post(self):
        return {'tamo': 'aqui'}
    
    def get(self, cpf=None):
        return {'isso': 'foi um get'}

    def put(self):
        return {'tem put': 'nesse role'}

    def delete(self, cpf=None):
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
    
    def get(self, id_conta=None):
        return {'isso': 'foi um get'}

    def delete(self, id_conta=None):
        return {'naaaao': 'pq me deletas?'}     


class Account(Resource):
    def post(self, valor=None):
        return {'tamo': 'aqui'}

    def get(self):
        return {'isso': 'foi um get'}

    def delete(self):
        return {'naaaao': 'pq me deletas?'}


class AccountDeposit(Resource):
    def post(self):
        return {'oia': 'a grana entrando'}
