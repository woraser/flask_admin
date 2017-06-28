#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/28
# Title:权限控制
# Tip:
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views