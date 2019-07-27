from app import app
from flask import jsonify


@app.route('/usage')
def usage():
    usage = [
        {'api_format': '/api/account-id/<int:account_id>', 'method': 'GET', 'description': 'Get account by account_id'},
        {'api_format': '/api/account-email/<string:account_email>', 'method': 'GET', 'description': 'Get account by account_email'},
        {'api_format': '/api/account-status/<string:account_status>', 'method': 'GET', 'description': 'Get account by account_status'},
        {'api_format': '/api/all-accounts', 'method': 'GET', 'description': 'Get all accounts info'},
        {'api_format': '/api/create-account', 'method': 'POST', 'description': 'Create a new account'},
        {'api_format': '/api/update-account', 'method': 'PUT', 'description': 'Update account info'},
        {'api_format': '/api/validate-password', 'method': 'POST', 'description': 'Verify password'}
    ]

    return jsonify(usage)
