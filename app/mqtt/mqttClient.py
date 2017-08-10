#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/6/30
# Title:
# Tip: mqtt客户端 单例模式

from flask_mqtt import Mqtt
from app.main import configSingle


class MqttClientSingle(object):
    _mattClient = None
    __instance = None
    def __init__(self):
        if self._mattClient is None:
            # 初始化mqtt
            self._mattClient = initMqttClient()
    pass

    def __new__(cls, *args, **kwargs):
        if MqttClientSingle.__instance is None:
            MqttClientSingle.__instance = object.__new__(cls, *args, **kwargs)
        return MqttClientSingle.__instance

    @property
    def mattClient(self):
        return self._mattClient

# 初始化mqtt连接
def initMqttClient():
    mqtt = Mqtt()
    # 模拟app上下文实现
    app = App()
    configInstance = configSingle.ConfigObj()
    mqtt_host = configInstance.config_obj.get("mqtt_conf", "MQTT_BROKER_URL")
    mqtt_port = configInstance.config_obj.get("mqtt_conf", "MQTT_BROKER_PORT")
    app.config = {"init": "dict", 'MQTT_BROKER_URL': mqtt_host, 'MQTT_BROKER_PORT': int(mqtt_port), 'MQTT_USERNAME': '',
                  'MQTT_PASSWORD': '', 'MQTT_KEEPALIVE': 5, 'MQTT_TLS_ENABLED': False}

    mqtt.init_app(app)
    return mqtt
    pass

# init app class for config
class App(object):
    config = {}
    def __init__(self):
        self.config = dict
        pass
    pass


if __name__ == '__main__':
    # test
    mqtt = MqttClientSingle()
    print id(MqttClientSingle())
    print id(MqttClientSingle())
    # 发布
    mqtt.publish("topic", "message")
    # 消费
    mqtt.subscribe("topic")
    pass