#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
from decoratorUtil import catchDbException

# 将peewee查询对象转化为dict
def convertDbObjToDict(objs, cls):
    dict_array = []
    fields = getFieldsFromModelCls(cls)
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

@catchDbException
def getModelClsByName(cls_name):
    mode = importlib.import_module('.models', 'app')
    cls = getattr(mode, cls_name)
    return cls
