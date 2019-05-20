# coding:utf-8
from selenium import webdriver
from common.base import Base
import time
"""
以page ogject的设计模式，根据页面的不同，分层设计
有利于自动化脚本的维护
"""
url = "http://localhost/zentao/www/user-login"


class PageLogin(Base):

    # 登陆页面需要用到的元素定位
    locator_user = ("id", "account")
    locator_psw = ("name", "password")
    locator_login = ("id", "submit")
    locator_keep_login = ("id", "keepLoginon")
    locator_forget_psw = ("link text", "忘记密码")
    locator_mobile = ("id", "mobile")
    locator_get_user = ("css selector", "#userMenu>a")

    def input_user(self,text=""):
        """添加用户名"""
        self.SendKeys(self.locator_user,text)

    def input_psw(self,text=""):
        """"输入密码"""
        self.SendKeys(self.locator_psw, text)

    def click_keep_login(self):
        """点击保持登陆"""
        self.Click(self.locator_keep_login)

    def click_login(self):
        """点击登陆按钮"""
        self.Click(self.locator_login)

    def click_forget_psw(self):
        """点击忘记密码"""
        self.Click(self.locator_forget_psw)

    def get_login_user(self):
        """获取登陆后的用户名"""
        try:
            user = self.FindElement(self.locator_get_user).text
            return user
        except:
            return ""

if __name__=="__main__":
    driver = webdriver.Firefox()
    login = PageLogin(driver)
    driver.get(url)
    login.input_user("admin")
    login.input_psw("123456")
    login.click_login()
    time.sleep(5)
    user = login.get_login_user()
    try:
        assert user=="2去admin"
    except:
        print("不一致")

    driver.quit()






