# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_analysis_passenger_agerate(body):
    """
    调用2.4.7.2旅客年龄人数分布查询接口
    :return:
    """
    url = "http://192.168.10.188:9090/data-platform-server/api/v1/analysis/passenger/agerate"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/analysis/passenger/agerate" + timestamp + apiKey
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
    start = time.clock()
    body = {
        "reqId": "32位UUID",
        "startTime": "2018092208000000",
        "endTime": "2018122208000000"
        }
    api_v1_analysis_passenger_agerate(body)
    end = time.clock()
    print(str(end-start)+"s")