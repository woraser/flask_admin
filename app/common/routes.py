#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Tip:通用模块
from flask import jsonify, request, current_app, url_for, session, redirect
from . import common
from dbFactory import getTablePageByCls
from ..commonUtil import buildDataTableResponse,getModelClsByName,buildSucc
from ..quartzJob import remoteJob
import json

@common.before_request
def before_request():
    if str(request.url_rule) != '/auth/login' and session.get('is_login') is None:
        return redirect(url_for('auth.login'))

# 根据tableName和分页参数获取分页数据 暂不支持查询和排序
# condition [{"key":"","op":"=","val":""}]
@common.route('/dataTable/<string:table_name>', methods=['POST'])
def getTablePage(table_name):
    post_data = request.json
    table_cls = getModelClsByName(table_name)
    res = getTablePageByCls(table_cls, post_data['offset'], post_data['pageSize'], post_data["condition"])
    response = buildDataTableResponse(post_data['draw'], res['data'], res['count'], res['count'])
    return json.dumps(response)

# 同步数据库中的基本数据
@common.route('/syncDbData')
def syncDbData():
    remoteJob.post_db_data()
    return buildSucc("success")