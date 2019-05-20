# coding:utf-8
import unittest
import os
from Airport.Auto_return import HTMLTestRunner_cn


def add_case(dirname):

    current_path = os.path.realpath(os.path.dirname(__file__))
    case_path = os.path.join(current_path, dirname)
    discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    return discover


def run_all_case(discover, report_name):
    current_path = os.path.realpath(os.path.dirname(__file__))
    report_path = os.path.join(current_path, report_name+".html")
    fp = open(report_path, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                              verbosity=2,
                                              title=u"数据分析平台自动化测试报告",
                                              description=u"测试用例执行如下",
                                             )
    runner.run(discover)
    fp.close()


if __name__ == '__main__':
    run_all_case(add_case("TestCase"), "20181023")