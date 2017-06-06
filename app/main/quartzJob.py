#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apscheduler.schedulers.background import BackgroundScheduler
import commons, ConfigParser, json
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

    def addJobDynamic(self):
        sched_config = {
             'timezone': 'Asia/Shanghai'
        }
        sched = BackgroundScheduler(gconfig=sched_config, prefix=None)
        # sched._configure(sched_config)
        config = ConfigParser.ConfigParser()
        config.readfp(open('config.ini'))
        sections = config.sections()
        for i in sections:
            if str(i).startswith('sensor'):
                job_name = config.get(i, 'job_name')
                job_time = config.get(i, 'job_time')
                if job_name is not None and job_time is not None and getattr(Quartz(), job_name) != None:
                    sched.add_job(getattr(Quartz(), job_name), 'interval', seconds=int(job_time))
                pass;
            pass
        return sched

if __name__ == '__main__':
    q = Quartz()
    q.addJobDynamic().start()


