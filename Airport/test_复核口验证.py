# coding:utf-8
import requests
from Airport.new_method import *
import json


def api_v1_face_review_check(body):
    """
    2.3.6复核口服务器接口（对外）
    :param body:发送安检复核请求到服务器  body作为参数
    :return:
    """
    url = "http://192.168.10.188:9090/review-server/api/v1/face/review/check"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/face/review/check" + timestamp + apiKey
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
    m2 = to_base64(r"C:\Users\Administrator\Desktop\100000.JPG")
    with open(r"D:\test1000\1比Nid1000features\51.jpg.txt", "r") as fp1:
        data3 = fp1.read().rstrip()
        live_feature = str(data3)
    a = get_uuid()
    body_data = {"reqId": a,
                 "gateNo": "T1AF2",
                 "deviceId": "T1AF002",
                 "scenePhoto": m2,
                 "sceneFeature": live_feature
                 }
    try:
        data_4 = api_v1_face_review_check(body_data)
        dict_data4 = json.loads(data_4)
        assert dict_data4["result"] ==0
    except Exception as A4:
        with open("fuhekou.txt", "a+") as z4:
            z4.write("time:%s appear error---%s" % (get_time_mmss(), A4)+"\n")

