# coding:utf-8
import requests
from Airport.new_method import *
import json


def api_v1_face_pre_security_check(body):
    """
    预安检口1：1人脸验证
    :return:
    """
    # url = "http://192.168.10.188:9090/presecurity-server/api/v1/face/pre-security/check"
    url = "http://192.168.10.194:13000/api/v1/face/pre-security/check"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/face/pre-security/check" + timestamp + apiKey
    sign2 = to_md5_str(sign1)
    header = {"apiId": apiId,
              #"backupId": "cigit188",
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
    with open(r"D:\test1000\1比1id1000features\50.jpg.txt", "r") as fp:
        data1 = fp.read().rstrip()
        data2 = str(data1)
    feature_id = data2
    with open(r"D:\test1000\1比1id1000features\50.jpg.txt", "r") as fp1:
        data3 = fp1.read().rstrip()
        data4 = str(data3)
    feature_live = data4
    m1 = to_base64(r"C:\Users\Administrator\Desktop\100000.JPG")
    m2 = to_base64(r"C:\Users\Administrator\Desktop\100000.JPG")

    body_data = {"reqId": get_uuid(),
                 "gateNo": "T1YA2",
                 "deviceId": "T1YA002",
                 "cardType": 0,     # 证件类型 int
                 "idCard": "200238199312134390",
                 "nameZh": "TEST1",
                 "nameEn": "CHENKEYUN",
                 "age": 25,  # int
                 "sex": 1,  # int
                 "birthDate": "19931213",
                 "address": "呼和浩特切换",
                 "certificateValidity": "20181012-长期",  # 时间yyyymmdd或者长期(起-止)
                 "nationality": "中国",
                 "ethnic": "汉族",
                 "contactWay": "119110",
                 "scenePhoto": m2,
                 "sceneFeature": feature_live,
                 "cardPhoto": m1,
                 "cardFeature": feature_id,
                 "flightNo": "TestA0011",
                 "flightDay": "01",
                 "QTCode": "1212131",
                 "seatId": "15C",
                 "startPort": "HET",
                 "boardingNumber": "111",
                 "fId": get_uuid()}
    try:
        data_2 = api_v1_face_pre_security_check(body_data)
        dict_data = json.loads(data_2)
        assert dict_data["result"] == 0
    except Exception as A1:
        with open("renlianyanzheng.txt","a+") as z1:
            z1.write("time:%s appear error---%s" % (get_time_mmss(), A1)+"\n")



