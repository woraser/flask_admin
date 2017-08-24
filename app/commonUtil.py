#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib, json
from decoratorUtil import catchDbException
from collections import Iterable
from datetime import datetime

# 将peewee查询对象转化为dict
def convertDbObjToDict(objs, cls):
    dict_array = []
    fields = getFieldsFromModelCls(cls)
    if not isinstance(objs, Iterable):
        dict_item = {}
        for i in fields:
            if getattr(objs, i) is not None:
                dict_item.setdefault(i, getattr(objs, i))
            pass
        return dict_item
    for obj in objs:
        dict_item = {}
        for i in fields:
            if getattr(obj, i) is not None:
                dict_item.setdefault(i, getattr(obj, i))
            pass
        dict_array.append(dict_item)
        pass
    return dict_array

# 从peewee model类中获得声明属性
def getFieldsFromModelCls(cls):
    declared_fields = []
    for k, v in dict(cls.__dict__).items():
        if hasattr(v, "field"):
            declared_fields.append(k)
        pass
    return declared_fields

# 拼装成dataTables返回结果
def buildDataTableResponse(draw, data, recordsTotal, recordsFiltered):
    response = {
        "data": data,
        "draw": draw,
        "recordsTotal": recordsTotal,
        "recordsFiltered": recordsFiltered,
    }
    return response
    pass

# 根据model类的名称获得cls
@catchDbException
def getModelClsByName(cls_name):
    mode = importlib.import_module('.models', 'app')
    cls = getattr(mode, cls_name)
    return cls

# 生成返回obj->成功
def buildSucc(data):
    res = {
        "status": 1,
        "data": data
    }
    return json.dumps(res)
    pass

# 生成返回obj->失败
def buildErr(msg):
    res = {
        "status": 0,
        "data": msg
    }
    return json.dumps(res)
    pass

# 生成返回obj->无返回结果
def buildNone():
    res = {
        "status": 2,
        "data": None
    }
    return json.dumps(res)
    pass

# 转换参数
def convertObj():
    pass


# 获取当前时间 str
def getNowStr():
    return str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 获取当前时间 date
def getNowDate():
    return datetime.now()

# 获取当前时间 str 自定义时间格式
def getNowFormat(fm="%Y-%m-%d %H:%M:%S"):
    return str(datetime.now().strftime(fm).format(fm=fm))

def getScore():
    pass

