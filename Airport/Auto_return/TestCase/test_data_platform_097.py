# coding:utf-8
import unittest
import json
from Airport.数据平台接口.数据分析.A_097安检通道旅客性别人数分布查询 import *


class TestApiAnalysisChannelSexRate(unittest.TestCase):
    """2.4.9.7旅客性别人数分布"""

    def test_01(self):
        """验证正确传入参数时能返回旅客年性别数分布数据"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atAJ-D",  # 通道编号(区域表里面的编号)
            "startTime": "2018101800000000",
            "endTime": "2018102300000000"
        }
        a = api_v1_analysis_channel_sexrate(body1)
        dict_data = json.loads(a)
        self.assertNotEqual(dict_data["results"][0]["value"], 0)

    def test_02(self):
        """验证查询非有效时间内不能查询到旅客性别人数分布数据"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atAJ-D",  # 通道编号(区域表里面的编号)
            "startTime": "2018091800000000",
            "endTime": "2018092300000000"
        }
        a = api_v1_analysis_channel_sexrate(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["results"][1]["value"], 0)

    def test_03(self):
        """验证区域通道不存在时，不能查到旅客性别人数分布数据"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atAJ-00",  # 通道编号(区域表里面的编号)
            "startTime": "2018101800000000",
            "endTime": "2018102300000000"
        }
        a = api_v1_analysis_channel_sexrate(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["results"][1]["value"], 0)

    def test_04(self):
        """验证reqId为空值时服务器的响应"""
        body1 = {
            "reqId": "",
            "areaCode": "atAJ-D",  # 通道编号(区域表里面的编号)
            "startTime": "2018101800000000",
            "endTime": "2018102300000000"
        }
        a = api_v1_analysis_channel_sexrate(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["msg"], "reqId is empty")

    def test_05(self):
        """验证areaCode为空时，服务器能正确响应"""
        body1 = {
            "reqId": get_uuid(),
            # "areaCode": "atAJ-D",  # 通道编号(区域表里面的编号)
            "startTime": "2018101800000000",
            "endTime": "2018102300000000"
        }
        a = api_v1_analysis_channel_sexrate(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["msg"], "areaCode is empty")

    def test_06(self):
        """验证startTime大于endTime相等时，服务器能正确响应"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atAJ-D",  # 通道编号(区域表里面的编号)
            "startTime": "2018101800000000",
            "endTime": "2018101700000000"
        }
        a = api_v1_analysis_channel_sexrate(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["msg"], "query error: startTime > endTime")

    def test_07(self):
        """验证服务器响应时间小于1s"""
        start = time.clock()
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atAJ-B",  # 通道编号(区域表里面的编号)
            "startTime": "20181010" + "06000000",
            "endTime": "20181023" + "06000000"
        }
        a = api_v1_analysis_channel_sexrate(body1)
        end = time.clock()
        print("服务器响应时间为:%fs" % (end - start))
        self.assertLessEqual(end - start, 1)

if __name__ == '__main__':
    unittest.main()