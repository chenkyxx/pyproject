# coding: utf-8
from bs4 import BeautifulSoup
import requests
import urllib3
import asyncio
urllib3.disable_warnings()
r=requests.get("https://ishuo.cn/",verify=False)
soup=BeautifulSoup(r.content, "html.parser")
'''
解析成有层级关系的html格式 prettify
'''
soup1=soup.prettify()
tag1=soup.title  # tag完整标签对象
print(tag1)
print(tag1.string)  # 获取标签中的字符串
duanzi=soup.find_all(class_="content")
print(type(duanzi))
for i in duanzi:
    print(i.get_text().replace("\n",""))