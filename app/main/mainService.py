#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/21
# Title:
# Tip:
from __future__ import division
from app.main import configSingle
from app.models import Sensor,SystemInfo
from systemInfo import getRunTime, getHardDiskTotal, getHardDiskUseage, getHardDiskUsed
from app.common.dbFactory import getTablePageByCls
import os



# 修改传感器数据
def updateSensorByIdAndData(id=None, update_data=None):
    update_data = {
        Sensor.sensor_no: update_data["sensor_no"],
        Sensor.max_limit: update_data["max_limit"],
        Sensor.min_limit: update_data["min_limit"],
        Sensor.job_time: int(update_data["job_time"])
    }
    return Sensor.update(update_data).where(Sensor.id == id).execute()


# build dict of dashboard for index
# 组装首页面板数据
def getDashboard():
    configInstance = configSingle.ConfigObj()
    config_obj = configInstance.config_obj
    dashboard_dict = {
        "id": config_obj.get("system_conf", "unique_id"),
        "GPS": config_obj.get("system_conf", "gps"),
        # "runtime": round(float(getRunTime())/60/60, 2),
        # "hd_total": str(round(getHardDiskTotal()/1024, 2))+"M",
        # "hd_usage": str(getHardDiskUseage())+"%"
        "runtime": int(200400 / 60 / 60),
        "hd_total": "250M",
        "hd_usage": "50%"
    }
    return dashboard_dict
    pass

# 获取系统运行参数历史记录
def getSystemHistory(limit=500):
    cursor = getTablePageByCls(SystemInfo, limit=limit, order=SystemInfo.id.desc(), condition=None)
    return cursor
    pass

