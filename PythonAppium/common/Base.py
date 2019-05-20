# coding:utf-8
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import re


class Base(object):
    """对appium的方法进行封装"""
    url = "http://127.0.0.1:4723/wd/hub"
    cap = {"platformName": "Android",
           "deviceName": "127.0.0.1:5555",
           "platformVersion": "5.1.1",
           "appPackage": "com.xiaomi.shop",
           "appActivity": "com.xiaomi.shop.activity.MainTabActivity"}

    def __init__(self):
        self.driver = webdriver.Remote(command_executor=self.url, desired_capabilities=self.cap)
        self.timeout = 10
        self.t = 0.5

    def find_element(self, locator):
        """通过定位方式找到元素"""
        if isinstance(locator, str):
            try:
                print()
                ele1 = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x:x.find)
                ele = self.driver.find_element_by_android_uiautomator(locator)
                return ele
            except Exception as e:
                print("元素定位异常：%s"+str(e))
        else:
            print("输入元素类型错误")


if __name__ == '__main__':
    aa = "Test(sddd)"
    b = re.match(".*(\()", aa)
    print(b[0])