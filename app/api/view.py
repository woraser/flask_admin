#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/28
# Title:
# Tip:
from flask import render_template, redirect, request, url_for, flash, session
from app.commonUtil import buildSucc,buildNone,buildErr
from peewee import Expression
from app.common.dbFactory import updateModelByWhere
from ..models import User
import json
from app.models import Sensor
from .apiService import updateModelByWhere



# 调用该接口 更新传感器数据
# POST:{}
#
def syncSensorFromRemote():
    post_data = request.json
    validate_data = __validateSensorPost(post_data)
    if not validate_data:
        return buildErr("参数错误，请仔细检查")
    res = updateModelByWhere(post_data)
    return buildSucc(res)
    pass
    pass

def __validateSensorPost(post_data=None):
    dict = {}
    hash_keys = dict.keys()
    hash_values = dict.values()
    if not hash_keys.__contains__("sensor_no"):
        return False
        pass

    return True

    pass