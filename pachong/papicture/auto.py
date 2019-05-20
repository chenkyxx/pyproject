# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
print("浏览器最大化")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id(id_="kw").send_keys(u"重庆天气")
driver.find_element_by_id(id_="su").click()
time.sleep(3)
driver.quit()
