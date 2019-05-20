# coding:utf-8
from Airport.msgQueue.Autosendlk import *
from Airport.id.Idcardnumber import get_random_id_number
from Airport.test_预安检人票验证 import *
from Airport.test_预安检口人脸验证 import api_v1_face_pre_security_check
from Airport.test_安检口 import api_v1_face_security_check
from Airport.test_复核口验证 import api_v1_face_review_check
from Airport.id.new_xingm import *

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

# 设置循环累加数
jj = 1
k = 1
while k < 1001:
    lk_sex = str(random.randint(0, 1))
    lk_cardid = get_random_id_number()
    lk_cname = get_name()
    lk_date = produce_flight_date()
    lk_flight = "101502" + str(jj)
    lk_id = "014"+str(jj)
    lk_bdno = get_lk_bdno()

    # 开始发送旅客信息（航班值机信息） 模拟安检系统

    send_lkxx(lk_bdno=lk_bdno,  # 生成随机的101-999的序列号
              lk_cardid=lk_cardid,    # 生成随机的正确的身份证号码
              lk_chkt=get_flight_out_time(),  # 在当前时间上加上对应的延迟时间作为起飞时间
              lk_cname=lk_cname,  # 生成人员姓名
              lk_date=lk_date,    # 以当前时间生成航班日期
              lk_desk=get_lk_desk(),  # 随机生成正确的航班目的地
              lk_flight=lk_flight,    # 累加生成航班号码
              lk_id=lk_id,            # 累加生成旅客id
              lk_inf=inf[random.randint(0, 1)],          # 是否带婴儿
              lk_insur=str(random.randint(0, 1)),      # 设置是否购买保险 设置是否购买保险 随机数
              lk_sex=lk_sex,          # 随机性别
              lk_vip=str(random.randint(0, 2))           # 随机贵宾是否是贵宾 0不是  1是  2未知
              )
    # 验票需要的参数  比对lk_flight 和 li_date
    time.sleep(0.5)
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
    # 1：1证件照片和现场照的features
    features_path = "E:/test1000/1比1id1000features"
    # 1:N证件照的features路径
    features_path_N = "E:/test1000/1比Nid1000features"
    try:
        with open((features_path+"/"+"%d" % k+".jpg.txt")) as fp:
            features_1 = fp.read().rstrip()
    except Exception as A:
        raise A
    features_1_1 = features_1
    try:
        with open((features_path_N+"/"+"%d" % k+".jpg.txt")) as fp1:
            features_N = fp1.read().rstrip()
    except Exception as A:
        raise A
    features_1_N = features_N

    m1 = to_base64(r"D:\work file\project\zhihuipanshi\chenkeyunli_gaitubao_com_150x150.jpg")
    m2 = to_base64(r"D:\work file\project\zhihuipanshi\chenkeyunli_gaitubao_com_150x150.jpg")

    time.sleep(0.5)
    # 发送预安检人脸验证
    body_data_a ={"reqId": get_uuid(),
                  "gateNo": atYA_list[random.randint(0, 4)],
                  "deviceId": list_device[random.randint(0, 18)],
                  "cardType": 0,     # 证件类型 int
                  "idCard": lk_cardid,
                  "nameZh": lk_cname,
                  "nameEn": "englishName"+str(jj),
                  "age": get_age(lk_cardid),  # int  通过身份证证件号码获取旅客年龄
                  "sex": lk_sex,  # int  获取一致的性别信息
                  "birthDate": get_birthday(lk_cardid), # 通过前面生成的身份号码获取生日信息
                  "address": "重庆市渝北区大竹林"+str(jj),
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
    time.sleep(1)

    # 进行安检口1:1
    body_data_b = {"reqId": get_uuid(),
                   "gateNo": atAJ_list[random.randint(0, 4)],
                   "deviceId": list_device[random.randint(0, 18)],
                   "cardType": 0,  # 证件类型 int
                   "idCard": lk_cardid,
                   "nameZh": lk_cname,
                   "nameEn": "englishName"+str(jj),
                   "age": get_age(lk_cardid),  # int
                   "sex": lk_sex,  # int
                   "birthDate": get_birthday(lk_cardid),
                   "address": "重庆西南"+str(jj),
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
    check = api_v1_face_review_check(body_data_c)
    check1 = json.loads(check.text)
    try:
        assert check1["userInfo"]["cardNo"] == lk_cardid
    except Exception:
        with open("20181010.txt", "a") as fp:
            fp.write("error-----%d" % k + "\n")

    # 发送安检状态
    safe_number_list = ["10","20","30","40","50","60"]
    safe_number= safe_number_list[random.randint(0, 5)]  # 安检通道号

    safe_operation_list = ["PA0101","PA0102","PA0103","PA0104","PA0105","PA0106","PA0107","PA0108",
                           "PA0109","PA0110"]
    safe_opera = safe_operation_list[random.randint(0, 9)]   # 安检验证员

    send_ajxx(ajxxb_id="ajxxid"+str(jj),
              lk_id=lk_id,
              safe_flag="1",  # 安检状态 1已安检 0是未安检
              safe_no=safe_number,  # 安检通道号
              safe_oper=safe_opera,  # 安检验证员
              safe_time=get_time_mmss())
    jj += 1
    if k==1000:
        k = 1
    else:
        k += 1