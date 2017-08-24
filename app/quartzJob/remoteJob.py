#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/14
# Title:远程同步脚本，用于同步传感器数据(db:Sensor)，配置文件
# Tip:
from ..common.dbFactory import queryTableByCls
from ..models import SensorData, Sensor, RemoteCommand
from ..decoratorUtil import catchDbException
from ..commonUtil import convertDbObjToDict, getNowStr
from ..main.configSingle import ConfigObj
import requests, json

# 推送传感器采集数据
def postSensorData():
    print "postSensorData"
    s = requests.session()
    s.keep_alive = False
    domain_address = ConfigObj().config_obj.get("internet_conf", 'remote_address')
    post_url = "/".join(["http:/", domain_address, "services/test.lua"])
    post_data = getSyncSensorData()
    post_array, id_array = buildPostData(post_data)
    if post_array and id_array:
        # 使用{'Connection': 'close'}来处理ConnectionError: HTTPConnectionPool(): Max retries exceeded with url问题
        res = requests.post(post_url, json.dumps({"post_data": post_array}), headers={'Connection': 'close'})
        if res.content and json.loads(res.content)["status"] == 1:
            updateSensorDataStatus(id_array)
            pass
        # 添加远程命令
        if res.content and json.loads(res.content)["command"]:
            handleCommand(json.loads(res.content)["command"])
            pass
    pass

#  推送传感器数据
def postSensor():
    sensor_data = getSyncSensor()
    # 同步传感器数据
    if sensor_data:
        requests.post("url", "")
        pass

    pass

# 获取节点上所有的传感器数据
def getSyncSensor():
    response = {}
    sensor_setting = queryTableByCls(Sensor, limit=200)
    if sensor_setting:
        response["sensor"] = convertDbObjToDict(sensor_setting, Sensor)
    return response
    pass


# 获取未发送的传感器采集数据 每次数量：200
def getSyncSensorData(limit=100):
    cursor = getUnPostSensorData(limit)
    return cursor
    pass

@catchDbException
def getUnPostSensorData(limit):
    return SensorData.select().where(SensorData.is_post==False).order_by(SensorData.id.desc()).limit(limit)

# 构建传感器采集数据的 推送结构
def buildPostData(data=None):
    post_array = []
    id_array = []
    if data:
        for i in data:
            post_array.append({
                "param": i.param_name,
                "val": i.val,
                "collect_time": i.created_time,
                "sensor_no": i.sensor_no
            })
            id_array.append(i.id)
            pass
    return post_array, id_array
    pass


# 构建传感器数据的 推送结构
def buildSensorPost(data=None):
    post_array = []
    id_array = []
    if data:
        for i in data:
            post_array.append({
                "sensor_no": i.param_name,
                "max_limit": i.val,
                "min_limit": i.created_time,
                "rel_equ": i.created_time,
                "type": i.created_time,
                "interface": i.created_time,
                "min_limit": i.created_time,
                "accessPort": i.created_time,
                "is_used": i.created_time
            })
            id_array.append(i.id)
            pass
    return post_array, id_array
    pass

# 传感器采集数据推送完成之后 修改推送状态 避免二次推送
def updateSensorDataStatus(id_array=None):
    SensorData.update(is_post=True).where(SensorData.id << id_array).execute()
    pass


# 处理请求返回的command命令
# return None/True/False
def handleCommand(command=None):
    if command is None:
        return
    insert_row = {
        "json_text": command,
        "created_time": getNowStr(),
        "is_executed": False
    }
    try:
        RemoteCommand.insert(insert_row).execute()
        res = True
        pass
    except Exception:
        res = False
        pass
    return res
    pass

# 执行远程command
# return
# command={}
#
#
#

def executeCommand(command=None):
    command_dict = json.loads(command)
    command = {
        "id": "",
        "type": "",
        "sensor_no": "",
        "action": ""
    }
    pass