# coding:utf-8

from locust import HttpLocust,TaskSet,task,TaskSequence,seq_task
import requests
import urllib.parse
import time
host = 'http://127.0.0.1:81'  # 禅道的服务器地址

def login(s, user= "admin", psw="e10adc3949ba59abbe56e057f20f883e"):
    u'''登录禅道'''
    loginUrl = host+"/zentao/user-login.html"
    h = {
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        # "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        # "Accept-Encoding": "gzip, deflate",
        # "Referer": host+"/zentao/user-login.html",
        # # "Cookie":  # 头部没登录前不用传cookie，因为这里cookie就是保持登录的
        # "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded"
        }

    body = {"account": user,
            "password": psw,
            "keepLogin[]": "on",
            "referer": host+"/zentao/my/"
            }
    try:
        r = s.post(loginUrl, data=body, headers=h)
        print(r.content.decode("utf-8"))  # 打印结果看到location='http://127.0.0.1/zentao/my/'说明登录成功了
        if "/zentao/my/" in str(r.content):
            print("登录成功！")
            return True
        else:
            print("登录失败：%s" % r.content)
            return False
    except Exception as msg:
        print("登录失败:%s"%str(msg))
        return False


class Behavior(TaskSequence):
    @task()
    def first_task(self):
        self.client.get("/")

class User(HttpLocust):
    host = "http://www.baidu.com"
    task_set = Behavior
    min_wait = 100
    max_wait = 500
if __name__=="__main__":
    import os
    com1 = "f:"
    com2 = r"cd F:\pyproject\test01\test_8_10"
    com3 = "locust -f xingn.py  --web-host=127.0.0.1 --master"
    com4 = "locust -f xingn.py  --web-host=127.0.0.1 --slave"
    os.system(com1)
    os.system(com2)  # s = requests.session()
    os.system(com3)
    # time.sleep(1)
    # os.system(com4)



    # login(s, user="admin", psw="e10adc3949ba59abbe56e057f20f883e")