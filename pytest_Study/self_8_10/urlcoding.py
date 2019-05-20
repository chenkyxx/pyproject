# coding:utf-8
from urllib import parse
import json

def dict_to_urlencoding(data):
    """
    将字典格式的数据转换成urlencodfing格式  eggs=2&bacon=0&spam=1'
    :param data: 要转换的字典格式的数据
    :return: 返回通过urlencong编码转换后的数据
    """
    str = parse.urlencode(data)
    return str


def str_to_urlencoding(str):
    """
    将字符串格式的数据转换成urlencoding编码
    :param str:要转换的字符串
    :return:返回转换的字符串
    """
    data = parse.quote(str)
    return data

def dict_to_jsonstr(dictdata):
    """
    把字典转换成json格式的字符串
    :param dictdata: 要转换的字典
    :return: 转换后的json格式的字符串
    """
    json_str = json.dumps(dictdata)
    return json_str


def main():
    print(" we are in %s"%__name__)

if __name__=="__main__":
    main()

