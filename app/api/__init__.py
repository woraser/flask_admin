#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/28
# Title:对外接口
# Tip:

from flask import Blueprint
api = Blueprint('api', __name__)
from . import view