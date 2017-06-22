#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Title:

from flask import render_template, json, session, redirect, url_for, request
from . import main
from app.commonUtil import buildErr,buildSucc,buildNone
from app.common.dbFactory import findOneByClsAndId
from mainService import updateSensorByIdAndData,getDashboard, getSystemHistory
from app.models import Sensor
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

# 进入首页
@main.route('/', methods=['GET', 'POST'])
def index():
    dashboard = getDashboard()
    configInfo = configSingle.getNodeConfig()
    return render_template('index.html', dashboard=dashboard, configInfo=configInfo)

# 进入首页
@main.route('/index', methods=['GET', 'POST'])
def default():
    return redirect(url_for('main.index'))


# 进入传感器管理页面
@main.route('/sensorManger', methods=['GET'])
def sensorManger():
    return render_template('sensorManger.html')

# 进入传感器详情页面
@main.route('/sensorDetail/<id>', methods=['GET'])
def sensorDetail(id=None):
    if not id:
        redirect(url_for('main.sensorManger'))
    sensorInfo = findOneByClsAndId("Sensor", id)
    return render_template('sensorDetail.html', sensorInfo=sensorInfo)

# 获取饼状图数据
@main.route('/systemPieInfo')
def getSystemInfo():
    res = {
        "cpu_free": systemInfo.getCpuFree(),
        "ram_usage": systemInfo.getRamUsage()
    }
    # res = {
    #     "cpu_free": random.randint(0, 100),
    #     "ram_usage": random.randint(0, 100)
    # }
    return json.dumps(res)

# 获取折线图数据
@main.route('/systemLineInfo')
def getSystemInfoHistory():
    response = getSystemHistory()
    return json.dumps(response)

# 修改节点配置信息
@main.route('/nodeConfig', methods=['PUT'])
def updateNodeConfig():
    post_data = request.data
    configSingle.updateNodeConfig(json.loads(post_data))
    return json.dumps({"status": 1})
    pass

# 获取单个传感器详情
@main.route('/sensorInfo/<string:id>', methods=['GET'])
def sensorInfo(id):
    record = findOneByClsAndId("Sensor", id)
    if record is None:
        return buildNone()
    return buildSucc(record)

# 修改单个传感器数据
@main.route('/sensorConfig/<string:id>', methods=['PUT'])
def sensorConfig(id):
    post_data = request.data
    result = updateSensorByIdAndData(id, json.loads(post_data))
    return buildSucc(result)