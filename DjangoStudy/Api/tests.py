# coding:utf-8
import base64
import json

from django.test import TestCase
import requests
import time
# Create your tests here.

# int(38288)


class ClassIterator:
    def __init__(self):
        self.iter_keys = []

    # 对象转字典必须实现的方法,自动调用获取需要dict化的属性名
    def keys(self):
        return self.iter_keys

    # 对象模式序列化成dict必须实现的方法,和keys方法配合返回dict属性的value
    def __getitem__(self, key):
        return getattr(self, key)

    # 可以动态隐藏不需要返回的属性名
    def hide(self, *keys):
        for key in keys:
            self.iter_keys.remove(key)
        # 兼容链式调用(非常适合列表推导式)
        return self

    # 可以动态增加需要返回的属性名
    def append(self, *keys):
        for key in keys:
            self.iter_keys.append(key)
        # 兼容链式调用(非常适合列表推导式)
        return self


class Img():
    name = ""
    img = bytearray

    def __init__(self, name, img):
        self.name = name
        self.img = img


def test_1():
    url = "http://127.0.0.1:8000/process"
    body = {"pid": "38288"}
    res = requests.get(url=url,
                       params=body,
                       verify=False
                        )
    return res


def test_2():
    url = "http://127.0.0.1:8000/insert_sql"
    # fp = open("C:/Users/Administrator/Desktop/1.jpg", "rb")
    # data = fp.read()
    # mm = base64.b64encode(data)
    # aa = str(mm.decode)
    body ={"img": "C:/Users/Administrator/Desktop/1.jpg",
           "name": "1111111"}

    res = requests.post(url=url,
                        json=body,
                        verify=False)
    return res


def test_3():
    url = "http://127.0.0.1:8000/insert_other"
    # fp = open("C:/Users/Administrator/Desktop/1.jpg", "rb")
    # data = fp.read()
    # mm = base64.b64encode(data)
    # aa = str(mm.decode)
    body ={"photo": "C:/Users/Administrator/Desktop/1.jpg"}

    res = requests.post(url=url,
                        json=body,
                        verify=False)
    return res
if __name__ == '__main__':
    a = test_3()
    print(a.text)
