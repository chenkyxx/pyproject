# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_system_area_update(body):
    """
    调用区域信息更新接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/system/area/update"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/system/area/update" + timestamp + apiKey
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
        "id": "1a9a01b1942141e3ae620a2db246280121212121",  # 需要修改的区域id
        "level": "1",
        "name": "区域名称100000000000000000000000000000000",
        "code": "区域名称100000000000",
        "size": "区域尺寸13223",
        "note": "区域备注133330000000",
    }
    api_v1_system_area_update(body)