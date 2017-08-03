#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/8/3
# Title:重启当前项目的脚本
# Tip:
import os

cmd_res = os.popen("ps | grep manage.py")
for line in cmd_lines:
    if "runserver" in line:
        os.popen("kill -9 {pid}".format(pid=line.split()[0]))
    pass
else:
    os.popen("cd /mnt/python-www/flask_admin/ && python manage.py runserver --host 0.0.0.0")
    pass





