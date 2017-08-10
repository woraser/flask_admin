#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/28
# Title:API对外接口服务类
# Tip:
from peewee import Expression
from app.models import Sensor
from app.common.dbFactory import updateModelByWhere

# 远程修改传感器参数 主要修改传感器上下限 是否启用
def updateSensorByRemote(post_data):
    exp_list = [Expression(getattr(Sensor, k), "=", v) for k, v in post_data if k != "id"]
    condition = Expression(Sensor.id, "=", post_data["id"])
    res = updateModelByWhere(Sensor, exp_list, condition)
    return res

    pass