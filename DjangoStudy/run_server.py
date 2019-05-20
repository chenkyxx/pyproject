# coding:utf-8
import os


def _main():
    """
    执行当前Django服务
    :return:
    """
    current_path = os.path.realpath(__file__)
    dir_path = os.path.dirname(current_path)
    real_path = os.path.join(dir_path, "manage.py")
    comm = "python %s runserver 127.0.0.1:8000" % real_path
    print("开启Django服务")
    os.system(comm)

if __name__ == '__main__':
    _main()