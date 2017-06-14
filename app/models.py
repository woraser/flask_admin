#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_login import UserMixin
from peewee import *

db = SqliteDatabase('./test3.db')

def initDb():
    db.create_tables([User, SensorData], safe=True)
    db.close()

class BaseModel(Model):
    class Meta:
        database = db

# 用户信息
class User(UserMixin, BaseModel):
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


# 传感器数据采集表
class SensorData(BaseModel):
    id = IntegerField(primary_key=True)
    no = CharField(max_length=20)
    val = CharField(max_length=20)
    created_time = IntegerField()
    is_post = BooleanField(verbose_name='是否已推送', default=False)


class EngineerEmail(BaseModel):
    id = IntegerField(primary_key=True)
    account = CharField(max_length=200)
    user_name = CharField(max_length=100)
    is_used = BooleanField(verbose_name='是否启用', default=True)

class systemInfo(BaseModel):
    id = IntegerField(primary_key=True)
    cpu_usage = CharField(max_length=20)
    mem_usage = CharField(max_length=20)
