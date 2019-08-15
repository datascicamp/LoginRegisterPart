from app import app
from flask import jsonify, render_template


@app.route('/')
@app.route('/tutorial')
def usage():
    usages = [
        {'api_format': '/api/account/account-id/<int:account_id>', 'method': 'GET',
         'description': 'Get account by account_id'},
        {'api_format': '/api/account/account-email/<string:account_email>', 'method': 'GET',
         'description': 'Get account by account_email'},
        {'api_format': '/api/account/account-status/<string:account_status>', 'method': 'GET',
         'description': 'Get account by account_status'},
        {'api_format': '/api/account/all-accounts', 'method': 'GET',
         'description': 'Get all accounts'},

        {'api_format': '/api/account/account-creating', 'method': 'POST',
         'description': 'Create new account'},
        {'api_format': '/api/account/account-updating', 'method': 'PUT',
         'description': 'Update account info'},
        {'api_format': '/api/account/validate-password', 'method': 'POST',
         'description': 'Verify username and password'},

        {'api_format': '/api/reset-password/token-receiving/<string:token>', 'method': 'GET',
         'description': 'Receive reset password token'},
        {'api_format': '/api/registration/token-receiving/<string:token>', 'method': 'GET',
         'description': 'Receive registration password token'},

        {'api_format': '/api/registration/token-creating/account-email/<string:account_email>', 'method': 'GET',
         'description': 'Get registration token by account_email'},
        {'api_format': '/api/registration/token-creating/account-id/<string:account_id>', 'method': 'GET',
         'description': 'Get registration token by account_id'},
        {'api_format': '/api/reset-password/token-creating/account-email/<string:account_email>', 'method': 'GET',
         'description': 'Get reset password token by account_email'},
        {'api_format': '/api/reset-password/token-creating/account-id/<string:account_id>', 'method': 'GET',
         'description': 'Get reset password token by account_id'},
    ]

    return render_template('frontPage.html', usage_infos=usages)

