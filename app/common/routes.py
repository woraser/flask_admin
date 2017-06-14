#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import jsonify, request, current_app, url_for
from . import common
from dbFactory import getTablePageByCls
from ..commonUtil import buildDataTableResponse
from ..quartzJob import remoteSync_job
import json


# 根据tableName和分页参数获取分页数据 暂不支持查询和排序
@common.route('/dataTable/<string:table_name>', methods=['POST'])
def getTablePage(table_name):
    post_data = request.json
    res = getTablePageByCls(table_name, post_data['offset'], post_data['pageSize'])
    response = buildDataTableResponse(post_data['draw'], res['data'], res['count'], res['count'])
    return json.dumps(response)
    pass

# 同步数据库中的基本数据
@common.route('/syncDbData')
def syncDbData():
    remoteSync_job.post_db_data()
    return "success"