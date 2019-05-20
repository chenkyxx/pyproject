# coding:utf-8
import unittest
import json
from Airport.数据平台接口.数据分析.A_093安检通道复核口人数峰值分析查询 import *


class TestApiAnalysisChannelReviewPeak(unittest.TestCase):
    """2.4.9.3复核口人数峰值分析"""

    def test_01(self):
        """验证正确传入参数时能返回复核口人数峰值数据"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atAF-A",  # 通道编号(区域表里面的编号)
            "startTime": "20181010"+"00000000",
            "endTime": "20181023"+"00000000"
        }
        a = api_v1_analysis_channel_review_peak(body1)
        dict_data = json.loads(a)
        self.assertNotEqual(dict_data["results"][0]["num"], 0)

    def test_02(self):
        """验证查询非有效时间内不能查询到复核口人数峰值数据"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atAF-A",  # 通道编号(区域表里面的编号)
            "startTime": "2017071100000000",
            "endTime": "2018071100000000"
        }
        a = api_v1_analysis_channel_review_peak(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["results"][0]["num"], 0)

    def test_03(self):
        """验证区域通道不存在时，不能查到复核口人数峰值数据"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atAF-11111111",  # 通道编号(区域表里面的编号)
            "startTime": "20181015" + "00000000",
            "endTime": "20181018" + "00000000"
        }
        a = api_v1_analysis_channel_review_peak(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["results"][random.randint(0, 2)]["num"], 0)

    def test_04(self):
        """reqId为空时候服务能正确响应"""
        body1 = {
            "reqId": None,
            "areaCode": "atAF-11111111",  # 通道编号(区域表里面的编号)
            "startTime": "20181015" + "00000000",
            "endTime": "20181018" + "00000000"
        }
        a = api_v1_analysis_channel_review_peak(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["msg"], "reqId is empty")

    def test_05(self):
        """验证服务响应时间小于1s"""
        start = time.clock()
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atAF-A",  # 通道编号(区域表里面的编号)
            "startTime": "20181010" + "06000000",
            "endTime": "20181023" + "06000000"
        }
        a = api_v1_analysis_channel_review_peak(body1)
        end = time.clock()
        print("服务器响应时间为:%fs" % (end - start))
        self.assertLessEqual(end - start, 1)


if __name__ == '__main__':
    unittest.main()

