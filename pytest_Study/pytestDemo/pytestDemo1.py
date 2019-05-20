# coding:utf-8
import pytest
# 对pytest单元测试框架功能练习


# @pytest.yield_fixture()
class Test(object):

    def setup_class(self):
        print("所有用例运行前执行一次")

    def teardown_class(self):
        print("============所有用例执行后执行一次================")

    def setup(self):
        print("===========每个用例执行前执行一次=================")

    def teardown(self):
        print("==============每个用例执行后执行一次===============")

    def test_one(self):
        print("test_one")
        x = "this"
        assert "h" in x

    # def test_two(self):
    #     x = "hello"
    #     assert hasattr(x, "check")

    def test_three(self):
        print("test_three")
        a = "hello"
        b = "hello world"
        assert a in b

if __name__ == '__main__':
    pytest.main(["-q pytestDemo1.py"])



