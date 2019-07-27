from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Account(db.Model):
    # name of database
    __tablename__ = "AccountInfo"
    account_id = db.Column(db.Integer, primary_key=True)
    account_email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    account_status = db.Column(db.String(8))
    account_create_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<\naccount_email = {}\naccount_status = {}\naccount_create_time = {}\n>'\
            .format(self.acoount_email, self.account_status, self.account_create_time)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # for api usage
    def to_dict(self):
        data = {
            'account_id': self.account_id,
            'account_email': self.account_email,
            'account_status': self.account_status,
            'account_create_time': self.account_create_time
        }
        return data

