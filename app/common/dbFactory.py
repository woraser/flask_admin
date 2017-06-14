#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..decoratorUtil import catchDbException
from ..models import db
from ..commonUtil import convertObjToDict, getModelClsByName
import time



# 根据model类名 获得分页数据
def getTablePageByCls(cla_name, offset=0, limit=10):
    cls = getModelClsByName(cla_name)
    data_array = queryTableByCls(cls, offset, limit)
    count = queryTotalTableByCls(cls)
    res = {}
    res.setdefault("count", count)
    content = []
    if data_array is not None:
        content = (convertObjToDict(data_array, cls))
    res.setdefault("data", content)
    return res

# 动态插入传感器数据
def insertSensorCollect(cls_name, sensor_name, val):
    cls = getModelClsByName(cls_name)
    row = buildSensorRow(sensor_name, val)
    return cls.insert(row).execute()

# 批量插入数据 事务支持@db.atomic()
@db.atomic()
def batchInsert(cls_name, insert_datas=[]):
    cls = getModelClsByName(cls_name)
    return cls.insert_many(insert_datas).execute()


@catchDbException
def queryTableByCls(cls, offset=0, limit=10):
    return cls.select().offset(offset).limit(limit)

@catchDbException
def queryTotalTableByCls(cls):
    return cls.select().count()


def buildSensorRow(sensor_name, val):
    return {
        "created_time": time.time(),
        "sensor_name": sensor_name,
        "val": val
    }


