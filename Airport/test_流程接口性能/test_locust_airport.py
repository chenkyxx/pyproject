# coding:utf-8
from locust import HttpLocust, task, TaskSequence, seq_task,TaskSet
from Airport.id.new_xingm import *
from Airport.id.Idcardnumber import *
from Airport.msgQueue.Autosendlk import *
from Airport.test_预安检人票验证 import *
from Airport.test_预安检口人脸验证 import api_v1_face_pre_security_check
from Airport.test_安检口 import api_v1_face_security_check
from Airport.test_复核口验证 import api_v1_face_review_check
import json
"""参数池"""
inf = ("INF", " ")
# lk_inf = inf[random.randint(0, 1)]   # 带婴儿标志


# 设置预安检通道编号
atYA_list = ["T1YA", "T1YA", "T1YA", "T1YA", "T2YA"]
# 设置安检口通道编号
atAJ_list = ["T1AJ", "T1AJ", "T1AJ", "T2AJ", "T1AJ"]
# 设置复核口通道编号
atAF_list = ["T1AF", "T1AF", "T1AF", "T1AF", "T2AF"]
# 设置设备编号
list_device = ["002","003","005","007","008","002","003","005","007","008",
                   "002","003","005","007","008","002","003","005","007"]
device_Id = list_device[random.randint(0, 18)]


class UserBehavior(TaskSequence):

    @task(1)
    def first_task(self):
        lk_sex = str(random.randint(0, 1))
        lk_cardid = get_random_id_number()
        lk_cname = get_name()
        lk_date = produce_flight_date()
        num = random.randint(1, 9999999)
        lk_flight = "cq"+str(num)
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
        time.sleep(1)
        # 验票需要的参数  比对lk_flight 和 li_date
        body_data = {"reqId": get_uuid(),
                     "flightNo": lk_flight,
                     "flightDay": str(lk_date[6:8]),
                     "QTCode": "abcde",
                     "seatId": "1",
                     "startPort": "HET",
                     "boardingNumber": lk_bdno}
        # 发送请求进行验票
        try:
            data_q = ticket_check(body_data)
            dict_qq = json.loads(data_q)
            assert dict_qq["result"] ==0
        except Exception as E1:
            with open("qq.txt","a+") as fq:
                fq.write("time:%s appear error---%s" % (get_time_mmss(), E1)+"\n")
        time.sleep(0.5)
        features_1_1 = "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"
        features_1_N = "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"

        m1 = to_base64(r"D:\work file\project\zhihuipanshi\chenkeyunli_gaitubao_com_150x150.jpg")
        m2 = to_base64(r"D:\work file\project\zhihuipanshi\chenkeyunli_gaitubao_com_150x150.jpg")

        time.sleep(2)
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
        try:
            data_w = api_v1_face_pre_security_check(body_data_a)
            dict_ww = json.loads(data_w)
            assert dict_ww["result"] ==0
        except Exception as E2:
            with open("ww.txt","a+") as fw:
                fw.write("time:%s appear error---%s" % (get_time_mmss(), E2)+"\n")
        time.sleep(1)
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
        try:
            data_e = api_v1_face_security_check(body_data_b)
            dict_ee = json.loads(data_e)
            assert dict_ee["result"] == 0
        except Exception as E3:
            with open("ee.txt", "a+") as fe:
                fe.write("time:%s appear error---%s" % (get_time_mmss(), E3)+"\n")
        time.sleep(1.5)
        # 进行安检复核
        body_data_c = {"reqId": get_uuid(),
                       "gateNo": atAF_list[random.randint(0, 4)],
                       "deviceId": list_device[random.randint(0, 18)],
                       "scenePhoto": m1,
                       "sceneFeature": features_1_N}

        # 发送请求
        try:
            data_r = api_v1_face_review_check(body_data_c)
            dict_rr = json.loads(data_r)
            assert dict_rr["result"] == 0
        except Exception as E4:
            with open("rr.txt", "a+") as fr:
                fr.write("time:%s appear error---%s" % (get_time_mmss(), E4)+"\n")
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
        time.sleep(1)


    # @seq_task(2)
    # @task(2)
    # def second_task(self):
    #     self.client.get("/")
    #
    # @seq_task(3)
    # @task(5)
    # def third_task(self):
    #     self.client.get("/")


class User(HttpLocust):
    task_set = UserBehavior
    max_wait = 500
    min_wait = 100
    host = "http://192.168.0.234:9090"


if __name__ == "__main__":
    command1 = "d:"
    command2 = r"cd D:\work file\Auto test\pythonproject\Airport\test_流程接口性能"
    command3 = r"locust -f test_locust_airport.py --web-host=192.168.0.125"
    os.system(command1)
    os.system(command2)
    os.system(command3)