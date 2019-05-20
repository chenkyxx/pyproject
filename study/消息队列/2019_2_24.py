# coding:utf-8
import requests
import threading

import time


def get_baidu():
    res = requests.get(url="https://www.baidu.com")
    return res.status_code


class MyThread(threading.Thread):
    def run(self):
        while True:
            statues = get_baidu()
            print(statues)
            time.sleep(1)


if __name__ == '__main__':
    threadings_list = []
    for i in range(0, 100):
        threadings_list.append(MyThread())
    for k in threadings_list:
        k.start()