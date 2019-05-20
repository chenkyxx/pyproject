# coding:utf-8
import unittest
import json
from Airport.数据平台接口.数据分析.A_091安检通道基础流量查询 import *


class TestApiAnalysisChannelEfficiency(unittest.TestCase):
    """2.4.9.1安检通道基础流量查询"""

    def test_01(self):
        """验证正确传入参数时能返回安检通道基础流量数据"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "T1AJ",  # 通道编号(区域表里面的编号)
            "startTime": "20181010"+"06000000",
            "endTime": "20181023"+"06000000"
        }
        a = api_v1_analysis_channel_efficiency(body1)
        dict_data = json.loads(a)
        self.assertEqual(None, dict_data["result"])

    def test_02(self):
        """验证查询非有效时间内不能查询到安检通道基础流量数据"""
        # 不做时间参数传入
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "T1AJ",  # 通道编号(区域表里面的编号)
            "startTime": "2018092310000000",
            "endTime": "2018092311000000"
        }
        a = api_v1_analysis_channel_efficiency(body1)
        dict_data = json.loads(a)
        self.assertEqual(None, dict_data["result"])

    def test_03(self):
        """验证区域通道不存在时，不能查到安检通道基础流量数据"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atAJ-M",  # 通道编号(区域表里面的编号)
            "startTime": "20181010"+"06000000",
            "endTime": "20181023"+"06000000"
        }
        a = api_v1_analysis_channel_efficiency(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["result"],None )

    def test_04(self):
        """验证startTime大于endTime相等时，服务器能正确响应"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "T1AJ",  # 通道编号(区域表里面的编号)
            "startTime": "2019010100000000",
            "endTime": "2018010100000000",
        }
        a = api_v1_analysis_channel_efficiency(body1)
        dict_data = json.loads(a)
        self.assertEqual(None,dict_data["result"])

    def test_05(self):
        """验证服务器响应时间小于1s"""
        start = time.clock()
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atAJ-B",  # 通道编号(区域表里面的编号)
            "startTime": "20181010" + "06000000",
            "endTime": "20181023" + "06000000"
        }
        a = api_v1_analysis_channel_efficiency(body1)
        end = time.clock()
        print("服务器响应时间为:%fs" % (end-start))
        self.assertLessEqual(end-start, 1)


if __name__ == '__main__':
    unittest.main()
