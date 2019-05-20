# coding:utf-8
from webstudy.test.Log import *
log = MyLog()


def erq():
    a = 1
    log.logger.info("1")
    b =2
    log.logger.debug(b)

if __name__ == '__main__':
    erq()