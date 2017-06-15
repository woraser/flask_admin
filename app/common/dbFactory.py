#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..decoratorUtil import catchDbException
from ..models import db, User
from ..commonUtil import convertDbObjToDict, getModelClsByName
import time


# 直接执行sql语句
def executeSql(sql, params=None):
    return db.execute_sql(sql, params)

#根据类名，id删除数据
def deleteByClsAndId(cla_name, identity=None):
    cls = getModelClsByName(cla_name)
    return User.delete().where(cls.id == identity).execute()

#根据id插入数据
def insertByCls(cla_name, data=None):
    cls = getModelClsByName(cla_name)
    return cls.insert(data).execute()

# 根据model类名 获得分页数据
def getTablePageByCls(cla_name, offset=0, limit=10):
    cls = getModelClsByName(cla_name)
    data_array = queryTableByCls(cls, offset, limit)
    count = queryTotalByCls(cls)
    res = {}
    res.setdefault("count", count)
    content = []
    if data_array is not None:
        content = (convertDbObjToDict(data_array, cls))
    res.setdefault("data", content)
    return res

# 动态插入传感器数据
def insertSensorCollect(cls_name, sensor_name, val):
    cls = getModelClsByName(cls_name)
    row = buildSensorRow(sensor_name, val)
    return cls.insert(row).execute()

# 批量插入数据 事务支持@db.atomic()
@db.atomic()
def batchInsert(cls_name, insert_datas=None):
    cls = getModelClsByName(cls_name)
    return cls.insert_many(insert_datas).execute()

# 根据类名，分页参数获取db数据
@catchDbException
def queryTableByCls(cls, offset=0, limit=10):
    return cls.select().offset(offset).limit(limit)

# 根据类名获取db数据
@catchDbException
def queryTotalByCls(cls):
    return cls.select().count()

# 构建传感器数据row
def buildSensorRow(sensor_name, val):
    return {
        "created_time": time.time(),
        "sensor_name": sensor_name,
        "val": val
    }


