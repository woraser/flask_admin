#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/8/4
# Title:
# Tip:
from . import shell
from flask import request, redirect, session, url_for
import unixScript
import json

@shell.before_request
def before_request():
    pass


# 重启项目
@shell.route('/restartProject')
def restartProject():
    unixScript.restartProject()
    return json.dumps({"status": 1})

# 项目升级
@shell.route('/upgradeProject')
def upgradeProject():
    unixScript.upgradeProject()
    return json.dumps({"status": 1})

# 项目备份
@shell.route('/backUpApplication')
def backUpApplication():
    unixScript.zipCurrentApplication()
    return json.dumps({"status": 1})


# 接受上传文件
@shell.route('/receiveUpgradeApp')
def receiveUpgradeApp():
    unixScript.receiveUpgradeApp()
    return json.dumps({"status": 1})


