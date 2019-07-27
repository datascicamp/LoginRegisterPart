from app import app
from flask import jsonify


@app.route('/usage')
def usage():
    usage = [
        {'api_format': '/users/uid/<int:uid>', 'method': 'GET', 'description': 'Get user info by uid'},
        {'api_format': '/users/username/<string:username>', 'method': 'GET', 'description': 'Get user info by username'},
        {'api_format': '/users/phone_number/<phone_number>', 'method': 'GET', 'description': 'Get user info by phone number'},
        {'api_format': '/users', 'method': 'GET', 'description': 'Get all users info'},
        {'api_format': '/users', 'method': 'POST', 'description': 'Create a new user'},
        {'api_format': '/users', 'method': 'PUT', 'description': 'Update user info'},
        {'api_format': '/users/validation/', 'method': 'POST', 'description': 'Verify password'}
    ]

    return jsonify(usage)
