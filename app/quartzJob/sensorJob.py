#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/13
# Title:传感器定时采集
# Tip:运行指令 jslinux dht11.js
from app.common.dbFactory import insertSensorCollect
from app.models import SensorData
import random
import os


class SensorQuartz(object):
    # 运行dht11传感器脚本 温湿度传感器
    @staticmethod
    def runDht11Collect():
        # # 温度
        # with os.popen("cat /sys/devices/dht11/iio:device0/in_temp_input") as ps:
        #     res = ps.read().strip()
        #     if type(res) == int:
        #         val_temp = round(res/1000, 2)
        #         insertSensorCollect(SensorData, "dht11_1", "温度", str(val_temp) + "°c")
        #         pass
        #
        #
        # # 湿度
        # with os.popen("cat /sys/devices/dht11/iio:device0/in_humidityrelative_input") as ps:
        #     res = ps.read().strip()
        #     if type(res) == int:
        #         val_humi = round(res/1000, 2)
        #         insertSensorCollect(SensorData, "dht11_1", "湿度", str(val_humi) + "%")
        #         pass
        insertSensorCollect(SensorData, "dht11_1", "湿度", str(random.randint(0, 100)) + "%")
        insertSensorCollect(SensorData, "dht11_1", "温度", str(random.randint(0, 100)) + "°c")
        # print "runDht11Collect"
        pass

    pass

    # 运行其他传感器的
    @staticmethod
    def runDht2Collect():
        # # 温度
        # with os.popen("cat /sys/devices/dht11/iio:device0/in_temp_input") as ps:
        #     res = ps.read().strip()
        #     if type(res) == int:
        #         val_temp = round(res/1000, 2)
        #         insertSensorCollect(SensorData, "dht11_1", "温度", str(val_temp) + "°c")
        #         pass
        #
        #
        # # 湿度
        # with os.popen("cat /sys/devices/dht11/iio:device0/in_humidityrelative_input") as ps:
        #     res = ps.read().strip()
        #     if type(res) == int:
        #         val_humi = round(res/1000, 2)
        #         insertSensorCollect(SensorData, "dht11_1", "湿度", str(val_humi) + "%")
        #         pass
        insertSensorCollect(SensorData, "dht11_1", "湿度", str(random.randint(0, 100)) + "%")
        insertSensorCollect(SensorData, "dht11_1", "温度", str(random.randint(0, 100)) + "°c")
        print "sensor data Dht2 ok"
        pass

    pass