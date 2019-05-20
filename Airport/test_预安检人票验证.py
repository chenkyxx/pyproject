# coding:utf-8
import requests
from Airport.new_method import *
import json


def ticket_check(body):
    url = "http://192.168.10.188:9090/presecurity-server/api/v1/ticket/check"
    apiId = "123456"
    apiKey = "1285384ddfb057814bad78127bc789be"
    timestamp = get_time_stamp()
    sign1 = "/api/v1/ticket/check" + timestamp + apiKey
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

    # m = json.loads(res.text)
    # print(m)
    # print(type(m))


if __name__ == '__main__':
    body_data = {"reqId": get_uuid(),
                 "flightNo": "TestA001",
                 "flightDay": "01",
                 "QTCode": "1212131",
                 "seatId": "15C",
                 "startPort": "HET",
                 "boardingNumber": "111"}

    ticket_check(body_data)
    # try:
    #     data = ticket_check(body_data)
    #     dict_1 = json.loads(data)
    #     assert dict_1["result"] == 0
    # except Exception as A:
    #     print(A)
    #     with open("renpiao.txt", "a+") as f:
    #         f.write("time:%s appear error---%s" % (get_time_mmss(), A)+"\n")

