# coding:utf-8
import unittest
import json
from Airport.数据平台接口.数据分析.A_081预安检通道基础流量查询布询接口 import *
from Airport.数据平台接口.数据分析.A_083预安检区域通过人数接口 import *


class TestApiAnalysisPreSecurityEfficiency(unittest.TestCase):
    """
    数据平台预安检通道基础流量查询接口回归测试
    """
    def test_01(self):
        """ 正常查询通道基础流量查询"""
        body_1 = {
            "reqId": "a",
            "areaCode": "T1YA",  # 通道编号(区域表里面的编号)
            "startTime": "20180922"+"06000000",
            "endTime": "20181022"+"06000000"
        }
        a1 = api_v1_analysis_pre_security_efficiency(body_1)
        dict_data = json.loads(a1)
        self.assertEqual(None, (dict_data["result"]))

    def test_02(self):
        """
        旅客数据不在时间段内不能查询到相关数据
        :return:
        """
        body_2 = {
            "reqId": "a",
            "areaCode": "T1YA",  # 通道编号(区域表里面的编号)
            "startTime": "2018082310000000",
            "endTime": "2018092311000000"
        }
        a2 = api_v1_analysis_pre_security_efficiency(body_2)
        dict_data = json.loads(a2)
        self.assertEqual(dict_data["result"], None)

    def test_03(self):
        """
        通道信息不存在时，不能查到信息
        :return:
        """
        body_3 = {
            "reqId": "a",
            "areaCode": "aaa",  # 通道编号(区域表里面的编号)
            "startTime": "2018092310000000",
            "endTime": "2018092311000000"
        }
        a3 = api_v1_analysis_pre_security_efficiency(body_3)
        dict_data = json.loads(a3)
        self.assertEqual(dict_data["result"], None)

    def test_04(self):
        """
        验证时间区间错误时 开始大于结束时间
        :return:
        """
        body_4 = {
            "reqId": "11",
            "areaCode": "T1YA",  # 通道编号(区域表里面的编号)
            "startTime": "2018102310000000",
            "endTime": "2018092311000000"
        }
        a4 = api_v1_analysis_pre_security_efficiency(body_4)
        dict_data = json.loads(a4)
        self.assertEqual(dict_data["result"], None)

    def test_05(self):
        """
        验证reqId为空时服务器能正确响应
        :return:
        """
        body_5 = {
            "reqId": None,
            "areaCode": "atYA-A",  # 通道编号(区域表里面的编号)
            "startTime": "2018102310000000",
            "endTime": "2018092311000000"
        }
        a5 = api_v1_analysis_pre_security_efficiency(body_5)
        dict_data = json.loads(a5)
        self.assertEqual(dict_data["msg"], "reqId is empty")

    def test_06(self):
        """验证服务器响应时间小于1s"""
        start = time.clock()
        body_1 = {
            "reqId": "a",
            "areaCode": "atYA-A",  # 通道编号(区域表里面的编号)
            "startTime": "20180922" + "06000000",
            "endTime": "20181022" + "06000000"
        }
        a1 = api_v1_analysis_pre_security_efficiency(body_1)
        end = time.clock()
        line = end-start
        self.assertLessEqual(line, 0.5)

if __name__ == '__main__':
    unittest.main()