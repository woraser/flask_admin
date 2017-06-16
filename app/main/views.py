from flask import render_template, json, session, redirect, url_for, request
from . import main
import systemInfo,random

@main.before_request
def before_request():
    if str(request.url_rule) != '/auth/login' and session.get('is_login') is None:
        return redirect(url_for('auth.login'))

@main.after_app_request
def after_request(response):
    return response

@main.route('/', methods=['GET', 'POST'])
def index():
    dashboard = systemInfo.getDashboard()
    return render_template('index.html', dashboard=dashboard)

@main.route('/index', methods=['GET', 'POST'])
def default():
    return redirect(url_for('main.index'))

@main.route('/systemPieInfo')
def getSystemInfo():
    # res = {
    #     "cpu_free": systemInfo.getCpuFree(),
    #     "ram_usage": systemInfo.getRamUsage()
    # }
    res = {
        "cpu_free": random.randint(0, 100),
        "ram_usage": random.randint(0, 100)
    }
    return json.dumps(res)

@main.route('/systemLineInfo')
def getSystemInfoHistory():
    response = systemInfo.getSystemHistory()
    return json.dumps(response)

