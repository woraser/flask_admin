#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/21
# Title:
# Tip:
from __future__ import division
from app.main import configSingle
from app.models import Sensor, SystemInfo
from app.common.dbFactory import findOneByClsAndId
from app.common.dbFactory import getTablePageByCls
from app.quartzJob.schedulerJob import Quartz
from systemInfo import getRunTime,getHardDiskTotal,getHardDiskUseage
from fileUpDownLoad import fileUpload,fileDownloadList,fileDownLoad
import json, os

# 修改传感器数据
# 若采集任务周期改变 需要动态修改定时任务
def updateSensorByIdAndData(id=None, update_data=None):
    record = findOneByClsAndId(Sensor, id)
    if record:
        if record["job_time"] != int(update_data["job_time"]):
            quartz = Quartz()
            quartz.updateJobTimeForSensor(record["job_name"], update_data["job_time"], update_data["sensor_no"])
            pass
        pass
    # 更改数据的传感器数据
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

# 上传当前配置文件
def uploadConfigFile():
    configInstance = configSingle.ConfigObj()
    config_obj = configInstance.config_obj
    uniqueId = config_obj.get("system_conf", "unique_id")
    file_base_url = config_obj.get("internet_conf", "file_server")
    filePath = 'config.ini'
    url = "/".join([file_base_url, "fileUpload", "multipartFiles", uniqueId])
    with open(filePath, "rb") as file:
        res = fileUpload(file, url)
        if isinstance(res, str):
            res_dict = json.loads(eval(res))
            return res_dict
            pass
        return res
    pass

# 获取该iotx上传的配置文件列表
def getFileListFromUpload(offset, pagesize):
    configInstance = configSingle.ConfigObj()
    config_obj = configInstance.config_obj
    uniqueId = config_obj.get("system_conf", "unique_id")
    file_base_url = config_obj.get("internet_conf", "file_server")
    url = "/".join([file_base_url, "fileDownload", "list", uniqueId])
    url = url+"?page={0}&size={1}".format(offset, pagesize)
    # url格式为http://ip:port/fileDownload/list/{单片机SN}?page=0&size=10&sort=uploadtime,desc
    # url = "http://10.2.0.135:8080/fileDownload/list/iotx1"
    res = fileDownloadList(url)
    if res is None or len(res) == 0:
        return []
    return json.loads(res)
    pass

def downLoadFileFromServer(id, file):
    configInstance = configSingle.ConfigObj()
    config_obj = configInstance.config_obj
    file_base_url = config_obj.get("internet_conf", "file_server")
    url = "/".join([file_base_url, "fileDownload", id])
    fileDownLoad(url, file)

    pass

# 判断该文件是否已经下载
def checkIsDownloaded(objectId):
    fileDir = "app/static/file/{0}.ini".format(objectId)
    if os.path.exists(fileDir):
        return True
        pass
    return False
    pass

