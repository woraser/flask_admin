#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.models import SensorData, User
from app.decoratorUtil import catchDbException
import random, time, collections


def getTestData():
    insert_data = []
    format_time = time.time()
    for i in range(100):
        insert_data.append({
            "no": str(i),
            "val": random.randint(0, 100),
            "created_time": format_time
        })
        pass
    SensorData().insert_many(insert_data).execute()
    pass



@catchDbException
def getData():
    return User().get(User.account == 'chenhuiggggg')

def getSensorData():
    account = getData()
    if account is None:
        return 'result is none'
        pass
    return account._data
    pass

if __name__ == '__main__':
    print getSensorData()
