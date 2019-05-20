# coding:utf-8
from BaiTaAirport2_month.common.common_method import *
import requests


class BlackListApi(object):
    """对黑名单管理的CRUD类"""
    def __init__(self, host="http://192.168.10.188:9090/"):
        self.apiId = "123456"
        self.apiKey = "1285384ddfb057814bad78127bc789be"
        self.host = host
        self.anjian_server = "security-server"
        self.review_server = "review-server"
        self.boardinggate_server = "boardinggate-server"
        self.data_platform_server = "data-platform-server"
        self.black_list_save = self.host+self.data_platform_server+"/api/v1/face/backlist/save"
        self.black_list_delete = self.host+self.data_platform_server+"/api/v1/face/backlist/delete"
        self.black_list_query = self.host+self.data_platform_server+"/api/v1/face/backlist/query"
        self.black_list_record_query = self.host+self.data_platform_server+"/api/v1/face/backlist/record/query"
        self.backlist_record_latest = self.host+self.data_platform_server+"/api/v1/face/backlist/record/latest"  # 黑名单最新记录查询接口

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def get_headers(self, sign):
        """获取各个接口的请求头"""
        timestamp = get_time_stamp()
        sign1 = to_md5_str(sign+timestamp+self.apiKey)
        header = {"apiId": self.apiId,
                  "sign": sign1,
                  "timestamp": timestamp}
        return header

    def api_black_list_save(self,
                            reqId=get_uuid(),
                            ids="",
                            certificateNumber="",
                            peopleName="",
                            focusType="",
                            img=""
                            ):
        """黑名单增加接口"""
        body = {"reqId": reqId,
                "id": ids,  # 32位UUID，流水表记录ID，有就更新，无则增加
                "certificateNumber": certificateNumber,
                "peopleName": peopleName,
                "focusType": focusType,
                "img": img
                }
        res = requests.post(url=self.black_list_save,
                            headers=self.get_headers("/api/v1/face/backlist/save"),
                            json=body,
                            verify=False)
        res.close()
        return res

    def api_black_list_delete(self,
                              this_sign="/api/v1/face/backlist/delete",
                              reqId=get_uuid(),
                              ids=""):
        """黑名单删除接口"""
        body = {"reqId": reqId,
                "ids": ids}
        res = requests.post(url=self.black_list_delete, headers=self.get_headers(this_sign),
                            json=body,
                            verify=False)
        res.close()
        return res.text

    def api_black_list_query(self,
                             reqId=get_uuid(),
                             page=1,
                             pageSize=1,
                             isCount=None):
        """黑名单查询接口"""
        this_sign = "/api/v1/face/backlist/query",
        body = {"reqId": reqId,
                "page": page,
                "pageSize": pageSize,
                "isCount": isCount}
        res = requests.post(url=self.black_list_query, headers=self.get_headers(this_sign),
                            json=body,
                            verify=False)
        res.close()
        return res.text

    def api_black_list_record_query(self,
                                    reqId=get_uuid(),
                                    areaCode="",
                                    date="",
                                    passengerName="",
                                    cardId="",
                                    kindType="",
                                    addressType="",
                                    page=1,
                                    pageSize=1,
                                    isCount=None):
        """黑名单报警记录查询接口"""
        this_sign = "/api/v1/face/backlist/record/query"
        body = {"reqId": reqId,
                "areaCode": areaCode,
                "date": date,    # 开始时间，格式yyyymmdd。如2018070109
                "passengerName": passengerName,   # 姓名
                "cardId": cardId,   # 证件号
                "kindType": kindType,  # 布控类型 0：布控人员 1：失信人员 2：重点检测人员
                "addressType": addressType,  # 出现地点类型 0：自助闸机 1：复核闸机
                "page": page,
                "pageSize": pageSize,
                "isCount": isCount}
        res = requests.post(url=self.black_list_record_query, headers=self.get_headers(this_sign),
                            json=body,
                            verify=False)
        res.close()
        return res.text

    def api_face_backlist_record_latest(self,
                                        reqId=get_uuid(),
                                        areaCode="",
                                        deviceCode=""):
        """2.4.16.5黑名单最新记录获取接口"""
        body = {"reqId": reqId,
                "areaCode": areaCode,   # 否
                "deviceCode": deviceCode}  # 否
        res = requests.post(url=self.black_list_record_query,
                            headers=self.get_headers("/api/v1/face/backlist/record/latest"),
                            json=body,
                            verify=False)
        res.close()
        return res.text

if __name__ == '__main__':
    board_no_list = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '052', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '067', '068', '069', '070', '071', '072', '073', '074', '075', '076', '077', '078', '079', '080', '081', '082', '083', '084', '085', '086', '087', '088', '089', '090', '091', '092', '093', '094', '095', '096', '097', '098', '099', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '294', '295', '296', '297', '298', '299', '300', '301', '302', '303', '304', '305', '306', '307', '308', '309', '310', '311', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '322', '323', '324', '325', '326', '327', '328', '329', '330', '331', '332', '333', '334', '335', '336', '337', '338', '339', '340', '341', '342', '343', '344', '345', '346', '347', '348', '349', '350', '351', '352', '353', '354', '355', '356', '357', '358', '359', '360', '361', '362', '363', '364', '365', '366', '367', '368', '369', '370', '371', '372', '373', '374', '375', '376', '377', '378', '379', '380', '381', '382', '383', '384', '385', '386', '387', '388', '389', '390', '391', '392', '393', '394', '395', '396', '397', '398', '399', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '419', '420', '421', '422', '423', '424', '425', '426', '427', '428', '429', '430', '431', '432', '433', '434', '435', '436', '437', '438', '439', '440', '441', '442', '443', '444', '445', '446', '447', '448', '449', '450', '451', '452', '453', '454', '455', '456', '457', '458', '459', '460', '461', '462', '463', '464', '465', '466', '467', '468', '469', '470', '471', '472', '473', '474', '475', '476', '477', '478', '479', '480', '481', '482', '483', '484', '485', '486', '487', '488', '489', '490', '491', '492', '493', '494', '495', '496', '497', '498', '499', '500']
    blacklist = BlackListApi()
    # 开始进行黑名单注册
    n = 0
    body = {"reqId": get_uuid(),
            "certificateNumber": "003228199312134390",
            "peopleName": "bukong3",
            "focusType": "0",
            "img": to_base64(testcardpath+"/"+str(3)+".jpg")}
    res = blacklist.api_black_list_save(reqId=get_uuid(),
                                        certificateNumber="500238199312134390",
                                        peopleName="陈克云",
                                        focusType="0",
                                        img=to_base64(testcardpath+"/"+str(3)+".jpg"))
    print(res.text)
