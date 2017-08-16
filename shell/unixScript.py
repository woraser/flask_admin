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
# 使用supervisorctl 来管理进程
def restartProject():
    isRunning= False
    configInstance = configSingle.ConfigObj()
    base_dir = configInstance.config_obj.get("project_conf", "base_dir")
    # 先判断是否存在使用supervisorctl进程 若存在 则重启 反之则新建
    checkRunning_shell = os.popen("ps | grep supervisord")
    for line in checkRunning_shell:
        if "{supervisord} /usr/bin/python2.7" in line:
            isRunning = True
            break
        pass
    pass
    if isRunning is True:
        restart_shell = "supervisorctl -c supervisor.conf reload"
        shell_script = "cd {path} && cd ./.. &&{restart}".format(path=base_dir, restart=restart_shell)
        os.popen(shell_script)
        pass
    else:
        start_shell = "supervisord -c supervisor.conf"
        os.popen("cd {path} && cd ./.. && {start}".format(path=base_dir, start=start_shell))
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

