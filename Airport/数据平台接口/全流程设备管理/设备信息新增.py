# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_system_device_save(body):
    """
    调用设备信息新增接口
    :param body:
    :return:
    """
    url = "http://192.168.10.188:9090/data-platform-server/api/v1/system/device/save"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/system/device/save" + timestamp + apiKey
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
    body = {"reqId": "11",
            "code": "12m5623456789012345",
            "name": "shebei02",
            "areaId": "121231",
            "type": "700",
            "time": "1221131111100",
            "config": "test1111"
            }
    api_v1_system_device_save(body)
