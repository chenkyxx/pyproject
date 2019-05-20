# coding:utf-8
import sys
import threading
import queue

if(sys.version[:1] == "3"):import _thread as thread
# 如果版本号是3
else:import thread
a = queue.Queue()
m = queue.Queue()
kk1 = {"名字": "陈克云", "xingbie": "nan"}
kk2 = {"名字": "陈克云1", "xingbie": "nan1"}
kk3 = {"xingbie": "nan"}
kk4 = {"xingbie": "nan1"}
a.put(kk1)
a.put(kk2)
m.put(kk3)
m.put(kk4)
print(a.qsize())
print(a.full())
print(a._get()["名字"],m._get()["xingbie"])
print(a._get()["名字"],m._get()["xingbie"])
# print(a._get()["名字"],m._get()["xingbie"])
# print(a._get()["名字"])


print(a.qsize())
print(a.empty())
