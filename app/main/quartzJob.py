#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apscheduler.schedulers.background import BackgroundScheduler
import commons
# http://quanjie.leanote.com/post/Python%E4%BB%BB%E5%8A%A1%E8%B0%83%E5%BA%A6%E6%A8%A1%E5%9D%97-%E2%80%93-APScheduler-2
# get system info by psutil
__author__ = 'chen hui'

class Quartz(object):

    # sched = BackgroundScheduler()

    def __init__(self):
        pass

    def my_job(self):
        print 'hello world'
        pass

    def addJobDynamic(self,conf_dict = {}):
        sched = BackgroundScheduler()
        job_dict = conf_dict.JOB_QUARTZ
        for k, v in job_dict.items():
            if getattr(Quartz(), k) != None:
               sched.add_job(getattr(Quartz(), k), 'interval', seconds=int(v))
        return sched


# sched = BackgroundScheduler()
# sched.add_job(getattr(Quartz(), 'my_job'), 'interval', seconds=5)
#     # def addJobForSched(self, dict={}):
#     #     for k, v in dict:
#     #
#     #         pass
#     #
#     # def initSched(self, config):
#     #     pass


