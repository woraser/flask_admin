#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler

# get system info by psutil
__author__ = 'chen hui'


def my_job():
    print 'hello world'
    pass

sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=5)
sched.start()
