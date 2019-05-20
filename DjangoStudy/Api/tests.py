# coding:utf-8
from django.test import TestCase
import requests
import time
# Create your tests here.

# int(38288)


def test_1():
    url = "http://127.0.0.1:8000/process"
    body = {"pid": "38288"}
    res = requests.get(url=url,
                       params=body,
                       verify=False
                        )
    return res


if __name__ == '__main__':
    while True:
        print(test_1().text)
