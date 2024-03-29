# coding:utf-8
import threading
from Airport.id.new_xingm import *
from Airport.new_method import *
from Airport.id.Idcardnumber import *
from Airport.msgQueue.Autosendlk import *
from Airport.test_预安检人票验证 import *
from Airport.test_预安检口人脸验证 import api_v1_face_pre_security_check
from Airport.test_安检口 import api_v1_face_security_check
from Airport.test_复核口验证 import api_v1_face_review_check
"""参数池"""
inf = ("INF", " ")
# lk_inf = inf[random.randint(0, 1)]   # 带婴儿标志


# 设置预安检通道编号
atYA_list = ["atYA-A", "atYA-B", "atYA-C", "atYA-D", "atYA-E"]
# 设置安检口通道编号
atAJ_list = ["atAJ-A", "atAJ-B", "atAJ-C", "atAJ-D", "atAJ-E"]
# 设置复核口通道编号
atAF_list = ["atAF-A", "atAF-B", "atAF-C", "atAF-D", "atAF-E"]
# 设置设备编号
list_device = ["SB001","SB002","SB003","SB004","SB005","SB006","SB007","SB008","SB009","SB010",
                   "SB012","SB013","SB014","SB015","SB016","SB017","SB018","SB019","SB020"]
device_Id = list_device[random.randint(0, 18)]


def fun1():
    lk_sex = str(random.randint(0, 1))
    lk_cardid = get_random_id_number()
    lk_cname = get_name()
    lk_date = produce_flight_date()
    num = str(random.randint(1, 100000))
    lk_flight = "ZU"+num
    lk_id = get_uuid()
    lk_bdno = get_lk_bdno()

    # 开始发送旅客信息（航班值机信息） 模拟安检系统

    send_lkxx(lk_bdno=lk_bdno,  # 生成随机的101-999的序列号
              lk_cardid=lk_cardid,  # 生成随机的正确的身份证号码
              lk_chkt=get_flight_out_time(),  # 在当前时间上加上对应的延迟时间作为起飞时间
              lk_cname=lk_cname,  # 生成人员姓名
              lk_date=lk_date,  # 以当前时间生成航班日期
              lk_desk=get_lk_desk(),  # 随机生成正确的航班目的地
              lk_flight=lk_flight,  # 累加生成航班号码
              lk_id=lk_id,  # 累加生成旅客id
              lk_inf=inf[random.randint(0, 1)],  # 是否带婴儿
              lk_insur=str(random.randint(0, 1)),  # 设置是否购买保险 设置是否购买保险 随机数
              lk_sex=lk_sex,  # 随机性别
              lk_vip=str(random.randint(0, 2))  # 随机贵宾是否是贵宾 0不是  1是  2未知
              )
    # 验票需要的参数  比对lk_flight 和 li_date

    time.sleep(2)
    body_data = {"reqId": get_uuid(),
                 "flightNo": lk_flight,
                 "flightDay": str(lk_date[6:8]),
                 "QTCode": "abcde",
                 "seatId": "1",
                 "startPort": "HET",
                 "boardingNumber": lk_bdno}
    # 发送请求进行验票
    ticket_check(body_data)

    time.sleep(0.5)
    features_1_1 = "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"

    features_1_N = "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"

    m1 = to_base64(r"D:\work file\project\zhihuipanshi\chenkeyunli_gaitubao_com_150x150.jpg")
    m2 = to_base64(r"D:\work file\project\zhihuipanshi\chenkeyunli_gaitubao_com_150x150.jpg")

    time.sleep(1)
    # 发送预安检人脸验证
    body_data_a = {"reqId": get_uuid(),
                   "gateNo": atYA_list[random.randint(0, 4)],
                   "deviceId": list_device[random.randint(0, 18)],
                   "cardType": 0,  # 证件类型 int
                   "idCard": lk_cardid,
                   "nameZh": lk_cname,
                   "nameEn": "englishName",
                   "age": get_age(lk_cardid),  # int  通过身份证证件号码获取旅客年龄
                   "sex": lk_sex,  # int  获取一致的性别信息
                   "birthDate": get_birthday(lk_cardid),  # 通过前面生成的身份号码获取生日信息
                   "address": "重庆市渝北区大竹林",
                   "certificateValidity": "%s-20201212" % get_birthday(lk_cardid),  # 时间yyyymmdd或者长期(起-止)
                   "nationality": "中国",
                   "ethnic": "汉族",
                   "contactWay": "13512134390",
                   "scenePhoto": m2,
                   "sceneFeature": features_1_1,
                   "cardPhoto": m1,
                   "cardFeature": features_1_1,
                   "flightNo": lk_flight,
                   "flightDay": str(lk_date[6:8]),
                   "QTCode": "abcde",
                   "seatId": "1",
                   "startPort": "HET",
                   "boardingNumber": lk_bdno,
                   "fId": get_uuid()}

    # 发送请求
    api_v1_face_pre_security_check(body_data_a)
    time.sleep(0.5)

    # 进行安检口1:1
    body_data_b = {"reqId": get_uuid(),
                   "gateNo": atAJ_list[random.randint(0, 4)],
                   "deviceId": list_device[random.randint(0, 18)],
                   "cardType": 0,  # 证件类型 int
                   "idCard": lk_cardid,
                   "nameZh": lk_cname,
                   "nameEn": "englishName",
                   "age": get_age(lk_cardid),  # int
                   "sex": lk_sex,  # int
                   "birthDate": get_birthday(lk_cardid),
                   "address": "重庆西南",
                   "certificateValidity": "%s-20201212" % get_birthday(lk_cardid),  # 时间yyyymmdd或者长期(起-止)
                   "nationality": "中国",
                   "ethnic": "汉族",
                   "contactWay": "13512134390",
                   "scenePhoto": m2,
                   "sceneFeature": features_1_1,
                   "cardPhoto": m1,
                   "cardFeature": features_1_1}
    # 发送请求
    api_v1_face_security_check(body_data_b)
    time.sleep(1.5)

    # 进行安检复核
    body_data_c = {"reqId": get_uuid(),
                   "gateNo": atAF_list[random.randint(0, 4)],
                   "deviceId": list_device[random.randint(0, 18)],
                   "scenePhoto": m1,
                   "sceneFeature": features_1_N}

    # 发送请求
    api_v1_face_review_check(body_data_c)

    # 发送安检状态
    safe_number_list = ["10", "20", "30", "40", "50", "60"]
    safe_number = safe_number_list[random.randint(0, 5)]  # 安检通道号

    safe_operation_list = ["PA0101", "PA0102", "PA0103", "PA0104", "PA0105", "PA0106", "PA0107", "PA0108",
                           "PA0109", "PA0110"]
    safe_opera = safe_operation_list[random.randint(0, 9)]  # 安检验证员

    send_ajxx(ajxxb_id=get_uuid(),
              lk_id=lk_id,
              safe_flag="1",  # 安检状态 1已安检 0是未安检
              safe_no=safe_number,  # 安检通道号
              safe_oper=safe_opera,  # 安检验证员
              safe_time=get_time_mmss())


threads = []
t1 = threading.Thread(fun1(), args=())
threads.append(t1)
t2 = threading.Thread(fun1(), args=())
threads.append(t2)

if __name__ == '__main__':
    while True:
        for i in threads:
            i.start()
        i.join()