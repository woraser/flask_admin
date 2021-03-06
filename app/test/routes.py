#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/13
# Title:
# Tip:
from flask import jsonify
from . import test
from ..models import User
from ..common.dbFactory import batchInsert
from app.main.systemInfo import getRunTime
from ..quartzJob import systemJob,remoteJob
import time
from app.mqtt.mqttClient import MqttClientSingle
from app.quartzJob.schedulerJob import Quartz


@test.route("/testpeewee")
def testpeewee():
    # format_time = time.time()
    # insert_datas = [{"account": "123", "pwd": "123", "created_time": format_time},
    #                 {"account": "1234", "pwd": "1234", "created_time": format_time},
    #                 {"account": "12345", "pwd": "12345", "created_time": format_time}]
    # res = batchInsert("User", insert_datas)
    # return jsonify({"status":1})
    pass


@test.route("/testGetSystemInfo")
def testGetSystemInfo():
    # system_job.addSystemInfo()
    return jsonify({"result":getRunTime()})
    pass

@test.route("/testPostSensor")
def testPostSensor():
    # system_job.addSystemInfo()
    remoteJob.postSensorData()
    return jsonify({"result":getRunTime()})
    pass

@test.route("/testMqtt")
def testMqtt():
    mqttCilent = MqttClientSingle()
    mqttCilent2 = MqttClientSingle()
    if mqttCilent.__eq__(mqttCilent2):
        print "single class"
        pass
    print id(mqttCilent)
    print id(mqttCilent2)
    mqttCilent.mattClient.publish("helloTopic", "message")
    return jsonify({"result": getRunTime()})
    pass

def testSay():
    print "added quartz job"

@test.route("/testAddJob")
def testAddJob():
    quartz = Quartz()
    quartz.getAllJobs()
    quartz.sched.pause()
    quartz.sched.add_job(testSay, 'interval', seconds=int(2), id="testSay")
    quartz.sched.resume()
    return jsonify({"result": getRunTime()})
    pass

@test.route("/deleteJob")
def removeAddJob():
    quartz = Quartz()
    quartz.sched.pause()
    quartz.sched.remove_job("testSay")
    quartz.sched.resume()
    return jsonify({"result": getRunTime()})
    pass






