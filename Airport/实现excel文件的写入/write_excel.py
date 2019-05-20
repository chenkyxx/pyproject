# coding:utf-8
from xlwt import *
import os

def write_features(j):
    file = Workbook(encoding="utf-8")
    table = file.add_sheet("1比Nfeature值")
    current_path = "E:/test1w/id1w"
    list_picture = os.listdir(current_path)
    for i in range(0,j):
        with open("E:/test1w/1比Nlive"+"/"+list_picture[i]) as fp:
            data = fp.read().rstrip()

