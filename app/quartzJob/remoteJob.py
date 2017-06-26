#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/14
# Title:远程同步脚本，用于同步传感器数据(db:Sensor)，配置文件，邮箱数据(db:EngineerEmail)
# Tip:
from ..common.dbFactory import queryTotalByCls
from ..models import SensorData
from ..decoratorUtil import catchDbException
from ..commonUtil import convertDbObjToDict
from ..main.configSingle import ConfigObj
import requests, json

# 对比推送数据库数据
def post_db_data():
    domain_address = ConfigObj().get("internet_conf", 'remote_address')
    post_url = ""
    post_data = getSyncSensor()
    requests.post(post_url, json.dumps(post_data))
    pass

# 获取等待同步的传感器数据
def getSyncSensor():
    response = {}
    sensor_setting = queryTotalByCls("Sensor")
    if sensor_setting:
        response["sensor"] = convertDbObjToDict(sensor_setting, "Sensor")
    return response
    pass


# 获取未发送的传感器采集数据 每次数量：200
def getSyncSensorData():
    cursor = getUnPostSensorData()
    return cursor
    pass

@catchDbException
def getUnPostSensorData():
    return SensorData.select().where(SensorData.is_post==False).order_by(SensorData.id.desc()).limit(limit)