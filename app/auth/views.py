#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/28
# Title:权限控制器
# Tip:

from flask import render_template, redirect, request, url_for, flash, session
from app.models import User
from . import auth
import json

@auth.before_request
def before_request():
    if str(request.url_rule) != '/auth/login' and session.get('is_login') is None:
        return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    reponse = {}
    reponse["status"] = 0
    if request.method == 'POST':
        post_data = request.values
        login_account = str(post_data['login_account'])
        login_pwd = str(post_data['login_pwd'])
        user = User.getUserByAccountAndPwd(login_account, login_pwd)
        if user is not None:
            session.setdefault('is_login', True)
            # json在转换date类型的时候会报错
            user._data["created_time"] = None
            session.setdefault('user', json.dumps(user._data))
            reponse['status'] = 1
            reponse['data'] = '/index'
            return json.dumps(reponse)
    return render_template('auth/login.html')


@auth.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('login'))
