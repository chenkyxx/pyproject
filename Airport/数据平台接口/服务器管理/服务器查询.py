# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_system_server_query(body):
    """
    调用服务器信息查询接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-server/api/v1/system/server/query"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/system/server/query" + timestamp + apiKey
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
    #while True:
        body = {
            "reqId": get_uuid(),
            "name": "人脸识别服务器",
            "kind": "300",  # 服务器类型（给的是字典表里面的id）
            "status": 1,  # 状态
            "page": "1",  # 分页页码 int
            "pageSize": "2",  # 分页长度 int
            "isCount": "1",  # 为1的时候查询总记录数 int
        }
        api_v1_system_server_query(body)