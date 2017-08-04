#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/8/4
# Title:与linux进行交互 执行项目管理
# Tip:
from flask import Blueprint

shell = Blueprint('shell', __name__)

from . import views