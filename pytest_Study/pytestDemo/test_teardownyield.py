# coding:utf-8
import pytest

# 以下代码用来利用teardown  yield进行唤醒操作

class A(object):
    name = 1

@pytest.fixture(scope="module")
def open():
    print("打开浏览器")

    yield
    print("执行teardown")
    print("关闭浏览器")


def test_01(open):
    print("test_01")
    raise NameError   # 其中一个用例遇到异常不影响其他用例的  teardown的执行


def test_02(open):
    print("test_02")


def test_03():
    x = "hello"
    assert hasattr(A(), "name")
    print(hasattr(A(), "name"))


@pytest.mark.skip(reason="不执行")   # pytest.mark.skip 可以标记无法在某些平台上运行的测试功能，戒者您希望失败的测试功
def test_04():
    print("zheco 跳过不执行")


@pytest.mark.xfail   # 当测试通过时尽管预计会失败（标有 pytest.mark.xfail），它是一个 xpass，将在测试摘要中报告
def test_05():
    print("bu 只能给")

if __name__ == '__main__':
    pytest.main(["-q", " test_teardownyield.py"])
