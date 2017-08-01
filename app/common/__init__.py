#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/28
# Title:通用路由 数据库工厂类
# Tip:
from flask import Blueprint
common = Blueprint('common', __name__)

from . import routes