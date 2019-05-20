# coding:utf-8
import pymysql
from Airport.new_method import *


def create_user_data(n):
    users = []
    for i in range(n):
        username = 'user'+ str(i+1)
        users.append((username , '000000'))
        return users


if __name__ == '__main__':
    from Airport.数据库测试.idcard import idcard
    # print(len(idcard))
    conn = pymysql.connect(host='192.168.0.231',
                           user='root',
                           passwd='123456',
                           port=3306,
                           database='htbusyinfo',
                           charset='utf8')
    cur = conn.cursor()
    air_zhiji = []
    air_passger = []
    start_time = get_time_mmss()
    for kk in range(0, 980000):
        data = (get_add_idcard(kk, "c", 32),  # 将值机表的主键id
                get_add_idcard(kk, "d", 32),  # aib_passenger_id 旅客表的主键
                "LHW",  # arrive_port` varchar(64) DEFAULT NULL,
                "104",  # boarding_gate` varchar(32) DEFAULT NULL,
                "200",  # 登机序列号 boarding_number` varchar(64) DEFAULT NULL,
                "Z22",  # 值机柜台号 boarding_pass_counter_number` varchar(64) DEFAULT NULL,
                "2018-10-13 12:37:47",  # boarding_pass_time` datetime DEFAULT NULL,值机时间
                None,   # certificate_image_path` varchar(512) DEFAULT NULL,
                idcard[kk],  # certificate_number` varchar(64) DEFAULT NULL,证件号码
                0,  # certificate_type` int(11) DEFAULT NULL, 证件类型
                "0-20191206",  # certificate_validity` varchar(128) DEFAULT NULL,证件有效期
                "13512134390",  # 联系方式
                "2018-10-13 13:55:16",  # 创建 时间
                "2018-10-13 19:12:01",  # 离港日期
                "HET",  # 始发港
                "汉族",  # ethnic` varchar(16) DEFAULT NULL,名族
                get_add_idcard(kk, "e", 32),  # 来自安检信息系统的旅客值机id
                "LK"+str(kk),  # 航班号码
                "0",  # is_baby` tinyint(4) DEFAULT NULL,
                0,  # is_buy_insurance` int(11) DEFAULT NULL,
                None,  # ischild
                0,  # isdelete
                0,  # is_internation 0否
                0,  # is-vip
                None,  # luggage_number行李牌号
                "中国",  # nationality国籍
                "北京市优衣库",  # passenger_address 旅客住址
                get_age(idcard[kk]),  # passenger_age
                get_bir_year(idcard[kk]),  # passenger_birth_year
                produce_flight_date(),  # passenger_date 航班日期 以当前时间生成
                "passenger_english_name",  # passenger_english_name
                "10",  # passenger_month
                "name"+str(kk),  # passenger_name
                "0",  # passenger_sex
                get_flight_out_time(h=9),  # plan_start_fly_time
                "3B",  # seat_number
                None,  # terminal 航站楼
                "2018-10-13 13:55:16",  # update_time
                )
        air_zhiji.append(data)

        data_l = (get_add_idcard(kk, "d", 32),  # aib_passenger_id 旅客表的主键
                  None,  # is_baby null
                  "北京市优衣库",  # address` varchar(512) DEFAULT NULL 旅客住址
                  get_birthday(idcard[kk]),  # 旅客生日  birth_date
                  idcard[kk],  # certificate_number` varchar(64) DEFAULT NULL, 证件号码
                  None,  # certificate_photo_path` varchar(512) DEFAULT NULL,身份证照片路径
                  "0",  # certificate_type` int(11) DEFAULT NULL, 证件类型
                  "0-20191206",  # certificate_validity` varchar(128) DEFAULT NULL,证件有效期
                  "13512134390",  # contact_way` varchar(512) DEFAULT NULL,  联系方式
                  "2018-10-13 13:55:16",  # create_time` datetime DEFAULT NULL, 创建时间
                  "汉族",  # ethnic` varchar(16) DEFAULT NULL, 名族
                  "中国",  # nationality` varchar(16) DEFAULT NULL,国籍
                  get_bir_year(idcard[kk]),  # passenger_birth_year` varchar(4) DEFAULT NULL,旅客出生年
                  "passenger_english_name",  # passenger_english_name` varchar(128) DEFAULT NULL,旅客英文姓名
                  "name"+str(kk),  # passenger_name` varchar(64) DEFAULT NULL,中文姓名
                  "0",  # sex` int(11) DEFAULT NULL,
                  "2018-10-13 13:55:16",  # update_time` datetime DEFAULT NULL,
                  )
        air_passger.append(data_l)

    try:
        insert_zhiji_sql ='insert into sec_passenger_checkin_10_12 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        inser_passger_sql = 'insert into aib_passenger_90 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cur.executemany(insert_zhiji_sql, air_zhiji)
        cur.executemany(inser_passger_sql,air_passger)

    except Exception as e:
        print(e)
        print("sql execute failed")
    else:
        print("sql execute success")
    conn.commit()
    cur.close()
    conn.close()
    # sql ='select * from sec_passenger_checkin_10_12 where certificate_number="000000000000119164"'
    # k = cur.fetchone()
    # 输出结果集有多少条数据
    # print cursor.rowcount
    #  查询顶部第一个数据
    #  rs = cursor.fetchone()
    #  print rs
    #  查询向下查询n个数据
    #  rs = cursor.fetchmany(1)
    #  print rs # 向下查询全部数据
    # rs = cursor.fetchall()
    # for row in rs:
    # #固定格式输出
    # print "id=%s,name=%s" % row
    # #获取结果第一个参数 print row[0]
    # while i < 900000:
    #     try:
    #         insert_sql = 'insert into userinfo values(%s,%s)'
    #         users = create_user_data(100)
    #         cur.executemany(insert_sql,users)
    #     except Exception as e :
    #         print(e)
    #         print("sql execute failed")
    #     else:
    #         print("sql execute success" )
    #         conn.commit()
    #         cur.close()
    #         conn.close()
    end_time = get_time_mmss()
    print("开始为:%s,结束时间为:%s" % (start_time, end_time))







