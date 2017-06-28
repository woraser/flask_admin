#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/28
# Title:
# Tip:
from app.models import Sensor
from peewee import Expression
import commons
from app.common.dbFactory import updateModelByWhere


def updateSensorByRemote(post_data):
    exp_list = [Expression(getattr(Sensor, k), "=", v) for k, v in post_data]


    pass