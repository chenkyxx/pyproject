# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_system_area_save(body):
    """
    2.2.13.1调用区域信息新增接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/system/area/save"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/system/area/save" + timestamp + apiKey
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
        "reqId": get_uuid(),
        "parentId": "",  # 父级区域Id，建立1级航站楼的时候为空
        "level": "1",
        "name": "aaa0000000000000000000000000000000000000000000000000000000",
        "code": "atAJ00",
        "size": "区域尺寸",
        "note": "区域备注",
        "externalCode": None

    }
    api_v1_system_area_save(body)