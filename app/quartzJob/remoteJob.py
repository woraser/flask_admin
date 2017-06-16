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

def post_db_data():
    domain_address = ConfigObj().get("internet_conf", 'remote_address')
    post_url = ""
    post_data = getSyncDbData()
    requests.post(post_url, json.dumps(post_data))
    pass


def getSyncDbData():
    response = {}
    email_data = queryTotalByCls("EngineerEmail")
    sensor_setting = queryTotalByCls("Sensor")
    if email_data:
        response["email"] = convertDbObjToDict(email_data, "EngineerEmail")
    if sensor_setting:
        response["sensor"] = convertDbObjToDict(sensor_setting, "Sensor")
    return response
    pass


# 获取传感器采集数据 数据上限 200
def getSyncSensorData(limit=200):
    cursor = SensorData.select().where(SensorData.is_post==False).limit(limit)
    return cursor
    pass


def getSensorSetting():
    email_data = queryTotalByCls("Sensor")
    if not email_data:
        return None
    pass
    pass

def getEmailData():
    email_data = queryTotalByCls("EngineerEmail")
    if not email_data:
        return None
    pass

def getSystemInfo():
    pass

@catchDbException
def getUnPostSensorData():
    return SensorData.select().where(SensorData.is_post==False).limit(limit)