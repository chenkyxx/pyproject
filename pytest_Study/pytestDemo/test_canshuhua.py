# coding:utf-8
import pytest


# 进行几种形式的参数化
# @pytest.mark.parametrize("test_input,expected", [("3+5", 8),
#                                                  ("4+6",10),
#                                                  pytest.param("6*9",52)],)

# 参数组合
@pytest.mark.parametrize("x", [1, 2, 3, 49])
@pytest.mark.parametrize("y", [1, 5,6,7,8,9,10,12,13,14])
# def test_01(test_input,expected):
#     assert eval(test_input) == expected


def test_02(x,y):
    print("结果为"+str(x+y))

if __name__ == '__main__':
    pytest.main(["-q test_canshuhua.py"])