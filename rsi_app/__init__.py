from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'
db = SQLAlchemy(app)

from rsi_app.core import models
from rsi_app.core import routes
from rsi_app.core import resources
app.register_blueprint(routes.core)

db.create_all()

api.add_resource(resources.User, '/usuario/<string:cpf>')
api.add_resource(resources.UserLogin, '/usuario/login')
api.add_resource(resources.UserLogout, '/usuario/logout')
api.add_resource(resources.Transfer, '/transferir')
api.add_resource(resources.Account, '/conta/<int:id>')
api.add_resource(resources.AccountDeposit, '/conta/adicionarSaldo')
api.add_resource(resources.Extract, '/extrato/<int:id_conta>')
