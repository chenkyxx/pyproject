# coding:utf-8
import pymysql
try:
    connection = pymysql.Connect(host="localhost",
                                 user="root",
                                 passwd="123456",
                                 port=3306,
                                 db="test",
                                 charset="utf8")
    curser1 = connection.cursor()
    sql = "select * FROM test;"
    k = curser1.execute(sql)
    m= curser1.fetchall()
    print(m[0])
    connection.commit()
    print(k)
    print(connection)
    curser1.close()
    connection.close()
    print("ok")
except Exception as result:
    print(result)

a= input("请输入你的名字：")
print(a)







