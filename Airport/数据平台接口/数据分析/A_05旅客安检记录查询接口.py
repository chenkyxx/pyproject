# coding:utf-8
import requests
from Airport.new_method import *


def api_v1_face_security_record(body):
    """
    调用旅客安检记录查询接口
    :return:
    """
    url = "http://192.168.10.188:9090/data-platform-server/api/v1/face/security/record"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/face/security/record" + timestamp + apiKey
    sign2 = to_md5_str(sign1)
    header = {"apiId": apiId,
              "backupId": "cigit188",
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
        # "name": "12323",
        # "cardType": "0",
        # "idCard": "500238199312134390",
        "startTime": "20180701091232",
        "endTime": "20181201091232",
        "page": "1",  # int
        "pageSize": "1",
        "isCount": "1"
        }
    api_v1_face_security_record(body)