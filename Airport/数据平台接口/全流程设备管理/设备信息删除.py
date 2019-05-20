# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_system_device_delete(body):
    """
    调用设备信息删除接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/system/device/delete"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/system/device/delete" + timestamp + apiKey
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
    body = {"reqId":get_uuid(),
            "ids": "4028806b6689e02001668a46c7e100d5,1111"
            }
    api_v1_system_device_delete(body)