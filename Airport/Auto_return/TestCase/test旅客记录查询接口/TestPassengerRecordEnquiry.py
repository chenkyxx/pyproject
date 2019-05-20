# coding:utf-8
import unittest
from Airport.数据平台接口.数据分析.A_01预安检旅客查询接口 import *
from Airport.数据平台接口.数据分析.A_02安检口旅客记录查询接口 import *
from Airport.数据平台接口.数据分析.A_03复核口旅客记录查询接口 import *
from Airport.数据平台接口.数据分析.A_04旅客值机记录查询接口 import *
from Airport.数据平台接口.数据分析.A_05旅客安检记录查询接口 import *


class TestPassengerRecordEnquiry(unittest.TestCase):
    """旅客记录（预安检，安检，复核，值机，安检）查询接口,响应时间"""

    def test_01_yu_an(self):
        """30000，40预安检旅客查询时间响应小于1s"""
        start1 = time.clock()
        body1 = {
            "reqId": get_uuid(),
            # "name": "",
            # "englishName": "",
            # "cardType": "",
            # "idCard": "",
            # "sex": "",
            # "areaCode": "",
            # "matchResult": "",
            "startTime": "2018070109123200",
            "endTime": "2018120109123200",
            "page": "30000",  # int
            "pageSize": "40",
            "isCount": "1"}
        a = api_v1_face_pre_security_query(body1)
        end1 = time.clock()
        print("服务器响应时间为:%fs" % (end1 - start1))
        self.assertLessEqual(end1 - start1, 1)

    def test_02_yu_an(self):
        """30000，30预安检旅客查询时间响应小于1s"""
        start1 = time.clock()
        body1 = {
            "reqId": get_uuid(),
            # "name": "",
            # "englishName": "",
            # "cardType": "",
            # "idCard": "",
            # "sex": "",
            # "areaCode": "",
            # "matchResult": "",
            "startTime": "2018070109123200",
            "endTime": "2018120109123200",
            "page": "30000",  # int
            "pageSize": "30",
            "isCount": "1"}
        a = api_v1_face_pre_security_query(body1)
        end1 = time.clock()
        print("服务器响应时间为:%fs" % (end1 - start1))
        self.assertLessEqual(end1 - start1, 1)

    def test_01_an_ji(self):
        """28000,40安检口旅客记录查询"""
        start1 = time.clock()
        body1 = {
            "reqId": get_uuid(),
            # "name": "冯娘",
            # "englishName": "yyy",
            # "cardType": "",
            # "idCard": "500238199312134390",
            # "sex": "0",
            # "areaCode": "atAJ-C",
            # "matchResult": "2",
            "startTime": "2018070109123200",
            "endTime": "2018120109123200",
            "page": "28000",  # int
            "pageSize": "40",
            "isCount": "1"}
        a = api_v1_face_security_query(body1)
        end1 = time.clock()
        print("服务器响应时间为:%fs" % (end1 - start1))
        self.assertLessEqual(end1 - start1, 1)

    def test_02_an_ji(self):
        """28000,30安检口旅客记录查询"""
        start1 = time.clock()
        body1 = {
            "reqId": get_uuid(),
            # "name": "冯娘",
            # "englishName": "yyy",
            # "cardType": "",
            # "idCard": "500238199312134390",
            # "sex": "0",
            # "areaCode": "atAJ-C",
            # "matchResult": "2",
            "startTime": "2018070109123200",
            "endTime": "2018120109123200",
            "page": "28000",  # int
            "pageSize": "30",
            "isCount": "1"}
        a = api_v1_face_security_query(body1)
        end1 = time.clock()
        print("服务器响应时间为:%fs" % (end1 - start1))
        self.assertLessEqual(end1 - start1, 1)

    def test_01_fu_he(self):
        """30000,40复核口旅客记录查询"""
        start1 = time.clock()
        body1 = {
            "reqId": get_uuid(),
            # "name": "",
            # "englistName": "",
            # "cardType": "",
            # "idCard": "",
            # "sex": "",
            # "areaCode": "",
            # "matchResult": "",
            "startTime": "20180701091232",
            "endTime": "20181201091232",
            "page": "30000",  # int
            "pageSize": "40",
            "isCount": "1"
        }
        api_v1_face_review_query(body1)
        end1 = time.clock()
        print("服务器响应时间为:%fs" % (end1 - start1))
        self.assertLessEqual(end1 - start1, 1)

    def test_02_fu_he(self):
        """30000,30复核口旅客记录查询"""
        start1 = time.clock()
        body1 = {
            "reqId": get_uuid(),
            # "name": "",
            # "englistName": "",
            # "cardType": "",
            # "idCard": "",
            # "sex": "",
            # "areaCode": "",
            # "matchResult": "",
            "startTime": "20180701091232",
            "endTime": "20181201091232",
            "page": "30000",  # int
            "pageSize": "30",
            "isCount": "1"
        }
        api_v1_face_review_query(body1)
        end1 = time.clock()
        print("服务器响应时间为:%fs" % (end1 - start1))
        self.assertLessEqual(end1 - start1, 1)

    def test_01_zhi_ji(self):
        """80000,40旅客值机记录查询"""
        start1 = time.clock()
        body1 = {
            "reqId": get_uuid(),
            # "name": "",
            # "englistName": "",
            # "nationality": "",
            # "cardType": "",
            # "idCard": "",
            # "startBirthYear": "1993",
            # "endBirthYear": "1993",
            "startTime": "20180701091232",
            "endTime": "20181201091232",
            "page": "80000",  # int
            "pageSize": "40",
            "isCount": "1"
        }
        api_v1_face_checkin_query(body1)
        end1 = time.clock()
        print("服务器响应时间为:%fs" % (end1 - start1))
        self.assertLessEqual(end1 - start1, 1)

    def test_02_zhi_ji(self):
        """80000,30旅客值机记录查询"""
        start1 = time.clock()
        body1 = {
            "reqId": get_uuid(),
            # "name": "",
            # "englistName": "",
            # "nationality": "",
            # "cardType": "",
            # "idCard": "",
            # "startBirthYear": "1993",
            # "endBirthYear": "1993",
            "startTime": "20180701091232",
            "endTime": "20181201091232",
            "page": "80000",  # int
            "pageSize": "30",
            "isCount": "1"
        }
        api_v1_face_checkin_query(body1)
        end1 = time.clock()
        print("服务器响应时间为:%fs" % (end1 - start1))
        self.assertLessEqual(end1 - start1, 1)

    def test_03_zhi_ji(self):
        """80000,20旅客值机记录查询"""
        start1 = time.clock()
        body1 = {
            "reqId": get_uuid(),
            # "name": "",
            # "englistName": "",
            # "nationality": "",
            # "cardType": "",
            # "idCard": "",
            # "startBirthYear": "1993",
            # "endBirthYear": "1993",
            "startTime": "20180701091232",
            "endTime": "20181201091232",
            "page": "80000",  # int
            "pageSize": "20",
            "isCount": "1"
        }
        api_v1_face_checkin_query(body1)
        end1 = time.clock()
        print("服务器响应时间为:%fs" % (end1 - start1))
        self.assertLessEqual(end1 - start1, 1)

    def test_01_lk_an_ji_record(self):
        """28000,40旅客值机记录查询"""
        start1 = time.clock()
        body1 = {
            "reqId": get_uuid(),
            # "name": "12323",
            # "cardType": "0",
            # "idCard": "500238199312134390",
            "startTime": "20180701091232",
            "endTime": "20181201091232",
            "page": "28000",  # int
            "pageSize": "40",
            "isCount": "1"}
        api_v1_face_security_record(body1)
        end1 = time.clock()
        print("服务器响应时间为:%fs" % (end1 - start1))
        self.assertLessEqual(end1 - start1, 1)

    def test_02_lk_an_ji_record(self):
        """28000,30旅客值机记录查询"""
        start1 = time.clock()
        body1 = {
            "reqId": get_uuid(),
            # "name": "12323",
            # "cardType": "0",
            # "idCard": "500238199312134390",
            "startTime": "20180701091232",
            "endTime": "20181201091232",
            "page": "28000",  # int
            "pageSize": "30",
            "isCount": "1"}
        api_v1_face_security_record(body1)
        end1 = time.clock()
        print("服务器响应时间为:%fs" % (end1 - start1))
        self.assertLessEqual(end1 - start1, 1)

if __name__ == '__main__':
    unittest.main()