#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Title: 配置文件

import ConfigParser
from ..decoratorUtil import singleton
import os

@singleton
class ConfigObj(object):

    config_obj = None
    def __init__(self):
        if self.config_obj is None:
            self.config_obj = ConfigParser.ConfigParser()
            with open('config.ini') as fp:
                self.config_obj.readfp(fp)
        pass


    def flushConfig(self):
        with open('config.ini', 'w') as fp:
            self.config_obj.write(fp)
            pass
        pass


# 获取系统配置数据
def getNodeConfig():
    configInstance = ConfigObj()

    config_dict = {
        "unique_id": configInstance.config_obj.get("system_conf", "unique_id"),
        "gps": configInstance.config_obj.get("system_conf", "gps"),
        "location": configInstance.config_obj.get("system_conf", "location"),
        "full_name": configInstance.config_obj.get("system_conf", "full_name"),
        "email_account": configInstance.config_obj.get("mail_conf", "mail_account"),
        "email_host": configInstance.config_obj.get("mail_conf", "mail_host"),
        "email_port": configInstance.config_obj.get("mail_conf", "mail_port"),
        "email_sender": configInstance.config_obj.get("mail_conf", "mail_sender"),
        "email_pwd": configInstance.config_obj.get("mail_conf", "mail_pwd"),
        "remote_address": configInstance.config_obj.get("internet_conf", "remote_address")
    }


    return config_dict
    pass

def updateNodeConfig(dict=None):

    pass



if __name__ == '__main__':
    ss = ConfigObj()
    ss2 = ConfigObj()
    ss3 = ConfigObj()
    ins1 = ss.config_obj
    ins2 = ss2.config_obj
    ins3 = ss3.config_obj
    print id(ins1)
    print id(ins2)
    print id(ins3)