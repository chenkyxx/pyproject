# coding:utf-8
import requests

def get_picture(piceurename):
    """
    文件服务器中图片下载接口
    :param piceurename:
    :return:
    """
    url = "http://192.168.0.232:9090/group1/M00/00/0C/" + piceurename
    res = requests.get(url)
    print(res.text)
    return res.content


if __name__ == '__main__':
    get_picture("1.jpg")