# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 22:27
# @Author  : chenky
# @Email   : 842202171@qq.com
# @File    : 7课 webview.py
# @Software: PyCharm
# @Project : pyproject

from appium import webdriver
import time

desired_caps = {"platformName": "Android",
                "deviceName": "emulator-5554",
                "platformVersion": "5.1.1",
                "noReset": True,
                # "unicodeKeyboard": True,  # 使用unicode编码方式发送字符串
                # "resetKeyboard": True,  # 隐藏键盘
                "appPackage": "com.yipiao",
                "appActivity": "com.yipiao.activity.LaunchActivity",
                }
driver = webdriver.Remote(desired_capabilities=desired_caps,
                          command_executor="http://127.0.0.1:4723/wd/hub")

time.sleep(10)
driver.find_element_by_android_uiautomator('text("下次再说")').click()
time.sleep(2)
driver.find_element_by_xpath("//*[@text='我的']").click()
time.sleep(2)

# 注意 以下这种定位方式外围只能是单引号
driver.find_element_by_android_uiautomator('text("产品意见")').click()
time.sleep(1)

print(driver.contexts)

driver.switch_to.context('WEBVIEW_com.yipiao')
p = driver.page_source
print(p)
time.sleep(2)
from selenium.webdriver.common.touch_actions import TouchActions
e1 = driver.find_element_by_css_selector('ol[class="bc-tags-block-content"]>li:nth-child(3)')
TouchActions(driver).tap(e1).perform()
# e2 = driver.find_element_by_xpath("//*[text()='酒店问题']")
# TouchActions(driver).tap(e2).perform()
time.sleep(2)
driver.quit()


if __name__ == '__main__':
    pass