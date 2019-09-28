from flask_restful import reqparse

def add_arguments_to_parser(parser, arguments):
    for field in arguments:
        parser.add_argument(
            field, help='This field cannot be blank', required=True
        )

user_registration_parser = reqparse.RequestParser()
account_registration_parser = reqparse.RequestParser()
account_deposit_parser = reqparse.RequestParser()
extract_insertion_parser = reqparse.RequestParser()
transfer_parser = reqparse.RequestParser()
login_parser = reqparse.RequestParser()

user_fields = (
    'email', 'password', 'nome', 'sobrenome', 'dataNascimento', 'cpf'
)
account_fields = ('id', 'cpf')
account_deposit_fields = ('conta', 'valor')
extract_fields = ('conta', 'data', 'valor')
transfer_fields = ('contaDestino', 'contaOrigem', 'valor')
login_fields = ('cpf', 'password')

add_arguments_to_parser(user_registration_parser, user_fields)
add_arguments_to_parser(account_registration_parser, account_fields)
add_arguments_to_parser(account_deposit_parser, account_deposit_fields)
add_arguments_to_parser(extract_insertion_parser, extract_fields)
add_arguments_to_parser(transfer_parser, transfer_fields)
add_arguments_to_parser(login_parser, login_fields)
