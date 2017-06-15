#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/14
# Title:获取系统数据 包括cpu使用率和内存使用率
# Tip:
from ..main import systemInfo
from datetime import datetime
from ..common.dbFactory import insertByCls


# 获取系统运行参数 插入数据库
def getSystemInfo():
    cpu_free = systemInfo.getCpuFree()
    ram_usage = systemInfo.getRamUsage()
    if cpu_free:
        cpu_free = cpu_free.split("%", "")
    row = {
        cpu_usage: 100-int(cpu_free),
        ram_usage: ram_usage,
        collect_time: datetime.now()
    }
    return insertByCls("SystemInfo", row)
    pass