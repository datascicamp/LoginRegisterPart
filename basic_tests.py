from app import db
from app.models import Account
import requests

if __name__ == '__main__':

    requests.post('http://127.0.0.1:5000/api/email-sending-by-account-id', data={'account_id': '1'})
    pass
