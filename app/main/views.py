from flask import render_template, json, session, redirect, url_for, request
from . import main
import sensorCollect
@main.before_app_request
def before_request():
    if str(request.url_rule) != '/auth/login' and session.get('is_login') is None:
        return redirect(url_for('auth.login'))

@main.after_app_request
def after_request(response):
    return response

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
    # data = []
    data.append({
        'id': '1',
        'no': '2',
        'name': '3',
        'cycle': '4'
    })
    # response = {}
    response['data'] = data
    return json.dumps(response)

@main.route('/getSensorData', methods=['GET'])
def getSensorData():
    sensorCollect.getTestData()
    pass