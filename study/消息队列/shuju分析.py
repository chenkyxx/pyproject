# coding:utf-8
import linecache
import re


def get_file_list(filepath:str) ->list:
    """
    :param filepath: 对应的文件路径
    :return: list
    """
    list_desk = linecache.getlines(filename=filepath)
    return list_desk

if __name__ == '__main__':
    a = get_file_list(r"C:\Users\Administrator\Desktop\SDK测试情况\10x10\log.log")
    for i in a:
        # m1 =re.match(r".*值为：(/w+)", i)
        # m1 =re.match(r".*值为：(.+)", i)
        m1 = str(i).split("为")
        if "识别出的" in m1 or "识别出的":
            print("id为%d个人" % int(m1[1][0:1])+"比对的人员为"+m1[1][0:1]+"对应的分数值为"+m1[2])
