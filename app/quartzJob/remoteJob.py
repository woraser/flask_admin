#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/14
# Title:远程同步脚本，用于同步传感器数据(db:Sensor)，配置文件，邮箱数据(db:EngineerEmail)
# Tip:
from ..common.dbFactory import queryTableByCls
from ..models import SensorData, Sensor
from ..decoratorUtil import catchDbException
from ..commonUtil import convertDbObjToDict
from ..main.configSingle import ConfigObj
import requests, json

# 推送传感器采集数据
def postSensorData():
    domain_address = ConfigObj().config_obj.get("internet_conf", 'remote_address')
    post_url = "/".join(["http:/", domain_address, "services/test.lua"])
    post_data = __getSyncSensorData()
    post_array, id_array = __buildPostData(post_data)
    if post_array and id_array:
        res = requests.post(post_url, json.dumps({"post_data": post_array}))
        if res.content and json.loads(res.content)["status"] == 1:
            __updateSensorDataStatus(id_array)
            pass
    pass

#  推送传感器数据
def postSensor():
    sensor_data = __getSyncSensor()
    # 同步传感器数据
    if sensor_data:
        requests.post("url", "")
        pass

    pass

# 获取节点上所有的传感器数据
def __getSyncSensor():
    response = {}
    sensor_setting = queryTableByCls(Sensor, limit=200)
    if sensor_setting:
        response["sensor"] = convertDbObjToDict(sensor_setting, Sensor)
    return response
    pass


# 获取未发送的传感器采集数据 每次数量：200
def __getSyncSensorData(limit=100):
    cursor = __getUnPostSensorData(limit)
    return cursor
    pass

@catchDbException
def __getUnPostSensorData(limit):
    return SensorData.select().where(SensorData.is_post==False).order_by(SensorData.id.desc()).limit(limit)

# 构建传感器采集数据的 推送结构
def __buildPostData(data=None):
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

# 传感器采集数据推送完成之后 修改推送状态 避免二次推送
def __updateSensorDataStatus(id_array=None):
    SensorData.update(is_post=True).where(SensorData.id << id_array).execute()
    pass