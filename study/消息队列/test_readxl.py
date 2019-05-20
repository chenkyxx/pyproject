# coding:utf-8
import xlrd

if __name__ == '__main__':

    # 打开文件
    workbook = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\1.xls")
    workbook2 = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\2.xls")
        # 获取sheet
    sheet = workbook.sheet_names()[0]

    sheet1 = workbook.sheet_by_index(0)
    sheet2 = workbook2.sheet_by_index(0)
    # print(sheet1.name)
    # # 获取        行和        列数
    # print(sheet1.nrows, sheet1.ncols)

    list1 = sheet1.col_values(0)
    print(sheet1.col_values(0, 1, 2))
    list2 = sheet2.col_values(0)
    print(list1)
    print(list2)
    list3 = []
    for i in range(0,len(list1)-1):
        if list1[i] in list2:
            pass
        else:
            print(list1[i])
            list3.append(list1[i])
    print(len(list3))


