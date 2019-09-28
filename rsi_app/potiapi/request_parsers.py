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

user_fields = (
    'email', 'password', 'name', 'surname', 'birth_date', 'cpf'
)
account_fields = ('id', 'cpf')
account_deposit_fields = ('conta', 'valor')
extract_fields = ('conta', 'data', 'valor')

add_arguments_to_parser(user_registration_parser, user_fields)
add_arguments_to_parser(account_registration_parser, account_fields)
add_arguments_to_parser(account_deposit_parser, account_deposit_fields)
add_arguments_to_parser(extract_insertion_parser, extract_fields)
