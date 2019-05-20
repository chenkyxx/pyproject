# coding:utf-8
import xlrd
import xlwt


class ReadWriteExcel(object):
    """读写excel类的封装"""
    def __init__(self, filepath):
        # 解析excel文件
        self.worksheet = xlrd.open_workbook(filename=filepath)

    def get_sheets(self):
        """
        :return: excel中所有sheetbook的name的list
        """
        sheet_names = self.worksheet.sheet_names()
        return sheet_names

    def get_sheet_class_index(self, a):
        """
        通过sheet工作表的索引返回sheet对象
        :param a: 索引
        :return: class，sheet
        """
        sheet1 = self.worksheet.sheet_by_index(a)
        return sheet1

    def get_sheet_class_name(self, sheet_name):
        """
        通过sheet工作表的名称返回sheet对象
        :param sheet_name: 工作表的对象名称
        :return: sheet_name对应的sheet对象
        """
        sheet1 = self.worksheet.sheet_by_name()
        return sheet1

    def get_rows_cols_num(self, a, row=None,col=None):
        """获取sheet对象的sheet的行数或者列数
        :param: a 第a个sheet对象
        :return: sheet 对象中所有的行数
        """
        if row is not None:
            try:
                rows = self.get_sheets()[a].nrows
                return rows
            except Exception as E:
                print(E)
        elif col is not None:
            try:
                cols = self.get_sheets()[a].ncols
                return cols
            except Exception as e:
                print(e)
        else:
            print("只能传入row和col中的一个")

    def get_cols_list(self, a):
        """
        获取以a为索引列放入list对象中，用来存储该列的value
        :param a:
        :return:
        """
        sheet_a = self.worksheet.sheet_by_index(a)
        value_list = sheet_a.col_values(a)
        return value_list


if __name__ == '__main__':
    pass
