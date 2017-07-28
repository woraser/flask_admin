#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Title:

from flask import render_template, json, session, redirect, url_for, request
from . import main
from app.commonUtil import buildErr,buildSucc,buildNone
from app.common.dbFactory import findOneByClsAndId
from mainService import updateSensorByIdAndData,getDashboard, getSystemHistory,uploadConfigFile,getFileListFromUpload,downLoadFileFromServer, checkIsDownloaded
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

# 进入默认页面
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
    sensorInfo = findOneByClsAndId(Sensor, id)
    return render_template('sensorDetail.html', sensorInfo=sensorInfo)

# 进入文件管理页面
@main.route('/fileManger', methods=['GET'])
def fileManger():
    return render_template('fileManger.html')

# 获取饼状图数据
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
    return buildSucc("success")
    pass

# 获取单个传感器详情
@main.route('/sensorInfo/<string:id>', methods=['GET'])
def sensorInfo(id):
    record = findOneByClsAndId(Sensor, id)
    if record is None:
        return buildNone()
    return buildSucc(record)

# 修改单个传感器数据
@main.route('/sensorConfig/<string:id>', methods=['PUT'])
def sensorConfig(id):
    post_data = request.data
    result = updateSensorByIdAndData(id, json.loads(post_data))
    return buildSucc(result)

# 上传当前的配置文件至服务器
@main.route('/fileUpload', methods=['GET'])
def uploadConfig():
    # 文件上传
    res = uploadConfigFile()
    if isinstance(res, dict):
        return buildSucc(res)
    return buildErr("上传失败!")
    pass

# 分页获取上传配置文件列表
@main.route('/fileTableList', methods=['POST'])
def getFileList():
    post_data = request.json
    try:
        fileObject = getFileListFromUpload(int(post_data['pageNumber'])-1, post_data['pageSize'])
        fileList = fileObject["content"]
        for item in fileList:
            item["id"] = str(item["id"])
            item["objectId"] = str(item["objectId"])
            item["isDownload"] = checkIsDownloaded(item["objectId"])
            pass
        pass
    except Exception:
        fileList = []
        pass
    finally:
        response = {
            "data": fileList,
            "draw": post_data['draw'],
            "recordsTotal": fileObject["totalElements"],
            "recordsFiltered": fileObject["totalElements"],
        }
        return json.dumps(response)
    pass

# 从远处服务器下载文件至本地
@main.route('/downloadFile/<string:id>', methods=['GET'])
def downLoadFile(id):
    try:
        with open("app/static/file/{0}.ini".format(id), 'w') as f:
            downLoadFileFromServer(id, f)
            pass
            return buildSucc("ok")
        pass
    except Exception:
        return buildErr("no")
        pass
    pass

# 覆盖配置文件 重启项目
@main.route('/restartServer/<string:id>', methods=['GET'])
def restartServerWithConfig(id):
    # reload config from /app/static/file/id.ini to config.ini


    # restart server
    buildSucc("ok")
    pass