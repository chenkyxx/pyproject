# coding:utf-8
import pytest
# 通过conftest进行预制操作


def test_01(log):
    print("执行了测试test_01")

def test_02(exit_name):
    print("执行了测试test_02")


if __name__ == '__main__':
    pytest.main(["-q test_peizhi.py"])