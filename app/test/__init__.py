#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/13
# Title:
# Tip:
from flask import Blueprint
test = Blueprint('test', __name__)

from . import routes