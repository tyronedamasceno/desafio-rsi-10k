from datetime import datetime

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
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
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
