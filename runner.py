#!/usr/bin/python

import Tkinter
top = Tkinter.Tk()
top.title("read4me")
top.geometry("500x500")
# Code to add widgets will go here...
L1 = Tkinter.Label(top, text="User Name")
L1.pack( side = 'left')
E1 = Tkinter.Entry(top, bd =2,width=100)
E1.pack(side ='left')

b= Tkinter.Button(top,text="Start")

b.place(anchor='se',height=50,width=50)
top.mainloop();
