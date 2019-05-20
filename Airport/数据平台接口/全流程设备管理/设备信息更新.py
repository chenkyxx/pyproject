# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_system_device_update(body):
    """
    调用设备信息更新接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/system/device/update"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/system/device/update" + timestamp + apiKey
    sign2 = to_md5_str(sign1)
    header = {"apiId": apiId,
              "sign": sign2,
              "timestamp": timestamp,
              "Content-Type": "application/json; charset=utf-8"}
    res = requests.post(url=url,
                        headers=header,
                        json=body,
                        verify=False)
    print(res.text)
    return res.text


if __name__ == '__main__':
    body = {"reqId": get_uuid(),
            "id": "4028806b66812c380166815111210000",
            "code": "shebei01",
            "name": "设备名称1",
            "areaId": "85df90517964488ba15e33c89b883805",
            "type": "700",
            "time": "20181213140000",
            "config": ""
            }
    api_v1_system_device_update(body)