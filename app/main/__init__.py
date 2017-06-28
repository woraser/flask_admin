#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/28
# Title:主路由器
# Tip:

from flask import Blueprint
main = Blueprint('main', __name__)

from . import errors, views