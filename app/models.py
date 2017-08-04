#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *
from app.main import configSingle
import time
from datetime import datetime

db = SqliteDatabase('./test3.db')

def initDb():
    db.create_tables([User, SensorData, SystemInfo, Sensor], safe=True)
    User.createdDefaultAccount()
    db.close()

class BaseModel(Model):
    class Meta:
        database = db

# 用户信息模型
class User(BaseModel):
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
            user = user_instance.get(User.account == account and User.pwd == pwd)
        except Exception as err:
            # err.message
            user = None
        return user

    # 添加默认账号
    @staticmethod
    def createdDefaultAccount():
        configInstance = configSingle.ConfigObj()
        default_account = configInstance.config_obj.get("super_user", "default_account")
        default_pwd = configInstance.config_obj.get("super_user", "default_pwd")
        user = User.getUserByAccountAndPwd(default_account, default_pwd)
        if user is not None:
            return
            pass
        row = {
            "account": default_account,
            "pwd": default_pwd,
            "pwd_hash": default_pwd,
            "created_time": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        }
        User.insert(row).execute()
        pass

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
    type = CharField(verbose_name='类型名称，传感器用途', max_length=200)
    interface = CharField(verbose_name='接口名称', max_length=200)
    accessPort = CharField(verbose_name='接入端口名称', max_length=200)
    is_used = BooleanField(verbose_name='是否启用', default=True)

# 传感器数据采集表
class SensorData(BaseModel):
    id = IntegerField(primary_key=True)
    sensor_no = CharField(verbose_name='传感器序列号', max_length=50)
    param_name = CharField(verbose_name='采集参数名称', max_length=50)
    val = CharField(verbose_name='采集值', max_length=50)
    created_time = IntegerField(verbose_name='创建时间,时间戳便于传输')
    is_post = BooleanField(verbose_name='是否已推送', default=False)

# 系统运行监控数据
class SystemInfo(BaseModel):
    id = IntegerField(primary_key=True)
    cpu_usage = FloatField(verbose_name='CPU使用率')
    ram_usage = FloatField(verbose_name='内存使用率')
    collect_time = CharField(verbose_name='采集时间', max_length=50)