# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x200")
def helloCallBack():
    msg=messagebox.showinfo( "Hello Python", "Hello World")
B = Button(top, text ="Hello", command = helloCallBack)
B.place(x=50,y=50)
top.mainloop()