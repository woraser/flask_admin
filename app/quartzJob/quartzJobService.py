#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/23
# Title:
# Tip:
from app.decoratorUtil import catchDbException
from app.models import Sensor
from peewee import Expression

# 获得所有活动的传感器数据
@catchDbException
def getActivitySensor():
    expression = Expression(Sensor.is_used, "=", True)
    # expression1 = Expression(Sensor.id, "=", "1")
    # condition = condition and expression1
    return Sensor.select().where(expression)
    pass