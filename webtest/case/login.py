# coding:utf-8
from selenium import webdriver
import unittest
import time
import ddt

from webtest.page.page_login import PageLogin

data = [{"user": "admin", "psw": "123456"},
        {"user": "admin1", "psw": "123456"},
        {"user": "admin1", "psw": "1234567"}]


@ddt.ddt
class Test_login(unittest.TestCase):
    """登陆模块"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login = PageLogin(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://localhost/zentao/www/user-login")
        self.driver.delete_all_cookies()  # 退出登陆
        self.driver.refresh()
        print("--------------------")

    # def login_liucheng(self,user,pws):
    #     self.login.input_user(user)
    #     self.login.input_psw(pws)
    #     m = self.is_alert_exist()

    def is_alert_exist(self):
        """判断alert是不是在"""
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()  # 用alert 点alert
            return text
        except:
            return ""

    def test_01(self):
        """正确登陆测试用例"""
        self.login.input_user("admin")
        self.login.input_psw("123456")
        self.login.click_login()
        time.sleep(2)
        user = self.login.get_login_user()
        self.assertEqual(user, "admin")

    def test_02(self):
        """密码错误时的用例"""
        self.login.input_user("admin")
        self.login.input_psw("12345")
        self.login.click_login()
        time.sleep(2)
        user = self.login.get_login_user()
        self.assertNotEqual(user, "admin")

    def test_03(self):
        """密码为空的情况"""
        self.login.input_user("admin")
        self.login.input_psw("")
        self.login.click_login()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        self.assertEqual(text, "登陆")


if __name__ == "__main__":
    unittest.main()

