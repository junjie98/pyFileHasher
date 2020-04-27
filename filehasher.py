#!/usr/bin/python
# -*- coding: utf-8 -*-

#File Hasher Program

import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
import hashlib

window=tk.Tk()
window.title("File Hasher Tool Alpha Build")
window.minsize(800,400)
BLOCK_SIZE=65536

#Hashing Functions
def md5():
    file_hash=hashlib.md5()
    with askopenfile(mode='rb',filetypes=[('All files','*.*')]) as f:
        fb=f.read(BLOCK_SIZE)
        while len(fb)>0:
            file_hash.update(fb)
            fb=f.read(BLOCK_SIZE)
    data_string=StringVar()
    data_string.set("MD5 Hash: "+file_hash.hexdigest())
    entry=Entry(window,textvariable=data_string,fg="black",bg="white",bd=0,width=130,state="readonly",justify="center").pack()

def sha1():
    file_hash=hashlib.sha1()
    with askopenfile(mode='rb',filetypes=[('All files','*.*')]) as f:
        fb=f.read(BLOCK_SIZE)
        while len(fb)>0:
            file_hash.update(fb)
            fb=f.read(BLOCK_SIZE)
    data_string=StringVar()
    data_string.set("SHA-1 Hash: "+file_hash.hexdigest())
    entry=Entry(window,textvariable=data_string,fg="black",bg="white",bd=0,width=130,state="readonly",justify="center").pack()

def sha256():
    file_hash=hashlib.sha256()
    with askopenfile(mode='rb',filetypes=[('All files','*.*')]) as f:
        fb=f.read(BLOCK_SIZE)
        while len(fb)>0:
            file_hash.update(fb)
            fb=f.read(BLOCK_SIZE)
    data_string=StringVar()
    data_string.set("SHA-256 Hash: "+file_hash.hexdigest())
    entry=Entry(window,textvariable=data_string,fg="black",bg="white",bd=0,width=130,state="readonly",justify="center").pack()

def sha512():
    file_hash=hashlib.sha512()
    with askopenfile(mode='rb',filetypes=[('All files','*.*')]) as f:
        fb=f.read(BLOCK_SIZE)
        while len(fb)>0:
            file_hash.update(fb)
            fb=f.read(BLOCK_SIZE)
    data_string=StringVar()
    data_string.set("SHA-512 Hash: "+file_hash.hexdigest())
    entry=Entry(window,textvariable=data_string,fg="black",bg="white",bd=0,width=130,state="readonly",justify="center").pack()

#Other Functions
def quit():
    window.destroy()
    
#Main GUI
f=Frame(window)
Label(window,text="Select Hashing Method:").pack(side=TOP,pady=10)
Button(f,text="MD5",command=md5,width=8,borderwidth=3).pack(side=LEFT,padx=5)
Button(f,text="SHA-1",command=sha1,width=8,borderwidth=3).pack(side=LEFT,padx=5)
Button(f,text="SHA-256",command=sha256,width=8,borderwidth=3).pack(side=LEFT,padx=5)
Button(f,text="SHA-512",command=sha512,width=8,borderwidth=3).pack(side=LEFT,padx=5)
Button(window,text="Quit",command=quit,width=8,borderwidth=3).pack(side=BOTTOM,pady=10)
copyright_symbol = u"\u00A9"
Label(window,text="Copyright "+copyright_symbol+" 2020 Written By: Koh Jun Jie").pack(side=BOTTOM)
f.pack()

window.mainloop()

