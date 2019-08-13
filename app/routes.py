from app import app
from flask import jsonify, render_template


@app.route('/')
@app.route('/tutorial')
def usage():
    usages = [
        {'api_format': '/api/competition/all-competitions', 'method': 'GET',
         'description': 'Get all competition infos'},
        {'api_format': '/api/competition/competition-name/<string:competition_name>', 'method': 'GET',
         'description': 'Get competitions info by its competition name'},
        {'api_format': '/api/competition/contributor-id/<string:contributor_id>', 'method': 'GET',
         'description': 'Get competitions by its owner(contributor_id)'},
        {'api_format': '/api/competition/hostname/<string:hostname>', 'method': 'GET',
         'description': 'Get competitions by its hostname'},
        {'api_format': '/api/competition/scenario/<string:scenario>', 'method': 'GET',
         'description': 'Get competitions by its scenario'},
        {'api_format': '/api/competition/data-feature/<string:data_feature>', 'method': 'GET',
         'description': 'Get competitions by its data feature'},
        {'api_format': '/api/competition/rid/<string:rid>', 'method': 'GET',
         'description': 'Get one competition info by its _id'},
        {'api_format': '/api/competition', 'method': 'POST',
         'description': 'Insert new competition infos'},
        {'api_format': '/api/competition/<string:rid>', 'method': 'PUT',
         'description': 'Modify an existed competition info'},
        {'api_format': '/api/competition/<string:rid>', 'method': 'DELETE',
         'description': 'Delete an existed competition info'},
        {'api_format': '/api/competition/comp-search/fuzzy/<string:keyword>', 'method': 'GET',
         'description': 'Fuzzy Search by comp_title, comp_host_name, comp_scenario or data_feature'},
    ]

    return render_template('frontPage.html', usage_infos=usages)

