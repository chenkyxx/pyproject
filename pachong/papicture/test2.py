# coding:utf-8
import requests
from bs4 import BeautifulSoup
r = requests.get("http://image.baidu.com/search/index?tn=baiduimage&ct=2""01326592&lm=-1&cl=2&ie=gb18030&word=%B7%E7%BE%B0&fr=ala&al""a=1&alatpl=adress&pos=0&hs=2&xthttps=000000",verify=False)
# print(r.content)

soup = BeautifulSoup(r.content,"html.parser")
soup1 = soup.prettify()
print(soup1)
all = soup.find_all(class_="main_img img-hover")
print(all)



