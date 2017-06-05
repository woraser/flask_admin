from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response, session, json
from flask_sqlalchemy import get_debug_queries
from . import main
from ..models import User

@main.before_app_request
def before_request():
    if str(request.url_rule) != '/auth/login' and session.get('is_login') is None:
        return redirect(url_for('auth.login'))

@main.after_app_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= current_app.config['FLASKY_SLOW_DB_QUERY_TIME']:
            current_app.logger.warning(
                'Slow query: %s\nParameters: %s\nDuration: %fs\nContext: %s\n'
                % (query.statement, query.parameters, query.duration,
                   query.context))
    return response


@main.route('/shutdown')
def server_shutdown():
    if not current_app.testing:
        abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/index', methods=['GET', 'POST'])
def default():
    return render_template('index.html')

@main.route('/sensorIndex', methods=['GET'])
def sensorIndex():
    return render_template('sensorSetting.html')

@main.route('/sensorTableData', methods=['GET', 'POST'])
def sensorTableData():
    data = []
    data.append({
        'id': '1',
        'no': '2',
        'name': '3',
        'cycle': '4'
    })
    response = {}
    response['data'] = data
    return json.dumps(response)