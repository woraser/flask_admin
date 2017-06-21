#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tip:http://homeway.me/2015/04/29/openwrt-develop-base-util/
# Title:系统级别参数
from __future__ import division
from app.main import configSingle
from app.common.dbFactory import getTablePageByCls
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

# 获取硬盘总量
def getHardDiskTotal():
    with os.popen("df | awk '{print $2}'") as ps:
        res = ps.read().strip().split("\n")
    int_list = [(int(i)) for i in res[1:]]
    return sum(int_list)
    pass

# 获取硬盘使用量
def getHardDiskUsed():
    with os.popen("df | awk '{print $3}'") as ps:
        res = ps.read().strip().split("\n")
    int_list = [(int(i)) for i in res[1:]]
    return sum(int_list)
    pass

# 获取硬盘的使用率
def getHardDiskUseage():
    df_total = getHardDiskTotal()
    df_used = getHardDiskUsed()
    return round(df_used/df_total, 4)*100


# build dict of dashboard for index
# 组装首页面板数据
def getDashboard():

    configInstance = configSingle.ConfigObj()
    config_obj = configInstance.config_obj
    dashboard_dict = {
        "id": config_obj.get("system_conf", "unique_id"),
        "GPS": config_obj.get("system_conf", "gps"),
        # "runtime": int(int(getRunTime())/60/60)
        "runtime": int(200400 / 60 / 60)
    }
    return dashboard_dict
    pass

def getSystemHistory(limit=500):
    orderBy = ('id', 'desc')
    cursor = getTablePageByCls("SystemInfo", limit=limit, order=orderBy)
    return cursor
    pass

