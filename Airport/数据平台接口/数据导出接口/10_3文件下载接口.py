# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_analysis_export_schedule(body):
    """
    调用2.4.10.3文件下载
    :return:
    """
    url = "http://192.168.0.234:9090/data-server/api/v1/analysis/export/download/具体文件名"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/analysis/export/download/具体文件名" + timestamp + apiKey
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
        "serialNum": "唯一的标志 序列号",
        }
    api_v1_analysis_export_schedule(body="")