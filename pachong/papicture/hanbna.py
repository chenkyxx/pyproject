# coding: utf-8
import requests
import xlrd
import xlwt
import json


def excelJsonfile():
    jsobj = json.load(open(r'C:\Users\Administrator\Desktop\1.json'))
    list1=jsobj["presp"]["pdata"]["flyStatus"]
    workbook = xlwt.Workbook()
    sheet1= workbook.add_sheet(sheetname="airphone",cell_overwrite_ok=True)
    k=0
    for i in list1:
        ptd = str(i["ptd"])
        flyNo = str(i["flyNo"])
        pterminal1 = str(i["pterminal1"])
        sheet1.write(k,0,ptd)
        sheet1.write(k,1,flyNo)
        sheet1.write(k,2,pterminal1)
        workbook.save(filename_or_stream="air.xls")
        k += 1
        print(ptd, flyNo, pterminal1)
    print()
excelJsonfile()






