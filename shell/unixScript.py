#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/8/3
# Title:unix运行脚本 通过调用方法可直接在unix环境中运行对应脚本
# Tip:若已存在进程 则执行重启 若不存在 则执行启动
import os
import json
from app.main import configSingle


# 项目升级
def upgradeProject(dir=None):
    configInstance = configSingle.ConfigObj()
    base_dir = configInstance.config_obj.get("project_conf", "base_dir")
    # 备份文件
    zipCurrentApplication()
    # 解压文件

    # 文件替换
    replaceApp()
    # 重启项目
    restartProject()
    return None
    pass


# 重启项目
def restartProject():
    cmd_res = os.popen("ps | grep manage.py")
    for line in cmd_res:
        if "runserver" in line:
            os.popen("kill -9 {pid}".format(pid=line.split()[0]))
        pass
    else:
        os.popen("cd /mnt/python-www/flask_admin/ && python manage.py runserver --host 0.0.0.0")
        pass
    pass

# 将当前app应用压缩打包到指定目录
def zipCurrentApplication():
    configInstance = configSingle.ConfigObj()
    base_dir = configInstance.config_obj.get("project_conf", "base_dir")
    path = base_dir+"/historyApp/app_$(date +%Y%m%d%H%M%S).tar.gz"
    copyDir = base_dir+"/app"
    os.popen("tar -zcvf {path} {copyDir}".format(path=path, copyDir=copyDir))
    pass

# 解压新app 覆盖当前app
def tarApplication():
    configInstance = configSingle.ConfigObj()
    base_dir = configInstance.config_obj.get("project_conf", "base_dir")
    os.popen("tar -zxf ")

    pass

# app目录完全替换
def replaceApp(cfile=None):
    configInstance = configSingle.ConfigObj()
    base_dir = configInstance.config_obj.get("project_conf", "base_dir")
    appPath = base_dir + "/app"
    os.popen("cp -frap {cfile} {dfile}".format(cfile=cfile, dfile=appPath))
    pass

# 接收上传的文件
def receiveUpgradeApp():
    configInstance = configSingle.ConfigObj()
    base_dir = configInstance.config_obj.get("project_conf", "base_dir")
    savePath = base_dir+"/upgradeApp"
    with open("", "w") as newFile:
        newFile.write()
        newFile.flush()
        pass
    pass

if __name__ == '__main__':
    pass

