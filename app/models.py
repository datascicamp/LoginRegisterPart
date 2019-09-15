from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from time import time
import jwt
from app import app


class Account(db.Model):
    # name of database
    __tablename__ = "AccountInfo"
    account_id = db.Column(db.Integer, primary_key=True)
    account_email = db.Column(db.String(128), index=True, unique=True)
    account_nickname = db.Column(db.String(128), index=True)
    password_hash = db.Column(db.String(128))
    account_status = db.Column(db.String(8))
    account_create_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<\naccount_email = {}\naccount_nickname = {}\naccount_status = {}\naccount_create_time = {}\n>'\
            .format(self.account_email, self.account_nickname, self.account_status, self.account_create_time)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # for api usage
    def to_dict(self):
        data = {
            'account_id': self.account_id,
            'account_email': self.account_email,
            'account_nickname': self.account_nickname,
            'account_status': self.account_status,
            'account_create_time': self.account_create_time
        }
        return data

    # for email sending - register verification
    def get_register_token(self, expires_in=1800):
        data_structure = {'registration': self.account_id, 'exp': time() + expires_in}
        ciphered_msg = jwt.encode(data_structure, app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')
        return ciphered_msg

    @staticmethod
    def verify_register_token(token):
        try:
            account_id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['registration']
        except:
            return
        return Account.query.get(account_id)

    # for email sending - password resetting
    def get_reset_password_token(self, expires_in=1800):
        data_structure = {'reset_password': self.account_id, 'exp': time() + expires_in}
        ciphered_msg = jwt.encode(data_structure, app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')
        return ciphered_msg

    @staticmethod
    def verify_reset_password_token(token):
        try:
            account_id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            return
        return Account.query.get(account_id)
