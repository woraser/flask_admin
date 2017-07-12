#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apscheduler.schedulers.background import BackgroundScheduler
from app.main import configSingle
from systemJob import recordSystemInfo
from sensorJob import SensorQuartz
from remoteJob import postSensorData
from quartzJobService import getActivitySensor
import logging, os

logging.basicConfig()
# http://quanjie.leanote.com/post/Python%E4%BB%BB%E5%8A%A1%E8%B0%83%E5%BA%A6%E6%A8%A1%E5%9D%97-%E2%80%93-APScheduler-2
__author__ = 'chen hui'

class Quartz(object):
    sched = None
    __instance = None

    def __init__(self):
        # unique
        if self.sched is None:
            self.sched = BackgroundScheduler(gconfig={'timezone': 'Asia/Shanghai'}, prefix=None)
        pass

    def __new__(cls, *args, **kwargs):
        if Quartz.__instance is None:
            Quartz.__instance = object.__new__(cls, *args, **kwargs)
        return Quartz.__instance

    def getAllJobs(self):
        self.sched.print_jobs()
        return self.sched.get_jobs()

    def removeJob(self, name):
        self.sched.remove_job(name)
        pass

    def startJob(self):
        self.sched.start()


    def addJobDynamic(self):
        configInstance = configSingle.ConfigObj()
        base_dir = configInstance.config_obj.get("project_conf", "base_dir")
        config_path = os.path.join(base_dir, "config.ini")
        # 初始化任务器 设置默认时区
        # sched = BackgroundScheduler(gconfig={'timezone': 'Asia/Shanghai'}, prefix=None)
        config = configInstance.config_obj
        # 添加系统任务
        system_time = config.get("system_conf", "system_job_time")
        system_job_time = system_time if isinstance(system_time, int) else 1
        self.sched.add_job(recordSystemInfo, 'interval', seconds=int(system_job_time), id=recordSystemInfo.func_name)
        # 添加服务器同步任务
        self.sched.add_job(postSensorData, 'interval', seconds=int(60),id=postSensorData.func_name)
        # 添加传感器时间
        # dht11 传感器
        sensorQuartz = SensorQuartz()
        activity_sensor = getActivitySensor()
        if activity_sensor is not None:
            for sensor in activity_sensor:
                self.sched.add_job(getattr(sensorQuartz, sensor.job_name), 'interval', seconds=int(sensor.job_time),id=str(sensor.sensor_no))
                pass
            pass
        # sched.add_job(getattr(sensorQuartz, "runDht11Collect"), 'interval', seconds=int(10))

        # sections = config.sections()
        # for i in sections:
        #     if str(i).startswith('quartzJob'):
        #         job_name = config.get(i, 'job_name')
        #         job_time = config.get(i, 'job_time')
        #         if job_name is not None and job_time is not None and getattr(Quartz(), job_name) != None:
        #             sched.add_job(getattr(Quartz(), job_name), 'interval', seconds=int(job_time))
        #         pass
        #     pass
        return self.sched

    def updateJobTimeForSensor(self, job_name=None, job_time=None, sensor_no=None):
        sensorQuartz = SensorQuartz()
        self.sched.pause()
        # remove old
        self.removeJob(str(sensor_no))
        # add new
        self.sched.add_job(getattr(sensorQuartz, job_name), 'interval', seconds=int(job_time), id=str(sensor_no))
        # continue job
        self.sched.resume()
        pass


if __name__ == '__main__':
    pass
    # q = Quartz()
    # q.addJobDynamic().start()

