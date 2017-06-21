#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/21
# Title:
# Tip:

from app.models import Sensor



def updateSensorByIdAndData(id=None, update_data=None):
    update_data = {
        Sensor.sensor_no: update_data["sensor_no"],
        Sensor.max_limit: update_data["max_limit"],
        Sensor.min_limit: update_data["min_limit"],
        Sensor.job_time: int(update_data["job_time"])
    }
    return Sensor.update(update_data).where(Sensor.id == id).execute()