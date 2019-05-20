# coding:utf-8
import os
from tkinter import *


class DirList(object):
    def __init__(self, inintdir=None):
        self.top = Tk()
        self.label = Label(self.top, text="Directory Listen V1.1")
        self.label.pack()

        self.cwd = StringVar(self.top)
        self.dir1 = Label(self.top, fg="bule", font=('Helvetica', 12, "bold"))
        self.dir1.pack()

        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)  # ???
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set())  # ??
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview())
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

        self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
        self.dirn.bind(sequence="<Return-1>", self.doLS)
        self.dirn.pack()

        self.brm = Frame(self.top)
