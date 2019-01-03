#!/user/bin/python
#  -*-coding: utf-8-*-
from Tkinter import *
# top=Tkinter.Tk()
# top.mainloop()

root =Tk()          #创建窗口对象的背景色
li2=['a','b','pho']
li=['c','python','php','html','sql','java',li2]
movie=['css','jquery','bott']
listb=Listbox(root)
listb2=Listbox(root)

for item in li:
    listb.insert(1,item)

for iten in movie:
    listb2.insert(0,iten)
listb.pack()        #将小部件放置主窗口
listb2.pack()
root.mainloop()     #进入消息循环