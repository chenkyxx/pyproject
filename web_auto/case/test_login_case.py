from selenium import webdriver
import unittest
from pages.login_page import LoginPage, login_url
'''
1. 输入admin, 输入123456 点登陆  期望结果：用眼睛去看？？？
2. 输入admin, 输入   点登陆
3. 输入admin, 输入123456， 点记住登陆按钮   点登陆
4. 点忘记密码

'''


class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies() # 退出登录
        self.driver.refresh()

    def test_01(self):
        '''输入账号admin, 输入密码123456 点登陆'''
        self.loginp.input_user("admin")
        self.loginp.input_psw("123456")
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == "admin")
        # 断言

    def test_02(self):
        '''输入admin, 输入   点登陆'''
        self.loginp.input_user("admin")
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == "")
        # 断言

    def test_03(self):
        '''输入admin, 输入123456， 点记住登陆按钮   点登陆'''
        self.loginp.input_user("admin")
        self.loginp.input_psw("123456")
        self.loginp.click_keep_login()
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        self.assertTrue(result == "admin")

    def test_04(self):
        '''忘记密码'''
        self.loginp.click_forget_psw()
        result = self.loginp.is_refresh_exist()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()




