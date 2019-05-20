# coding:utf-8
import pytest
"""
以下代码单独管理预制操作流程
"""

@pytest.fixture()
def log():
    print("执行log操作")


@pytest.fixture()
def exit_name():
    print("执行exit操作")