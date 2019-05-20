# coding:utf-8
import os

if __name__ == '__main__':
    current_path = os.path.realpath(__file__)
    # print(current_path)
    last_path = os.path.dirname(current_path)
    # print(last_path)
    commond1 = "F:"
    commond2 = "cd %s" % last_path
    commond3 = "pytest --html=report.html"
    os.system(commond1)
    os.system(commond2)
    os.system(commond3)