import datetime
# allow to set variable is_active=True and to stay connected
from flask_login import UserMixin
import logging as lg
from werkzeug.security import generate_password_hash
import csv
import difflib as dif
from . import db

class Users(db.Model, UserMixin):

    id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True)
    last_name = db.Column(db.String(length=30), nullable=False)
    first_name = db.Column(db.String(length=30), nullable=False)
    email_address = db.Column(db.String(length=50),nullable=False, unique=True)
    password_hash = db.Column(db.String(length=200), nullable=False)
    is_admin = db.Column(db.Boolean(), nullable=False, default=False)

    def __repr__(self):
        return f'{self.last_name} {self.first_name}'

    def json_id(self):
        return {
            'id': self.id, 
            'last_name': self.last_name, 
            'first_name': self.first_name,
            'email_address': self.email_address,
            'is_admin': self.is_admin
            }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


def init_db():
    db.drop_all()
    db.create_all()
    Users(last_name="HADDOU", first_name= "ayoub1", email_address= "ayoub1@gmail.com", password_hash= generate_password_hash("1234", method='sha256'), is_admin=True).save_to_db()
    