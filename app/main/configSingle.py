#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton



@singleton
class ConfigObj(object):

    config_obj = None
    def __init__(self):
        if self.config_obj is None:
            self.config_obj = ConfigParser.ConfigParser()
            with open('config.ini') as fp:
                self.config_obj.readfp(fp)
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