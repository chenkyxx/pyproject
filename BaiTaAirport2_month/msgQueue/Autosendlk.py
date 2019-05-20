# coding:utf-8
from xml.etree import ElementTree as ET

from BaiTaAirport2_month.common.Log import MyLog
from BaiTaAirport2_month.common.common_method import *
from BaiTaAirport2_month.msgQueue.msg import send_msg

name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]
log = MyLog(name=name)


def send_lkxx(lk_IsInternation="0",
              lk_bdno="01",
              lk_cardid="500238199312134390",
              lk_chkt="20180929103700",
              lk_cname="陈克云",
              lk_date="20180929",
              lk_desk="CTU",
              lk_ename="HHHH",
              lk_flight="3U8317",
              lk_gateno="10",
              lk_id="0000001",
              lk_inf=" ",
              lk_insur="0",
              lk_outtime="20140626102446",
              lk_sex="1",
              lk_vip="0"):
    """
    发送旅客信息表到消息队列
    :param lk_IsInternation:  1     是否国际 0否，1是，2未知
    :param lk_bdno:           2     <!--2 10 登机序号 -->  3位
    :param lk_cardid:         4     证件号码
    :param lk_chkt:           6     值机日期
    :param lk_cname:          8     旅客中文姓名80
    :param lk_date:           9     9航班日期 8 YYYYMMDD
    :param lk_desk:           11    11目的地  机场三字代表码
    :param lk_ename:          12    旅客英文姓名
    :param lk_flight:         13    航班号 12
    :param lk_gateno          14    登机口号码 无意义
    :param lk_id:             15    旅客ID 主键 str 36
    :param lk_inf:            16    16婴儿标志3 INF带婴儿 “”表示未带婴儿
    :param lk_insur:          18    是否购保1
    :param lk_outtime:        20    旅客起飞时间
    :param lk_sex:            23    性别  1男性 2女性 0 未知
    :param lk_vip:            26    是否是贵宾1 否0，是1，未知2
    :return:
    """
    # list_data = []
    # person_info = {"lk_IsInternation": lk_IsInternation, "lk_bdno": lk_bdno, "lk_cardid": lk_cardid,
    #                "lk_chkt": lk_chkt, "lk_cname": lk_cname, "lk_date": lk_date, "lk_desk": lk_desk,
    #                "lk_ename": lk_ename, "lk_flight": lk_flight, "lk_id": lk_id, "lk_inf": lk_inf,
    #                "lk_insur": lk_insur, "lk_outtime": lk_outtime, "lk_sex": lk_sex, "lk_vip": lk_vip
    #                }
    # with open("./info.json", "r") as fp1:
    #     list_11 = list(fp1.read())
    #     print(type(list_11))
    #     list_data.extend(list_11)
    #     list_data.append(person_info)
    # with open("./info.json", "w", encoding="utf-8") as fp2:
    #     json.dump(fp2, list_data)

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
    root[3][0][12].text = lk_ename
    root[3][0][13].text = lk_flight
    root[3][0][14].text = lk_gateno
    root[3][0][15].text = lk_id
    root[3][0][16].text = lk_inf
    root[3][0][18].text = lk_insur
    root[3][0][20].text = lk_outtime
    root[3][0][23].text = lk_sex
    root[3][0][26].text = lk_vip
    tree.write(file_or_filename="lkxx1.xml",
               encoding="utf-8",
               xml_declaration=True)
    with open("lkxx1.xml", "rb") as fp:
        data = fp.read().decode("utf-8")
        print(data)
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
        print(data)
        send_msg(data)


if __name__ == '__main__':
    board_no_list = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '067', '068', '069', '070', '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', '081', '082', '083', '084', '085', '086', '087', '088', '089', '090', '091', '092', '093', '094', '095', '096', '097', '098', '099', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '329', '330', '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345', '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356', '357', '358', '359', '360', '361', '362', '363', '364', '365', '366', '367', '368', '369', '370', '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385', '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '430', '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441', '442', '443', '444', '445', '446', '447', '448', '449', '450', '451', '452', '453', '454', '455', '456', '457', '458', '459', '460', '461', '462', '463', '464', '465', '466', '467', '468', '469', '470', '471', '472', '473', '474', '475', '476', '477', '478', '479', '480', '481', '482', '483', '484', '485', '486', '487', '488', '489', '490', '491', '492', '493', '494', '495', '496', '497', '498', '499', '500']
    lk_sex = str(random.randint(1, 2))
    a = 2
    send_lkxx(lk_cardid="342425199012124714",
              lk_chkt=get_time_mmss(),
              lk_cname="潘俊涛",
              lk_date=produce_flight_date(),
              lk_desk="TEN",
              lk_flight="test001",
              lk_id=get_uuid(),
              lk_bdno="008",
              lk_insur="1",
              lk_outtime=get_flight_out_time(2),
              lk_sex="1")




