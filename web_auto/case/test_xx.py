from selenium import webdriver
import unittest
from pages.login_page import LoginPage, login_url
import ddt
from common.read_excel import ExcelUtil
import os
'''
1. 输入admin, 输入123456 点登陆  期望结果：用眼睛去看？？？
2. 输入admin, 输入   点登陆
3. 输入admin1111, 输入123456，   点登陆
'''

# 测试的数据
testdates = [
    {"user": "admin", "psw": "123456", "expect": True},
    {"user": "admin", "psw": "", "expect": False},
    {"user": "admin1111", "psw": "123456", "expect": False},
           ]

# propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# filepath = os.path.join(propath, "common", "datas.xlsx")
# print(filepath)
#
# data = ExcelUtil(filepath)
# testdates = data.dict_data()
# print(testdates)

@ddt.ddt
class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)
        cls.driver.get(login_url)

    def setUp(self):
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()   # 退出登录
        self.driver.refresh()
        self.driver.get(login_url)

    def login_case(self, user, psw, expect):
        self.loginp.login(user, psw)
        # self.loginp.input_user(user)
        # self.loginp.input_psw(psw)
        # self.loginp.click_login_button()
        result = self.loginp.get_login_result(user)
        print("测试结果：%s" % result)
        self.assertTrue(result == expect)

    @ddt.data(*testdates)
    def test_01(self, data):
        '''输入账号admin, 输入密码123456 点登陆'''
        print("---------------开始测试 --------")
        print("测试数据:%s" % data)
        self.login_case(data["user"], data["psw"], data["expect"])
        print("--------------结束：pass! --------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()




