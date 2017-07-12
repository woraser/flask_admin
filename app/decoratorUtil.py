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


# 单例模式
# 可以使用__new__魔法变量来代替
def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


