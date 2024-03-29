from datetime import datetime

from passlib.hash import pbkdf2_sha256 as sha256

from rsi_app import db


friendship = db.Table(
    'friendship',
    db.Column(
        'friend_a_cpf',
        db.Integer,
        db.ForeignKey('user.cpf'),
        primary_key=True
    ),
    db.Column(
        'friend_b_cpf',
        db.Integer,
        db.ForeignKey('user.cpf'),
        primary_key=True
    )
)


class User(db.Model):
    cpf = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(100),
        nullable=False
    )
    surname = db.Column(
        db.String(200),
        nullable=False
    )
    birth_date = db.Column(
        db.String(10),
        nullable=False,
    )
    email = db.Column(
        db.String(100),
        nullable=False
    )
    password = db.Column(
        db.String(100),
        nullable=False
    )
    street = db.Column(
        db.String(100),
        nullable=True
    )
    number = db.Column(
        db.Integer,
        nullable=True
    )
    neighborhood = db.Column(
        db.String(100),
        nullable=True
    )
    city = db.Column(
        db.String(100),
        nullable=True
    )
    state = db.Column(
        db.String(100),
        nullable=True
    )
    accounts = db.relationship(
        'Account',
        backref='user',
        lazy=True
    )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_info(self, new_info):
        User.query.filter_by(cpf=self.cpf).update(new_info)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return dict(
            cpf=self.cpf,
            nome=self.name,
            sobrenome=self.surname,
            dataNascimento=self.birth_date,
            email=self.email,
            rua=self.street,
            numero=self.number,
            bairro=self.neighborhood,
            natal=self.city,
            estado=self.state,
        )

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    @classmethod
    def find_by_cpf(cls, cpf):
        return cls.query.filter_by(cpf=cpf).first()


class Account(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    balance = db.Column(
        db.Float,
        default=0.0
    )
    cpf = db.Column(
        db.Integer,
        db.ForeignKey('user.cpf'),
        nullable=False
    )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return dict(
            conta=self.id,
            saldo=self.balance
        )

    def delete_account(self):
        db.session.delete(self)
        db.session.commit()

    def update_balance(self, value):
        self.balance += value
        db.session.commit()

    def reset_balance(self, value):
        self.balance = 0
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()


class Extract(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    date = db.Column(
        db.Date,
        default=datetime.utcnow
    )
    value = db.Column(
        db.Float,
        nullable=False
    )
    description = db.Column(
        db.String(255)
    )
    account = db.Column(
        db.Integer,
        nullable=False
    )

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def to_dict(self):
        return dict(
            conta=self.account,
            data=self.date.isoformat(),
            descricao=self.description,
            valor=self.value
        )

    @classmethod
    def delete_all(cls, id_conta):
        db.session.query(cls).filter_by(account=id_conta).delete()
        db.session.commit()