from app import app, db
from app.models import Account
from flask import jsonify
from flask import request
from werkzeug.http import HTTP_STATUS_CODES


# get account by account_id
@app.route('/api/account-id/<int:account_id>', methods=['GET'])
def get_user_by_uid(account_id):
    data = list()
    data.append(Account.query.get_or_404(account_id).to_dict())
    return jsonify(data)


# get account by account_email
@app.route('/api/account-email/<string:account_email>', methods=['GET'])
def get_user_by_username(account_email):
    data = list()
    data.append(Account.query.filter(Account.account_email == account_email).first_or_404().to_dict())
    return jsonify(data)


# get account by account_status
@app.route('/api/account-status/<string:account_status>', methods=['GET'])
def get_user_by_phone_number(account_status):
    data = list()
    for account in Account.query.filter(Account.account_status == account_status).all():
        data.append(account.to_dict())
    return jsonify(data)


# get all accounts
@app.route('/api/all-accounts', methods=['GET'])
def get_all_users():
    data = list()
    for account in Account.query.all():
        data.append(account.to_dict())
    return jsonify(data)


# create new account
@app.route('/api/create-account', methods=['POST'])
def create_new_user():
    account_email = request.form.get('account_email')
    password = request.form.get('password')

    # check faults
    if password is None or account_email is None:
        return bad_request('This post must include both account_email and password fields.')
    if Account.query.filter_by(account_email=account_email).first():
        return bad_request('please use a different account_email.')

    # db operations
    new_account = Account(account_email=account_email)
    new_account.set_password(password)
    db.session.add(new_account)
    db.session.commit()

    # response data
    data = list()
    # This account_email is the one which user input in POST form
    data.append(Account.query.filter(Account.account_email == account_email).first_or_404().to_dict())

    return jsonify(data)


# update account info
@app.route('/api/update-account', methods=['PUT'])
def update_user():
    account_email = request.form.get('account_email')
    if account_email is None:
        return bad_request('This post must include account_email field.')

    # get PUT data
    password = request.form.get('password') or None
    account_status = request.form.get('account_status') or None

    # take out data form db
    account = Account.query.filter_by(account_email=account_email).first()

    # update procedure
    if password is not None:
        account.set_password(password)
    # Mention that user mustn't change their account_email without re-validate their email
    if account_email is not None:
        account.account_email = account_email
    if account_status is not None:
        account.account_status = account_status

    # update db
    db.session.add(account)
    db.session.commit()

    # response data
    data = list()
    # This username is the one which user input in POST form
    data.append(Account.query.filter(Account.account_email == account_email).first_or_404().to_dict())

    return jsonify(data)


# verify username and password
@app.route('/api/validate-password/', methods=['POST'])
def validate_password():
    # Get user information from POST
    account_email = request.form.get('account_email')
    password = request.form.get('password')

    # if there is no password field or account_email field in post
    if password is None or account_email is None:
        return bad_request('This post must include both username and password fields.')
    account = Account.query.filter(Account.account_email == account_email).first()
    if account is None:
        return jsonify([{'account_id': -1, 'account_email': account.account_email,
                         'account_status': 'Unavailable', 'password_validation': 'False'}])
    validate = account.check_password(password)

    # authentication verify success.
    if validate is True:
        return jsonify([{'account_id': account.account_id, 'account_email': account.account_email,
                         'account_status': account.account_status, 'password_validation': 'True'}])
    # authentication verify failed.
    return jsonify([{'account_id': -1, 'account_email': account.account_email,
                     'account_status': 'Unavailable', 'password_validation': 'False'}])


# bad requests holder
def bad_request(message):
    return error_response(400, message)


# error response
def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response
