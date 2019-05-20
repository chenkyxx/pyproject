# coding:utf-8
import time
from appium import webdriver


def _main():
    print(str(round(time.time()*1000)))
    url = "http://127.0.0.1:4723/wd/hub"
    cap = {"platformName": "Android",
           "deviceName": "127.0.0.1:5555",
           "platformVersion": "5.1.1",
           "appPackage": "com.xiaomi.shop",
           "appActivity": "com.xiaomi.shop.activity.MainTabActivity"}
    driver = webdriver.Remote(command_executor=url, desired_capabilities=cap)
    print(str(round(time.time()*1000)))
    driver.quit()

if __name__ == '__main__':
    _main()