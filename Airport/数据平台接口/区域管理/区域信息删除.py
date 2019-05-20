# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_system_area_delete(body):
    """
    调用区域信息删除接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/system/area/delete"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/system/area/delete" + timestamp + apiKey
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
    body = {
        "reqId": "1",
        "ids": "1111",  # 需要删除的区域id
    }
    api_v1_system_area_delete(body)