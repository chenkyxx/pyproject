# coding:utf-8
import unittest
import json
from Airport.new_method_1 import *
from Airport.数据平台接口.数据分析.A_083预安检区域通过人数接口 import *


class TestApiAnalysisPreSecurityPassNum(unittest.TestCase):
    """2.4.8.3预安检区域通过人数接口"""
    # 更改接口后，

    def test_01(self):
        """能够正确查询出预安检区域通过人数"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atYA-B",  # 通道编号(区域表里面的编号)
            "startTime": "20181010"+"06000000",
            "endTime": "20181023"+"06000000"
        }
        a = api_v1_analysis_pre_security_passnum(body1)
        dict_data = json.loads(a)
        self.assertLessEqual(1000, dict_data["results"][1]["num"])

    def test_02(self):
        """不在时间段内时候不能查到相关信息"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atYA-B",  # 通道编号(区域表里面的编号)
            "startTime": "20180705" + "06000000",
            "endTime": "20180706" + "06000000",
        }
        a = api_v1_analysis_pre_security_passnum(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["results"][0]["num"], 0)

    def test_03(self):
        """区域通道不存在时，不能查到相关信息"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atYA-M",  # 通道编号(区域表里面的编号)
            "startTime": delete_str(get_today_month(-1)) + "06000000",
            "endTime": datetimestr()[0:8]+"06000000"
        }
        a = api_v1_analysis_pre_security_passnum(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["results"][0]["num"], 0)

    def test_04(self):
        """验证开始时间大于结束时间时，能正确响应"""
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atYA-M",  # 通道编号(区域表里面的编号)
            "startTime": "20181121" + "06000000",
            "endTime": "20181001" + "06000000",
        }
        a = api_v1_analysis_pre_security_passnum(body1)
        dict_data = json.loads(a)
        self.assertEqual(dict_data["msg"], "query error: startTime > endTime")

    def test_05(self):
        """验证服务器响应时间小于1s"""
        start = time.clock()
        body1 = {
            "reqId": get_uuid(),
            "areaCode": "atYA-B",  # 通道编号(区域表里面的编号)
            "startTime": "20181010" + "06000000",
            "endTime": "20181023" + "06000000"
        }
        a = api_v1_analysis_pre_security_passnum(body1)
        end = time.clock()
        print("响应时间为%fs" % (end-start))
        self.assertLessEqual(end-start,1)

if __name__ == '__main__':
    unittest.main()
