# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_form_login(body):
    """
    调用旅客登录接口
    :return:
    """
    url = "http://192.168.0.56:80/api/v1/analysis/passenger/data"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/analysis/passenger/data" + timestamp + apiKey
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
    body = {"loginname": "登录名",
            "pwd": ""
            }
    response = api_v1_form_login(body)
