from app import db
from app.models import Account
import requests

if __name__ == '__main__':

    # sending email by account_id
    # requests.post('http://127.0.0.1:5000/api/email-sending-by-account-id', data={'account_id': '1'})

    # sending email by account_email
    # requests.post('http://127.0.0.1:5000/api/email-sending-by-account-email',
    # data={'account_email': 'herbwang1989@gmail.com'})

    # sending email by account_email
    requests.put('http://127.0.0.1:4998/api/account/account-updating',
                  data={'account_email': 'mike@yeah.net', 'account_nickname': '胖球球', 'password': '123'})

    pass
