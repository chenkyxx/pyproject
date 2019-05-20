# coding:utf-8
from tkinter import *
from tkinter import messagebox


class JiSuan(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("450x300")
        self.label = Label(self.root, text="计算器V1.0")
        self.label.pack()
        self.xx = StringVar(self.root)
        self.yy = StringVar(self.root)
        self.result = StringVar(self.root)

        self.fm = Frame(self.root)
        self.entry_xx = Entry(self.fm, textvariable=self.xx).pack()
        self.entry_yy = Entry(self.fm, textvariable=self.yy).pack()
        self.entry_result = Entry(self.fm, textvariable=self.result).pack()
        self.botton = Button(self.fm, text="计算结果", command=self.add).pack()
        self.fm.pack()

    def add(self):
        try:

            m = float(self.xx.get())+float(self.yy.get())
            a = int(m)
            self.result.set(a)
        except:
            messagebox.showinfo(" error", message="输入错误，只能输入数字")


def main():
    d = JiSuan()
    mainloop()

if __name__ == '__main__':
     main()