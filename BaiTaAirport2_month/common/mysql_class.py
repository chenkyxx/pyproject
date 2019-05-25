# coding:utf-8
import base64
import binascii
import pymysql as ps
from PIL import Image
import numpy as np


class DataBase(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connect = ps.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.password,
                                  database=self.database,
                                  charset='utf8',
                                  use_unicode=True)
        self.cursor = self.connect.cursor()

    def get_cursor(self):
        return self.cursor

    def get_connect(self):
        return self.connect

    def close_database(self):
        """关闭数据库"""
        self.cursor.close()
        self.connect.close()

    def cud(self, sql):
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            print("ok")
        except Exception as A:
            print('cud出现错误'+str(A))
        self.close_database()

    def find_all(self, sql):
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            self.close_database()
            return data
        except Exception as e:
            print("错误"+str(e))

if __name__ == '__main__':
        shujuku = DataBase("192.168.1.101", 3306, "root", "123456", "test")
        fp = open("C:/Users/Administrator/Desktop/1.jpg", "rb")
        img = fp.read()
        sree = base64.b64encode(img)
        print(sree)
        aa = base64.b64decode(sree)
        print(aa)
        print(img)
        fp.close()
        sql = "INSERT INTO `test`.`test` (photo) VALUES (%s)" % img
        args = [1, img]
        print(sql)
        c = shujuku.get_cursor()
        co = shujuku.get_connect()
        c.execute(sql)

        co.commit()

        # 关闭游标
        c.close()
        # 关闭连接
        co.close()
