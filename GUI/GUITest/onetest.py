# coding:utf-8
from tkinter import *


def add():
    var3 = var1.get()+var2.get()
    return var3

if __name__ == '__main__':
    root = Tk()  # 创建一个tkinker.TK的实例root，该实例就是一个窗口
    root.title("计算程序")
    root.geometry("500x300")
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    frame = Frame(root)
    Label(frame, text='x的值').grid(row=0, sticky=W)
    Label(frame, text='y的值').grid(row=1, sticky=W)
    Entry(frame, textvariable=var1).grid(row=0, column=1, sticky=E)
    Entry(frame, textvariable=var2).grid(row=1, column=1, sticky=E)

    Button(frame, text="计算结果", command=add()).grid(row=2, column=1, sticky=W)
    Entry(frame, show=var3).grid(row=2, column=3, sticky=E)

    frame.grid()
    mainloop()    # 进行消息循环
