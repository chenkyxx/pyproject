# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 22:05
# @Author  : chenky
# @Email   : 842202171@qq.com
# @File    : 5课 元素定位.py
# @Software: PyCharm
# @Project : pyproject

from appium import webdriver
import time

# Appium默认每次都会清空app的缓存数据，加个noReset参数

desired_caps = {"platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "5.1.1",
                "noReset": True,
                "unicodeKeyboard": True,  # 使用unicode编码方式发送字符串
                "resetKeyboard": True,  # 隐藏键盘
                "appPackage": "com.taobao.taobao",
                "appActivity": "com.taobao.tao.welcome.Welcome"}
driver = webdriver.Remote(desired_capabilities=desired_caps,
                          command_executor="http://127.0.0.1:4723/wd/hub")

# 1.xpath 定位text语法
# driver.find_element_by_xpath("//*[@text='同意']").click()

# 2.xpath 定位text高级语法
driver.find_element_by_xpath("//*[contains(@text,'同意')]").click()

# 3.content-desc属性用by_accessibility_id定位
time.sleep(3)
driver.find_element_by_accessibility_id("我的淘宝").click()

driver.quit()
