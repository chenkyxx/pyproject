# coding:utf-8
from webtest.common import HTMLTestRunner_cn
import unittest
import os


def add_testcase(case="case"):
    global currentpath
    currentpath = os.path.realpath(__file__)
    path1 = os.path.dirname(currentpath)
    casepath = os.path.join(path1, case)
    discover = unittest.defaultTestLoader.discover(start_dir=casepath,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    return discover


def run_case(suit,name="testreport"):
    path2 = os.path.dirname(currentpath)
    reportpath = os.path.join(path2, "report", "%s.html" % name)
    fp = open(reportpath, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                              verbosity=2,
                                              title=u"web自动化测试报告",
                                              description=u"测试结果详情",
                                              retry=0,
                                              save_last_try=False)
    runner.run(suit)
    fp.close()

if __name__ == '__main__':
    suit = add_testcase()
    run_case(suit)
