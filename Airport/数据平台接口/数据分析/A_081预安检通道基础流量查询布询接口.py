# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_analysis_pre_security_efficiency(body):
    """
    调用2.4.8.1预安检通道基础流量查询接口
    :return:
    """
    url = "http://192.168.0.234:9090/data-platform-server/api/v1/analysis/pre-security/efficiency"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/analysis/pre-security/efficiency" + timestamp + apiKey
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
        "reqId": "32位UUID",
        "areaCode": "atYA-A",  # 通道编号(区域表里面的编号)
        "startTime": "2018092300000000",
        "endTime": "2018102300000000"
        }
    api_v1_analysis_pre_security_efficiency(body)