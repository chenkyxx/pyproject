# coding:utf-8
from BaiTaAirport2_month.API.BlackList import *
from BaiTaAirport2_month.TestData.PictureBase64One import Base64Picture


class AirportProcess(BlackListApi):
    def __init__(self, host="http://192.168.10.188:9090/"):
        BlackListApi.__init__(self, host)
        self.A_security_ticket_check = self.host + self.anjian_server + "/api/v1/face/security/ticket-check"
        self.B_security_face_check = self.host + self.anjian_server + "/api/v1/face/security/face-check"
        self.api_v1_face_review_check = self.host + self.review_server + "/api/v1/face/review/check"
        self.api_v1_face_review_manual_check = self.host + self.review_server + "/api/v1/face/review/manual-check"  # 复核人工通道
        self.api_v1_face_security_manual_check = self.host + self.anjian_server + "/api/v1/face/security/manual-check"  # 安检人工通道
        self.api_v1_face_transfergate_ticket_collect = self.host + self.boardinggate_server + "/api/v1/face/transfergate/ticket-collect"
        self.api_v1_face_notice_crateLib = self.host + self.boardinggate_server + "/api/v1/face/notice/crateLib"  # 登机口通知建库
        self.api_v1_face_boarding_check = self.host + self.boardinggate_server + "/api/v1/face/boarding/check"  # 登机口复核
        self.api_v1_face_boarding_library_check = self.host + self.boardinggate_server + "/api/v1/face/boarding/library-check"  # 登机口建库人数查询
        self.api_v1_face_boarding_manual_check = self.host + self.boardinggate_server + "/api/v1/face/boarding/manual-check"  # 登机口人工放行报警
        self.api_v1_face_data_flowback_query = self.host+self.data_platform_server +"/api/v1/face/data/flowback-query" # 用于登机口，安检口人员回查功能
        self.api_v1_face_security_manual_optcheck = self.host + self.anjian_server + "/api/v1/face/security/manual-optcheck"  # 安检口人工放行
        self.api_anjian1_1 = self.host+self.anjian_server+"/api/v1/face/security/check"  # 安检1：1人脸验证
        self.api_v1_face_review_self_check = self.host+self.review_server+"/api/v1/face/review/self-check"  # 自助闸机复核接口

    def api_security_ticket_check(self,
                                  reqId=get_uuid(),
                                  gateNo="",
                                  deviceId="",
                                  cardType="0",
                                  idCard="",
                                  nameZh="nameZh",
                                  nameEn="nameEn",
                                  age=None,
                                  sex=None,
                                  birthDate="",
                                  address="重庆市",
                                  certificateValidity="20120101-20230202",
                                  nationality="CHina",
                                  ethnic="汉族",
                                  contactWay="0123456789",
                                  cardPhoto="",
                                  fId=get_uuid()
                                  ):
        """2.3.14自助验证闸机A门接口（二期)"""
        body = {"reqId": reqId,
                "gateNo": gateNo,
                "deviceId": deviceId,
                "cardType": cardType,
                "idCard": idCard,
                "nameZh": nameZh,  # 非必填
                "nameEn": nameEn,  # 非必填
                "age": age,  # 非必填
                "sex": sex,  # 非必填
                "birthDate": birthDate,
                "address": address,  # 非必填
                "certificateValidity": certificateValidity,
                "nationality": nationality,  # 非必填
                "ethnic": ethnic,  # 非必填
                "contactWay": contactWay,  # 非必填
                "cardPhoto": cardPhoto,
                "fId": fId}
        res = requests.post(url=self.A_security_ticket_check,
                            json=body,
                            headers=self.get_headers("/api/v1/face/security/ticket-check"),
                            verify=False)
        res.close()
        return res

    def api_face_security_face_check(self,
                                     reqId=get_uuid(),
                                     gateNo="",
                                     deviceId="",
                                     cardType="",
                                     idCard="",
                                     nameZh="nameZh",
                                     nameEn="nameEn",
                                     age="",
                                     sex="",
                                     birthDate="",
                                     address="重庆市",
                                     certificateValidity="20180101-20260203",
                                     nationality="China",
                                     ethnic="汉族",
                                     contactWay="0123456789",
                                     scenePhoto="",
                                     sceneFeature="",
                                     cardPhoto="",
                                     cardFeature=""):
        """2.3.15自助验证闸机B门接口（二期）"""
        body = {"reqId": reqId,
                "gateNo": gateNo,
                "deviceId": deviceId,
                "cardType": cardType,
                "idCard": idCard,
                "nameZh": nameZh,  # 非必填
                "nameEn": nameEn,  # 非必填
                "age": age,  # 非必填
                "sex": sex,  # 非必填
                "birthDate": birthDate,
                "address": address,  # 非必填
                "certificateValidity": certificateValidity,
                "nationality": nationality,  # 非必填
                "ethnic": ethnic,  # 非必填
                "contactWay": contactWay,  # 非必填
                "scenePhoto": scenePhoto,
                "sceneFeature": sceneFeature,
                "cardPhoto": cardPhoto,
                "cardFeature": cardFeature
                }
        res = requests.post(url=self.B_security_face_check,
                            json=body,
                            headers=self.get_headers("/api/v1/face/security/face-check"),
                            verify=False)
        res.close()
        return res

    def api_anjian(self,
                     anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard="300238199312134390",
                     nameZh="铁塔",
                     nameEn="CHENKEYUN",
                     age=25,
                     sex=1,
                     birthDate=get_birthday("300238199312134390"),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto="204.jpg",
                     sceneFeature="",
                     cardPhoto="204.jpg",
                     cardFeature="",
                   ):
        """安检1：1人脸验证"""
        body = {"reqId": get_uuid(),
                 "gateNo": anjiangateNo,
                 "deviceId": anjiandeviceId,
                 "cardType": cardType,  # 证件类型 int
                 "idCard": idCard,
                 "nameZh": nameZh,
                 "nameEn": nameEn,
                 "age": age,  # int
                 "sex": sex,  # int
                 "birthDate": birthDate,
                 "address": address,
                 "certificateValidity": "20081010-20191206",  # 时间yyyymmdd或者长期(起-止)
                 "nationality": nationality,
                 "ethnic": ethnic,
                 "contactWay": "18680946659",
                "scenePhoto": scenePhoto,
                 "sceneFeature": sceneFeature,
                 "cardPhoto": cardPhoto,
                 "cardFeature": cardFeature,
                 }
        res = requests.post(url=self.api_anjian1_1,
                            json=body,
                            headers=self.get_headers("/api/v1/face/security/check"),
                            verify=False)
        res.close()
        return res

    def api_face_review_self_check(self,
                                   reqid=get_uuid(),
                                   gateno="",
                                   deviceid="",
                                   scenephoto="",
                                   scenefeature=""):
        """2.3.16 自助闸机复核接口（二期）"""
        body = {"reqId": reqid,
                "gateNo": gateno,
                "deviceId": deviceid,
                "scenePhoto": scenephoto,
                "sceneFeature": scenefeature}
        res = requests.post(url=self.api_v1_face_review_self_check,
                            json=body,
                            headers=self.get_headers("/api/v1/face/review/self-check"),
                            verify=False)
        res.close()
        return res

    def api_face_review_check(self,
                              reqId=get_uuid(),
                              gateNo="",
                              deviceId="",
                              scenePhoto="",
                              sceneFeature=""):
        """2.3.6复核口服务器接口（二期优化）"""
        body = {"reqId": reqId,
                "gateNo": gateNo,
                "deviceId": deviceId,
                "scenePhoto": scenePhoto,
                "sceneFeature": sceneFeature}
        res = requests.post(url=self.api_v1_face_review_check,
                            headers=self.get_headers("/api/v1/face/review/check"),
                            json=body,
                            verify=False)
        res.close()
        return res

    def api_face_review_manual_check(self,
                                     reqId=get_uuid(), gateNo="", deviceId="", scenePhoto="", cardNo="",
                                     passengerName="", passengerEnglishName="", securityStatus="",
                                     securityPassTime="", securityGateNo="", securityDeviceNo="",
                                     flightNo="", boardingNumber="",
                                     sourceType=""):
        """2.3.7复核口人工复核接口（二期)安检的状态(0人证1:1 1 人工放行 2闸机B门通过 3-未知)"""
        body = {"reqId": reqId,
                "gateNo": gateNo,
                "deviceId": deviceId,
                "scenePhoto": scenePhoto,  # 否 现场照base64编码，有现场照就上传现场照
                "cardNo": cardNo,
                "passengerName": passengerName,
                "passengerEnglishName": passengerEnglishName,
                "securityStatus": securityStatus,
                "securityPassTime": securityPassTime,
                "securityGateNo": securityGateNo,  # 否
                "securityDeviceNo": securityDeviceNo,  # 否
                "flightNo": flightNo,
                "boardingNumber": boardingNumber,
                "sourceType": sourceType}
        res = requests.post(url=self.api_v1_face_review_manual_check,
                            headers=self.get_headers("/api/v1/face/review/manual-check"),
                            json=body,
                            verify=False)
        res.close()
        return res

    def api_face_security_manual_check(self,
                                       reqId=get_uuid(),
                                       flightNo="HU002",
                                       faceImage=Base64Picture,
                                       gateNo="T1AJ1",
                                       deviceCode="T1AJMM007",
                                       boardingNumber="010",
                                       seatId="001",
                                       startPort="HET",
                                       flightDay="1",
                                       faceFeature="",
                                       kindType=0                  # 类型：0：刷票 1：刷票放行
                                       ):
        """2.3.8安检人工通道接口，直接刷票（一期二阶段）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "faceImage": faceImage,
                "gateNo": gateNo,
                "deviceCode": deviceCode,
                "boardingNumber": boardingNumber,
                "seatId": seatId,
                "startPort": startPort,
                "flightDay": flightDay,
                "faceFeature": faceFeature,
                "kindType": kindType
                }
        res = requests.post(url=self.api_v1_face_security_manual_check,
                            headers=self.get_headers("/api/v1/face/security/manual-check"),
                            json=body,
                            verify=False)
        res.close()
        return res

    def api_face_transfergate_ticket_collect(self,
                                             reqId=get_uuid(),
                                             flightNo="test006",
                                             faceImage="",
                                             deviceCode="T1ZZ002",
                                             gateNo="",
                                             seatId="1",
                                             startPort="HET",
                                             boardingNumber="001",
                                             flightDay="20181225",   # 传Dd
                                             faceFeature="",
                                             sourceType="0"):
        """2.3.9中转通道接口（一期二阶段）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "faceImage": faceImage,
                "gateNo": gateNo,
                "deviceCode": deviceCode,
                "boardingNumber": boardingNumber,
                "seatId": seatId,
                "startPort": startPort,
                "flightDay": flightDay,    # DD
                "faceFeature": faceFeature,
                "sourceType": sourceType
                }
        res = requests.post(url=self.api_v1_face_transfergate_ticket_collect,
                            headers=self.get_headers("/api/v1/face/transfergate/ticket-collect"),
                            json=body,
                            verify=False)
        res.close()
        return res

    def api_face_notice_cratelib(self,
                                 reqId=get_uuid(),
                                 flightNo="DL04462",
                                 date="20190121",
                                 boardingGate="14",
                                 deviceCode="T1DJ001",
                                 number=200,
                                 outTime=get_flight_out_time(1)
                                 ):
        """登机口复核建库通知接口"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "date": date,
                "boardingGate": boardingGate,
                "deviceCode": deviceCode,
                "number": number,
                "outTime": outTime
                }

        res = requests.post(url=self.api_v1_face_notice_crateLib,
                            headers=self.get_headers("/api/v1/face/notice/crateLib"),
                            json=body,
                            verify=False)
        res.close()
        return res

    def api_face_boarding_review_check(self, reqId=get_uuid(),
                                faceImage="",
                                faceFeature="",
                                deviceCode="T1DJ001",
                                boardingGate="14",
                                flightNo="DL04462",
                                flightDay="20190121"   # （yyyyMMdd）
                                ):
        """2.3.11登机口复核接口（二期优化）"""
        body = {"reqId": reqId,
                "faceImage": faceImage,
                "faceFeature": faceFeature,
                "deviceCode": deviceCode,
                "boardingGate": boardingGate,
                "flightNo": flightNo,
                "flightDay": flightDay}
        res = requests.post(url=self.api_v1_face_boarding_check,
                            headers=self.get_headers("/api/v1/face/boarding/check"),
                            json=body,
                            verify=False)
        res.close()
        return res

    def api_face_boarding_library_check(self,
                                        reqId=get_uuid(),
                                        flightNo="",
                                        date="",
                                        boardingGate="",
                                        deviceCode="",
                                        gateNo=""):
        """2.3.12登机口建库人数查询接口（二期）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "date": date,
                "boardingGate": boardingGate,
                "deviceCode": deviceCode,
                "gateNo": gateNo}
        res = requests.post(url=self.api_v1_face_boarding_library_check,
                            headers=self.get_headers("/api/v1/face/boarding/library-check"),
                            json=body,
                            verify=False)
        res.close()
        return res.text

    def api_face_boarding_manual_check(self,
                                       reqId=get_uuid(),
                                       flightNo="",
                                       date="",
                                       boardingGate="",
                                       deviceCode="",
                                       gateNo="",
                                       cardId="",
                                       scenePhoto="",
                                       sourceType="",
                                       passengerName="",
                                       boardingNumber=""
                                       ):
        """2.3.13登机口人工放行、报警接口（二期）"""
        body = {"reqId": reqId,
                "flightNo": flightNo,
                "date": date,
                "boardingGate": boardingGate,
                "deviceCode": deviceCode,
                "gateNo": gateNo,
                "cardId": cardId,
                "scenePhoto": scenePhoto,
                "sourceType": sourceType,  # 0-放行，1-报警
                "passengerName": passengerName,
                "boardingNumber": boardingNumber}
        res = requests.post(url=self.api_v1_face_boarding_manual_check,
                            headers=self.get_headers("/api/v1/face/boarding/manual-check"),
                            json=body,
                            verify=False)
        res.close()
        print(body)
        return res

    def api_face_data_flowback_query(self,
                                     reqId=get_uuid(),
                                     cardId="",
                                     flightNo="",
                                     flightDay="",   # 航班dd
                                     boardingNumber=""):
        """2.3.17 人员回查-安检、登机口接口（二期）"""
        body = {"reqId": reqId,
                "cardId": cardId,  # 否
                "flightNo": flightNo,  # 否
                "flightDay": flightDay,  # 否
                "boardingNumber": boardingNumber}  # 否
        res = requests.post(url=self.api_v1_face_data_flowback_query,
                            headers=self.get_headers("/api/v1/face/data/flowback-query"),
                            json=body,
                            verify=False)
        res.close()
        return res

    def api_face_security_manual_optcheck(self,
                                          reqId=get_uuid(),
                                          gateNo="",
                                          deviceId="",
                                          cardType="",
                                          idCard="",
                                          nameZh="",
                                          nameEn="",
                                          age="",
                                          sex="",
                                          birthDate="",
                                          address="重庆市",
                                          certificateValidity="20120101-长期",
                                          nationality="China",
                                          ethnic="汉族",
                                          contactWay="0123456789",
                                          scenePhoto="",
                                          sceneFeature="",
                                          cardPhoto="",
                                          cardFeature=""):
        """2.3.17安检口人工放行接口（二期）"""
        body = {"reqId": reqId,
                "gateNo": gateNo,
                "deviceId": deviceId,
                "cardType": cardType,
                "idCard": idCard,
                "nameZh": nameZh,
                "nameEn": nameEn,
                "age": age,
                "sex": sex,
                "birthDate": birthDate,
                "address": address,
                "certificateValidity": certificateValidity,
                "nationality": nationality,
                "ethnic": ethnic,
                "contactWay": contactWay,
                "scenePhoto": scenePhoto,
                "sceneFeature": sceneFeature,
                "cardPhoto": cardPhoto,
                "cardFeature": cardFeature}
        res = requests.post(url=self.api_v1_face_security_manual_optcheck,
                            headers=self.get_headers("/api/v1/face/security/manual-optcheck"),
                            json=body,
                            verify=False)
        res.close()
        return res


