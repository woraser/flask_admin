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