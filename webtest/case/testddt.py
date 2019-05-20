# coding:utf-8
import unittest
import ddt
data1 =[{"user":"admin","psw":"123456","desc":"密码正确得情况"},
       {"user":"admin1","psw":"123456","desc":"密码bu正确得情况"},
       {"user":"admin1","psw":"1234567","desc":"密码都正确得情况"}]


@ddt.ddt
class DdtTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("所有用例执行之前执行一次")

    @classmethod
    def tearDownClass(cls):
        print("所有用例执行结束之后执行一次")

    def setUp(self):
        print("每个用例执行之前都要执行")

    def tearDown(self):
        print("每个用例执行之后都要执行一次\n")



    @ddt.data(*data1)
    def test_01(self,mm):
        print(mm["user"]+"\t"+mm["psw"]+mm["desc"])

    def test_02(self):
        print("")

if __name__ == "__main__":
    unittest.main()




