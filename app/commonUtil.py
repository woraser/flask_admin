#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib, json
from decoratorUtil import catchDbException
from collections import Iterable

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


def buildSucc(data):
    res = {
        "status": 1,
        "data": data
    }
    return json.dumps(res)
    pass

def buildErr(msg):
    res = {
        "status": 0,
        "data": msg
    }
    return json.dumps(res)
    pass

def buildNone():
    res = {
        "status": 2,
        "data": None
    }
    return json.dumps(res)
    pass

