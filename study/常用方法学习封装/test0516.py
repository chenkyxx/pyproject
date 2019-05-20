# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 0:35
# @Author  : chenky
# @Email   : 842202171@qq.com
# @File    : test0516.py
# @Software: PyCharm
# @Project : pyproject

import xlrd
import xlwt


def help(basepath: str,start_rows:int,end_rowx:int, colx:int):
    """
    返回规定列的值存储在一个list、中
    :param basepath:
    :param start_rows: 开始的行数
    :param end_rowx: 结束的行数
    :param colx: 从地N列开始数
    :return:
    """
    wooksheets = xlrd.open_workbook(basepath)
    sheet = wooksheets.sheet_by_name("年度工资申报")
    list_a = sheet.col_values(start_rowx=3, end_rowx=56, colx=3)
    return list_a


def search_money(basepath:str, searchname:str):
    worksheets = xlrd.open_workbook(basepath)
    sheets = worksheets.sheet_names()  # 返回所有sheet的name
    list_sheet = ['行政', '事业', '村官', '本土人才', '扶贫信息员', '村干部']
    value = []
    for sheet_name in list_sheet:
        if sheet_name == "行政":
            sheet = worksheets.sheet_by_name("行政")
            list_cols = sheet.col_values(0,3,38)
            for i in range(0, list_cols.__len__()-1):
                if list_cols[i] == searchname:
                    # 找到对应的工资
                    list_cols_money = sheet.col_values(2)
                    # 将找出来的工资保存到list中
                    value.append(list_cols_money[i])
        elif sheet_name == list_sheet[1]:
            sheet = worksheets.sheet_by_name(list_sheet[1])
            list_cols_name = sheet.col_values(0, 3, 41)
            for i in range(0, list_cols_name.__len__()-1):
                if list_cols_name[i] == searchname:
                    # 找到对应的工资
                    list_cols_money = sheet.col_values(2)
                    # 将找出来的工资保存到list中
                    value.append(list_cols_money[i])
        elif sheet_name == list_sheet[2]:
            sheet = worksheets.sheet_by_name(list_sheet[2])
            list_cols_name = sheet.col_values(0, 3, 7)
            for i in range(0, list_cols_name.__len__()-1):
                if list_cols_name[i] == searchname:
                    # 找到对应的工资
                    list_cols_money = sheet.col_values(2)
                    # 将找出来的工资保存到list中
                    value.append(list_cols_money[i])
        elif sheet_name == list_sheet[3]:
            sheet = worksheets.sheet_by_name(list_sheet[3])
            list_cols_name = sheet.col_values(1, 3, 11)
            for i in range(0, list_cols_name.__len__()-1):
                if list_cols_name[i] == searchname:
                    # 找到对应的工资
                    list_cols_money = sheet.col_values(3)
                    # 将找出来的工资保存到list中
                    value.append(list_cols_money[i])
        elif sheet_name == list_sheet[4]:
            sheet = worksheets.sheet_by_name(list_sheet[4])
            list_cols_name = sheet.col_values(1, 3, 5)
            for i in range(0, list_cols_name.__len__()-1):
                if list_cols_name[i] == searchname:
                    # 找到对应的工资
                    list_cols_money = sheet.col_values(3)
                    # 将找出来的工资保存到list中
                    value.append(list_cols_money[i])
        elif sheet_name == list_sheet[5]:
            sheet = worksheets.sheet_by_name(list_sheet[5])
            list_cols_name = sheet.col_values(1, 3, 169)
            for i in range(0, list_cols_name.__len__()-1):
                if list_cols_name[i] == searchname:
                    # 找到对应的工资
                    list_cols_money = sheet.col_values(3, 3, 169)
                    list_cols_money_kouchu = sheet.col_values(4, 3, 169)
                    value.append(list_cols_money)
                    # 便利循环 找到两份工资的减去一半
                    for m in range(0, list_cols_money.__len__()-1):
                        if float(list_cols_money[i]) == 2*float(list_cols_money_kouchu[i]):
                            value.append(str(list_cols_money_kouchu))
    return value


if __name__ == '__main__':
    print(search_money(r"C:\Users\Administrator\Desktop\2019年5月工资支付单.xls", "潘登锡"))
    # print(search_money(r"C:\Users\Administrator\Desktop\2019年5月工资支付单.xls"))
    # print(help(basepath=r"C:\Users\Administrator\Desktop\拷贝数据\填报表格 - 副本\在册人员工资明细表.xls"))