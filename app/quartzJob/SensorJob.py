#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/13
# Title:传感器定时采集
# Tip:运行指令 jslinux dht11.js

import os


# 运行dht11传感器脚本 温湿度传感器
def runDht11Collect():
    os.popen("jslinux dht11.js")
    pass


if __name__ == '__main__':
    runDht11Collect()


