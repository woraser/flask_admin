/**
 * Created by chenhui on 2017/6/22.
 * 传感器 dht11
 * temp 温度
 * humi 湿度
 */
var dht11 = require('dht11');
    if (dht11.fetch())
    {
        print("val_temp: " + dht11.readTemperature());
        print("val_humi: " + dht11.readHumidity());
    }
    else
    {
        print("fetch error");
    }
    exit(0)
