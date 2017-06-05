#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from peewee import *

db = SqliteDatabase('./test3.db')

def initDb():
    db.create_tables([User], safe=True)
    db.close()

class BaseModel(Model):
    class Meta:
        database = db

# 用户信息
class User(UserMixin,BaseModel):
    id = IntegerField(primary_key=True)
    account = CharField(max_length=20)
    pwd = CharField(max_length=200)
    pwd_hash = CharField(max_length=200)
    created_time = DateField()

    @staticmethod
    def getUserByAccountAndPwd(account, pwd):
        user_instance = User()
        # pwd_hash = generate_password_hash(pwd)
        try:
            user = user_instance.get(User.account == account and  User.pwd == pwd)
        except Exception:
            user = None
        return user

    def updatePwd(self, account, new_pwd):
        user_instance = User()
        # new_pwd_hash = generate_password_hash(new_pwd)
        User.update(pwd=new_pwd).where(User.id == account['id']).execute()
        pass


