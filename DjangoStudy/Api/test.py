import unittest

from Api.models import IMG


class MyTestCase(unittest.TestCase):
    def test_1(self):
        fp = open("C:/Users/Administrator/Desktop/1.jpg", "rb")
        data = fp.read()
        imga = IMG(img=data, name="test11fgfgfgf")
        imga.save()


if __name__ == '__main__':
    unittest.main()
