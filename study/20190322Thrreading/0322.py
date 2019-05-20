# coding:utf-8
import threading
from threading import Lock


num = 0

def change(n):
    global num
    num += n
    num -= n


def _run(n):
    for i in range(0,100000):
        try:

            change(n)
        finally:
            lock.release()


if __name__ == '__main__':
    a = threading.Thread(target=_run, args=(5,))
    b = threading.Thread(target=_run, args=(8,))
    # c = threading.Thread(target=_run, args=(9,))
    a.start()
    b.start()
    # c.start()
    print(num)