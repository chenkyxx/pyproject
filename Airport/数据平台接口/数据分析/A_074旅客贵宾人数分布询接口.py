# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_analysis_passenger_viprate(body):
    """
    调用2.4.7.4旅客贵宾人数分布查询接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/analysis/passenger/viprate"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/analysis/passenger/viprate" + timestamp + apiKey
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
    print(res.elapsed.total_seconds())   # 服务器响应时间
    return res.text


if __name__ == '__main__':
    body = {
        "reqId": "32位UUID",
        "startTime": "2018092208000000",
        "endTime": "2018102208000000"
        }
    api_v1_analysis_passenger_viprate(body)