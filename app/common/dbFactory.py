#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ..decoratorUtil import catchDbException
from ..models import db, User
from peewee import Expression
from ..commonUtil import convertDbObjToDict, getModelClsByName
import time


# 直接执行sql语句
def executeSql(sql, params=None):
    return db.execute_sql(sql, params)

#根据类名，id删除数据
def deleteByClsAndId(cla_name, identity=None):
    cls = getModelClsByName(cla_name)
    return User.delete().where(cls.id == identity).execute()

#根据类名插入数据
def insertByCls(cla_name, data=None):
    cls = getModelClsByName(cla_name)
    return cls.insert(data).execute()

# 根据类名和主键获得数据详情
def findOneByClsAndId(cls, id):
    # cls = getModelClsByName(Cla)
    record = findOneByIdFromDb(cls, id)
    if record is not None:
        return convertDbObjToDict(record, cls)
        pass
    return record

# 根据条件修改类
# update_dict = {cls.id:1,..}
# condition={Expression(Sensor.id, "=", id),..}
def updateModelByWhere(cls, update_dict=None, condition=None):
    return cls.update(update_dict).where(condition).execute()
    pass

# 根据model类 获得分页数据
def getTablePageByCls(cls, offset=0, limit=10,condition=None,order=None):
    # cls = getModelClsByName(cla_name)
    data_array = queryTableByCls(cls, offset, limit, condition, order)
    count = queryTotalByCls(cls, condition)
    res = {}
    res.setdefault("count", count)
    content = []
    if data_array is not None:
        content = (convertDbObjToDict(data_array, cls))
    res.setdefault("data", content)
    return res

# 动态插入传感器数据
def insertSensorCollect(cls, sensor_no, param_name, val):
    row = buildSensorRow(sensor_no, param_name,  val)
    return cls.insert(row).execute()

# 批量插入数据 事务支持@db.atomic()
@db.atomic()
def batchInsert(cls_name, insert_datas=None):
    cls = getModelClsByName(cls_name)
    return cls.insert_many(insert_datas).execute()

# 根据类名，分页参数获取db数据
@catchDbException
def queryTableByCls(cls, offset=0, limit=10, condition=None, order=None):
    expresses = None
    if condition:
        for condi in condition:
            if expresses is None:
                expresses = Expression(getattr(cls,condi["key"]), condi["op"], condi["val"])
                pass
            else:
                expresses = expresses and Expression(getattr(cls,condi["key"]), condi["op"], condi["val"])
                pass
            pass
    return cls.select().where(expresses).order_by(order).offset(offset).limit(limit)

# 根据类名获取db数据总量 query count
@catchDbException
def queryTotalByCls(cls, condition=None):
    expresses = None
    if condition:
        for condi in condition:
            if expresses is None:
                expresses = Expression(getattr(cls,condi["key"]), condi["op"], condi["val"])
                pass
            else:
                expresses = expresses and Expression(getattr(cls,condi["key"]), condi["op"], condi["val"])
                pass
            pass
    return cls.select().where(expresses).count()

# 根据类名和id获取db数据
@catchDbException
def findOneByIdFromDb(cls, unique_id):
    return cls.get(cls.id == unique_id)

# 构建传感器数据row
def buildSensorRow(sensor_no, param_name, val):
    return {
        "created_time": time.time(),
        "sensor_no": sensor_no,
        "param_name": param_name,
        "val": val
    }


