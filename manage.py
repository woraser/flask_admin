#!/usr/bin/env python'
# -*- coding: utf-8 -*-
import os

# from app.models import User
COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app
from flask_script import Manager

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app()
# 添加一些特殊路由 进行linux交互
from shell import shell as shell_blueprint
app.register_blueprint(shell_blueprint, url_prefix='/shell')

manager = Manager(app)

# start the app when execute command:python manage.py
if __name__ == '__main__':

    # linux执行方法：python manage.py runserver --host 0.0.0.0
    manager.run()
    # 避免debug模式下二次初始化数据 但是文件更新之后不会在刷新文件
    # app.run(port=5000, debug=True, use_reloader=False)
#     等同于 判断WERKZEUG_RUN_MAIN 变量 再决定是否运行app
#     if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
#         pass
#     app.run(port=5000, debug=True)

