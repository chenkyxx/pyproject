# coding:utf-8
import unittest
import json
from Airport.数据平台接口.数据分析.A_082预安检区域通过率接口 import *
from Airport.new_method_1 import *


class TestApiAnalysisPreSecurityPassRate(unittest.TestCase):
    """预安检通过率接口测试回归"""
    def test_01(self):
        """查询通过率"""
        body_1 = {
            "reqId": "32位UUID",
            "areaCode": "atYA-A",  # 通道编号(区域表里面的编号)
            "startTime": "20181010"+"06000000",
            "endTime": "20181023"+"06000000"
        }
        a = api_v1_analysis_pre_security_passrate(body_1)
        dict_data = json.loads(a)
        self.assertNotEqual(dict_data["results"][0]["num"], 0)

    def test_02(self):
        """不在当前时间不能查出来"""
        body_1 = {
            "reqId": "32位UUID",
            "areaCode": "atYA-A",  # 通道编号(区域表里面的编号)
            "startTime": "2018092308000000",
            "endTime": "2018092408000000"
        }
        a = api_v1_analysis_pre_security_passrate(body_1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["results"][0]["num"], 0)

    def test_03(self):
        """区域通道不存在时不能查询相关信息"""
        body_1 = {
            "reqId": "32位UUID",
            "areaCode": "atYA-M",  # 通道编号(区域表里面的编号)
            "startTime": "2018092308000000",
            "endTime": "2018102308000000"
        }
        a = api_v1_analysis_pre_security_passrate(body_1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["results"][0]["num"], 0)

    def test_04(self):
        """验证服务器响应时间小于1S"""
        start = time.clock()
        body_1 = {
            "reqId": "32位UUID",
            "areaCode": "atYA-A",  # 通道编号(区域表里面的编号)
            "startTime": "20181010" + "06000000",
            "endTime": "20181023" + "06000000"
        }
        a = api_v1_analysis_pre_security_passrate(body_1)
        end = time.clock()
        line = end-start
        print("响应时间为%fs" % line)
        self.assertLessEqual(line, 1)

if __name__ == '__main__':
    unittest.main()


