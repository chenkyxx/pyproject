# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 21:10
# @Author  : chenky
# @Email   : 842202171@qq.com
# @File    : 6课 uiautomator定位.py
# @Software: PyCharm
# @Project : pyproject

from appium import webdriver
import time

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
driver.find_element_by_xpath("//*[contains(@text,'同意')]").click()
time.sleep(3)
# 1. text定位

driver.find_element_by_android_uiautomator('text("注册/登录")').click()
time.sleep(2)
# text("text文本")

# 2.文本比较长的时候，可以用textContains模糊匹配,只要文本包含匹配内容就可以了。
# textContains("包含text文本")

# 3.textStartsWith是以某个文本开头的匹配

# textStartsWith("以text文本开头")

# 4.正则匹配textMatches，这个需要配合正则表达式。

# textMatches("正则表达式")

# 5. resourceId 定位
driver.find_element_by_android_uiautomator('resourceId("com.taobao.taobao:id/aliuser_login_mobile_et")').click()
time.sleep(2)
# 6className("className")
# 7 description(“xxxx")
driver.find_element_by_android_uiautomator('description("帮助")').click()
time.sleep(1)
# 8 组合定位  id+text  class+text  例子：'resourceId("com.taobao.taobao:id/aliuser_login_mobile_et")'.text("捏的")
# 9 通过父子定位
l = 'resourceId("com.taobao.taobao:id/aliuser_login_mobile_et").childSelector(text("222"))'
# 10 通过兄弟定位
ll = 'resourceId("com.taobao.taobao:id/aliuser_login_mobile_et").fromParent(text("222"))'
time.sleep(1)
driver.quit()