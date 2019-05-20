# coding:utf-8
import pymysql as ps


class DataBase(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def open_data_base(self):
        """打开数据库的连接"""
        self.conn = ps.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               password=self.password,
                               database=self.database,
                             )
        self.curs = self.conn.cursor()

    def close_database(self):
        """关闭数据库"""
        self.curs.close()
        self.conn.close()

    def cud(self, sql):
        self.open_data_base()
        try:
            self.curs.execute(sql)
            self.conn.commit()
            print("ok")
        except Exception as A:
            print('cud出现错误'+str(A))
        self.close_database()

    def find_all(self, sql):
        self.open_data_base()
        try:
            self.curs.execute(sql)
            data = self.curs.fetchall()
            return data
        except:
            print("错误")

if __name__ == '__main__':
    shujuku = DataBase("192.168.0.231", 3306, "root", "123456", "faceguard")
    shujuku.open_data_base()
    # a = shujuku.find_all("select * from base_dictory_value;")
    # # shujuku.cud("insert into base_dictory_value VALUES ('14','9','2018-09-19 15:10:56','2018-09-19 15:10:59','android','1');")
    # b = shujuku.find_all("select * from base_dictory_value;")
    # for i in b:
    #     print(i)
    # print(b.__len__())
    #
    # shujuku.close_database()
    sql1 = "select * FROM face_library WHERE library_code='code00';"
    data = shujuku.find_all(sql1)
    print(type(data[0][0]))