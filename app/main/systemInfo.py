#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tip:http://homeway.me/2015/04/29/openwrt-develop-base-util/
# Title:系统级别参数
from app.main import configSingle
import os

# get system info by psutil
__author__ = 'chen hui'

# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:4])

# 获取内存使用率
def getRamUsage():
    RAM_stats = getRAMinfo()
    RAM_total = round(int(RAM_stats[0]) / 1000, 1)
    RAM_used = round(int(RAM_stats[1]) / 1000, 1)
    # RAM_free = round(int(RAM_stats[2]) / 1000, 1)  # Disk information
    RAM_usage = round(float(RAM_used / RAM_total), 2)
    return RAM_usage


# Return % of CPU free
def getCpuFree():
    return(str(os.popen("top -n1 | awk '/CPU/ {print $8}'").readline().strip()))

# Return runTime of system
def getRunTime():
    with os.popen("cat /proc/uptime") as ps:
        res = ps.readline().strip().split(" ")
    return res[0]
    pass

# build dict of dashboard for index
# 组装首页面板数据
def getDashboard():

    configInstance = configSingle.ConfigObj()
    config_obj = configInstance.config_obj
    dashboard_dict = {
        "id": config_obj.get("system_conf", "unique_id"),
        "GPS": config_obj.get("system_conf", "cps"),
        "runtime": int(getRunTime()/60/60)
    }
    return dashboard_dict
    pass

