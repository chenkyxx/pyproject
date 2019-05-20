# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import logging
# from webstudy.test.Log import MyLog

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

handle = logging.FileHandler('log.log', encoding="utf-8")
handle.setLevel(level=logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s")
handle.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)

logger.addHandler(handle)
logger.addHandler(console)


class Base(object):
    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def find_element(self, locator):
        if not isinstance(locator, tuple):
            logger.warning("定位方式错误，必须是元祖类型")
        else:
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            logger.info("正在开始定位：定位方式为<%s>====value为:<%s>" % (locator[0], locator[1]))
            return ele

    def send_text(self, locator, text):
        self.find_element(locator).send_keys(text)
        logger.info("发送文本"+"-->"+text)

    def click_element(self, locator):
        self.find_element(locator).click()
        logger.info("进行点击事件")

if __name__ == '__main__':
    url = "https://www.baidu.com"
    locator_sou = ("id", "kw")
    locator_click = ('id', 'su')
    locator_result1 = ("xpath", "//div[@id='2']/h3/a[@target='_blank']")
    locator_result2 = ("css selector", 'div[id="1"]>h3>a[target="_blank"]')
    locator_result3 = ("xpath", "//div[@id='1']/h3/a[@class='favurl']/em")
    driver = webdriver.Firefox()
    driver.get(url)
    baidu = Base(driver)
    try:
        baidu.send_text(locator_sou, "qq邮箱")
    except:
        logger.warning("AttributeError: 'NoneType' object has no attribute 'send_keys'")
    baidu.click_element(locator_click)
    baidu.click_element(locator_result2)
    time.sleep(10)

    baidu.driver.quit()