if __name__ == '__main__':
    #
    # res = AirportProcess().api_security_ticket_check(
    #                               reqId=get_uuid(),
    #                               gateNo="T1AJ",
    #                               deviceId="T1AJ001",
    #                               cardType="0",
    #                               idCard="002228199312134390",
    #                               nameZh="nameZh",
    #                               nameEn="nameEn",
    #                               age=get_age("002228199312134390"),
    #                               sex=1,
    #                               birthDate=get_birthday("002228199312134390"),
    #                               address="重庆市",
    #                               certificateValidity="20120101-20230202",
    #                               nationality="China",
    #                               ethnic="汉族",
    #                               contactWay="0123456789",
    #                               cardPhoto=Base64Picture,
    #                               fId=get_uuid()
    #                               )
    # print(res.text)
    #
    # res = AirportProcess().api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ1",
    #                                  deviceId="T1AJ001",
    #                                  cardType="0",
    #                                  idCard="002228199312134390",
    #                                  nameZh="nameZh",
    #                                  nameEn="nameEn",
    #                                  age=get_age("002228199312134390"),
    #                                  sex="1",
    #                                  birthDate=get_birthday("002228199312134390"),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(testlive8k_features+"/2.txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(testcard8k_features+"/2.txt"))
    #
    # print(res.text)
    #
    # time.sleep(1)
    #
    # res1 = AirportProcess().api_face_review_self_check(reqid=get_uuid(),
    #                                gateno="T1AF1",
    #                                deviceid="T1AF001",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(testlive2k_features+"/2.txt"))
    #
    # print(res1.text)


    # 进行人证1：1黑名单
    res = AirportProcess().api_anjian(anjiangateNo="T1AJ1",
                     anjiandeviceId="T1AJ001",
                     cardType=0,
                     idCard="003228199312134390",
                     nameZh="bukong3",
                     nameEn="CHENKEYUN",
                     age=25,
                     sex=1,
                     birthDate=get_birthday("003228199312134390"),
                     address="重庆市大竹林街道",
                     nationality="中国",
                     ethnic="汉族",
                     scenePhoto=Base64Picture,
                     sceneFeature=get_txt(testlive8k_features+"/3.txt"),
                     cardPhoto=Base64Picture,
                     cardFeature=get_txt(testlive8k_features+"/3.txt"))
    print(res.text)
    # idcard_list = get_id_re_match()
    # print(idcard_list)
    # for i in range(0, 20):
    #     res = AirportProcess().api_security_ticket_check(reqId=get_uuid(),
    #                               gateNo="T1AJ2",
    #                               deviceId="T1AJ002",
    #                               cardType="0",
    #                               idCard=idcard_list[i],
    #                               nameZh="nameZh",
    #                               nameEn="nameEn",
    #                               age=get_age(idcard_list[i]),
    #                               sex=1,
    #                               birthDate=get_birthday(idcard_list[i]),
    #                               address="重庆市",
    #                               certificateValidity="20120101-20230202",
    #                               nationality="CHina",
    #                               ethnic="汉族",
    #                               contactWay="0123456789",
    #                               cardPhoto=Base64Picture,
    #                               fId=get_uuid())
    #     print(res.text)
    #     time.sleep(1)
    #     res1 = AirportProcess().api_face_security_face_check(reqId=get_uuid(),
    #                                  gateNo="T1AJ2",
    #                                  deviceId="T1AJ002",
    #                                  cardType="0",
    #                                  idCard=idcard_list[i],
    #                                  nameZh="nameZh",
    #                                  nameEn="nameEn",
    #                                  age=get_age(idcard_list[i]),
    #                                  sex="1",
    #                                  birthDate=get_birthday(idcard_list[i]),
    #                                  address="重庆市",
    #                                  certificateValidity="20180101-20260203",
    #                                  nationality="China",
    #                                  ethnic="汉族",
    #                                  contactWay="0123456789",
    #                                  scenePhoto=Base64Picture,
    #                                  sceneFeature=get_txt(shiwanli8k_features+"/"+str(i+6000)+".txt"),
    #                                  cardPhoto=Base64Picture,
    #                                  cardFeature=get_txt(shiwanid8k_features+"/"+str(i+6000)+".txt"))
    #     print(res1.text)
    #     print("第%d次完成"%(i+1))
    #     time.sleep(6)
    #
    #
    #     res2 = AirportProcess().api_face_review_self_check(
    #         reqid=get_uuid(),
    #                                gateno="T1AF2",
    #                                deviceid="T1AF002",
    #                                scenephoto=Base64Picture,
    #                                scenefeature=get_txt(shiwanli2k_features+"/"+str(i+6000)+".txt")
    #     )
    #     print(res2.text)
    #     print("第%d次完成" % (i+1))
    #     time.sleep(1)
    #
    #
    #     card = "500101199208130420"
    #     res = AirportProcess(host="http://192.168.10.194:16000/").api_face_data_flowback_query(
    #                                  reqId=get_uuid(),
    #                                  cardId=card,
    #                                  flightNo="",
    #                                  flightDay=produce_flight_day(),
    #                                  boardingNumber="001")
    #     json_data = json.loads(res.text)
    #     print(json_data)