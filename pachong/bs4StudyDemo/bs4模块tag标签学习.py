# coding:utf-8
from bs4 import BeautifulSoup
import sys


class BaseBs4(object):
    def __init__(self, filename, method="lxml", from_encoding="",exclude_encodings=""):
        """
        :param filename:  A string or a file-like object representing
        markup to be parsed.
        :param method:This
        may be the name of a specific parser ("lxml", "lxml-xml",
        "html.parser", or "html5lib") or it may be the type of markup
        to be used ("html", "html5", "xml")
        :param from_encoding:使用该参数确定编码
        :param exclude_encodings:排除掉不正确的字符编码
        :return:
        """
        self.position = filename
        self.parse_method = method  # 要使用的特定的解析器的名称
        self.soup = BeautifulSoup(markup=self.position,features=self.parse_method)

    def get_one_tag(self, tag_name: str, attribute):
        """
        通过标签名字 || 属性获得标签对象
        :param tag_name:
        :param attribute:
        :return:
        """
        tag_object = self.soup.find(name=tag_name, attrs=attribute)
        return tag_object

if __name__ == '__main__':
    parsetion = BaseBs4(open("test.html", "rb+"), method="lxml")
    a = parsetion.get_one_tag(tag_name="li", attribute={"nu": "1"})
    print("对象是："+str(type(a))+"\n"+str(a), file=sys.stderr)
    print(a.get_text())
    print(a.get_text().rstrip())
    print(a.get_text().rstrip().split(" ")[0])

    print("================")
    b = parsetion.get_one_tag(tag_name="li", attribute=None)
    print(b)

