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

# 传感器数据表
class Sensor(BaseModel):
    id = IntegerField(primary_key=True)
    sensor_no = CharField(verbose_name='传感器序列号', max_length=200)
    sensor_name = CharField(verbose_name='传感器名称', max_length=200)
    job_name = CharField(verbose_name='定时采集任务名称', max_length=200)
    job_time = IntegerField(verbose_name='定时任务周期', default=60)
    rel_equ = CharField(verbose_name='关联设备名称', max_length=200)
    max_limit = CharField(verbose_name='上限值', max_length=200)
    min_limit = CharField(verbose_name='下限值', max_length=200)
    type = CharField(verbose_name='类型名称', max_length=200)
    interface = CharField(verbose_name='接口名称', max_length=200)
    is_used = BooleanField(verbose_name='是否启用', default=True)


# 传感器数据采集表
class SensorData(BaseModel):
    id = IntegerField(primary_key=True)
    sensor_no = CharField(verbose_name='传感器序列号', max_length=20)
    val = CharField(verbose_name='采集值', max_length=20)
    created_time = IntegerField(verbose_name='创建时间')
    is_post = BooleanField(verbose_name='是否已推送', default=False)

# 收件人邮箱
class EngineerEmail(BaseModel):
    id = IntegerField(primary_key=True)
    account = CharField(verbose_name='收件邮箱', max_length=200)
    user_name = CharField(verbose_name='收件人名称', max_length=100)
    is_used = BooleanField(verbose_name='是否启用', default=True)
    created_time = DateField(verbose_name='创建时间')

# 系统运行监控数据
class SystemInfo(BaseModel):
    id = IntegerField(primary_key=True)
    cpu_usage = FloatField(verbose_name='CPU使用率')
    mem_usage = FloatField(verbose_name='内存使用率')
    collect_time = DateField(verbose_name='采集时间')