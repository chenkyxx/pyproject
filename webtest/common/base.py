# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.time = 0.5

    def SendKeys(self, locator, text):
        ele = self.FindElement(locator)
        ele.send_keys(text)

    def Click(self,locator):
        ele = self.FindElement(locator)
        ele.click()

    def Clear(self,locator):
        ele = self.FindElement(locator)
        ele.clear()

    def IsElementSelect(self,locator):
        ele = self.FindElement(locator)
        r = ele.is_select()
        return r

    def IsElementExist(self,locator):
        try:
            self.FindElement(locator)
            return True
        except:
            return False

if __name__ == "__main__":
    locator_user = ("id", "account")
    locator_psw = ("name", "password")
    locator_login = ("id", "submit")
    url = "http://127.0.0.1/zentao/user-login.html"
    driver = webdriver.Firefox()
    driver.get(url)
    a = Base(driver)
    a.SendKeys(locator_user,"admin")
    a.SendKeys(locator_psw,"123456")
    a.Click(locator_login)
    time.sleep(5)
    driver.quit()




