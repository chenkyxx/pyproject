# coding:utf-8
from xml.etree import ElementTree as ET
from Airport.msgQueue.msg import *
from Airport.new_method import *


def send_lkxx(lk_IsInternation="0",
              lk_bdno="01",
              lk_cardid="500238199312134390",
              lk_chkt="20180929103700",
              lk_cname="陈克云",
              lk_date="20180929",
              lk_desk="CTU",
              lk_flight="3U8317",
              lk_id="0000001",
              lk_inf="  ",
              lk_insur="0",
              lk_sex="1",
              lk_vip="0"):
    """
    发送旅客信息表到消息队列
    :param lk_IsInternation:  1     是否国际 0否，1是，2未知
    :param lk_bdno:           2     <!--2登机号 10 登机序号 -->  3位
    :param lk_cardid:         4     证件号码
    :param lk_chkt:           6     值机日期
    :param lk_cname:          8     旅客中文姓名80
    :param lk_date:           9     9航班日期 8 YYYYMMDD
    :param lk_desk:           11    11目的地  机场三字代表码
    :param lk_flight:         13    航班号 12
    :param lk_id:             15    旅客ID 主键 str 36
    :param lk_inf:            16    16婴儿标志3 INF带婴儿 “”表示未带婴儿
    :param lk_insur:          18    是否购保1
    :param lk_sex:            23    性别  1男性 2女性 0 未知
    :param lk_vip:            26    是否是贵宾1 否0，是1，未知2
    :return:
    """
    base_file_path = os.path.realpath(__file__)
    base_dir_path = os.path.dirname(base_file_path)
    project_path = os.path.dirname(base_dir_path)
    xml_path = os.path.join(project_path, "aj系统xml文件")
    ET.register_namespace(prefix="", uri="http://schemas.datacontract.org/2004/07/Xasd.FASC.SECM.Entity")
    tree = ET.parse((xml_path+"/"+"lkxx.xml"))
    root = tree.getroot()
    root[3][0][1].text = lk_IsInternation
    root[3][0][2].text = lk_bdno
    root[3][0][4].text = lk_cardid
    root[3][0][6].text = lk_chkt
    root[3][0][8].text = lk_cname
    root[3][0][9].text = lk_date
    root[3][0][11].text = lk_desk
    root[3][0][13].text = lk_flight
    root[3][0][15].text = lk_id
    root[3][0][16].text = lk_inf
    root[3][0][18].text = lk_insur
    root[3][0][23].text = lk_sex
    root[3][0][26].text = lk_vip
    tree.write(file_or_filename="lkxx1.xml",
               encoding="utf-8",
               xml_declaration=True)
    with open("lkxx1.xml", "rb") as fp:
        data = fp.read().decode("utf-8")
        #print(data)
        send_msg(data)


def send_ajxx(ajxxb_id="1138301",
              lk_id="0000001",
              safe_flag="0",
              safe_no="20",
              safe_oper="PA0100",
              safe_time="20180930091420"):
    """
    发送安检信息到消息队列
    :param ajxxb_id:     1 安检信息id 主键35
    :param lk_id:        3 旅客id 35旅客在安检系统主键
    :param safe_flag:    4 安检状态 0未安检，1：已安检
    :param safe_no:      5 安检通道号20
    :param safe_oper:    6 安检验证员60
    :param safe_time:    10 安检时间14 YYYYMMDDhhmmss
    :return:
    """
    base_file_path = os.path.realpath(__file__)
    base_dir_path = os.path.dirname(base_file_path)
    project_path = os.path.dirname(base_dir_path)
    xml_path = os.path.join(project_path, "aj系统xml文件")
    ET.register_namespace(prefix="", uri="http://schemas.datacontract.org/2004/07/Xasd.FASC.SECM.Entity")
    tree = ET.parse((xml_path+"/"+"ajxx.xml"))
    root = tree.getroot()
    root[3][0][1].text = ajxxb_id
    root[3][0][3].text = lk_id
    root[3][0][4].text = safe_flag
    root[3][0][5].text = safe_no
    root[3][0][6].text = safe_oper
    root[3][0][10].text = safe_time
    tree.write(file_or_filename="ajxx1.xml",
               encoding="utf-8",
               xml_declaration=True)
    with open("ajxx1.xml", "rb") as fp:
        data = fp.read().decode("utf-8")
        #print(data)
        send_msg(data)


if __name__ == '__main__':
    send_lkxx(lk_cardid="500318199312134391", lk_chkt="20181011101201", lk_cname="cenkeyun",
              lk_date="20181011",
              lk_flight="GS6595",
              lk_id=get_uuid(),
              lk_bdno="147",
              lk_insur="1")









