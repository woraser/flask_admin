#!/usr/bin/env python
# -*- coding: utf-8 -*-



#捕获异常，常用于peewee查询为空时返回异常
def catchDbException(func):
    def warpper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception, e:
            # print e.message
            pass
        pass
    return warpper

