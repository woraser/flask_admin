#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Title:

from flask import render_template, json, session, redirect, url_for, request
from . import main
import systemInfo,random,configSingle
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

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
    configInfo = configSingle.getNodeConfig()
    return render_template('index.html', dashboard=dashboard, configInfo=configInfo)

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

