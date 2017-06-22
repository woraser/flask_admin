#!/usr/bin/env python'
# -*- coding: utf-8 -*-
import os
from flask import current_app
from app.main.configSingle import ConfigObj
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

from app import create_app, db
# from app.models import User, Follow, Role, Permission, Post, Comment
from flask_script import Manager, Shell
# from flask_migrate import Migrate, MigrateCommand

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app()
manager = Manager(app)


# 定义全局变量 项目所在绝对路径
# migrate = Migrate(app, db)

# def make_shell_context():
#     print 123
#     return dict(app=app, db=db, User=User)
#
# manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)


# start the app when execute command:python manage.py
if __name__ == '__main__':
    # manager.run()
      app.run(debug=True)

