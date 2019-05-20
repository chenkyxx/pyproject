# coding:utf-8
import requests
import time



url = "http://127.0.0.1:8080/hello"

while True:
    try:
        r = requests.get(url=url)
        print(r.text)
    except:
        try:
            r = requests.get(url=url)
            print(r.text)
        except:
            break
