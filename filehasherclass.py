#!/usr/bin/python
# -*- coding: utf-8 -*-

#File Hasher Program

from tkinter import *
from tkinter.filedialog import askopenfile
import hashlib

BLOCK_SIZE=65536

#Main GUI
class window:
    def __init__(self,master):
        self.master=master
        master.title("File Hasher Tool Alpha Build")
        master.minsize(800,400)

        self.label=Label(master,text="Select Hashing Method:")
        self.label.pack(side=TOP,pady=10)

        self.frame=Frame()
        self.frame.pack()

        self.md5button=Button(self.frame,text="MD5",command=self.md5,width=8,borderwidth=3)
        self.md5button.pack(side=LEFT,padx=5)

        self.sha1button=Button(self.frame,text="SHA-1",command=self.sha1,width=8,borderwidth=3)
        self.sha1button.pack(side=LEFT,padx=5)

        self.sha256button=Button(self.frame,text="SHA-256",command=self.sha256,width=8,borderwidth=3)
        self.sha256button.pack(side=LEFT,padx=5)

        self.sha512button=Button(self.frame,text="SHA-512",command=self.sha512,width=8,borderwidth=3)
        self.sha512button.pack(side=LEFT,padx=5)

        self.quitbutton=Button(master,text="Quit",command=self.quit,width=8,borderwidth=3)
        self.quitbutton.pack(side=BOTTOM,pady=10)

        copyright_symbol = u"\u00A9"
        self.clabel=Label(master,text="Copyright "+copyright_symbol+" 2020 Written By: Koh Jun Jie")
        self.clabel.pack(side=BOTTOM)

    #Hashing Functions
    def md5(self):
        file_hash=hashlib.md5()
        with askopenfile(mode='rb',filetypes=[('All files','*.*')]) as f:
            fb=f.read(BLOCK_SIZE)
            while len(fb)>0:
                file_hash.update(fb)
                fb=f.read(BLOCK_SIZE)
        data_string=StringVar()
        data_string.set("MD5 Hash: "+file_hash.hexdigest())
        self.entry=Entry(self.master,textvariable=data_string,fg="black",bg="white",bd=0,width=130,state="readonly",justify="center")
        self.entry.pack()

    def sha1(self):
        file_hash=hashlib.sha1()
        with askopenfile(mode='rb',filetypes=[('All files','*.*')]) as f:
            fb=f.read(BLOCK_SIZE)
            while len(fb)>0:
                file_hash.update(fb)
                fb=f.read(BLOCK_SIZE)
        data_string=StringVar()
        data_string.set("SHA-1 Hash: "+file_hash.hexdigest())
        self.entry=Entry(self.master,textvariable=data_string,fg="black",bg="white",bd=0,width=130,state="readonly",justify="center")
        self.entry.pack()

    def sha256(self):
        file_hash=hashlib.sha256()
        with askopenfile(mode='rb',filetypes=[('All files','*.*')]) as f:
            fb=f.read(BLOCK_SIZE)
            while len(fb)>0:
                file_hash.update(fb)
                fb=f.read(BLOCK_SIZE)
        data_string=StringVar()
        data_string.set("SHA-256 Hash: "+file_hash.hexdigest())
        self.entry=Entry(self.master,textvariable=data_string,fg="black",bg="white",bd=0,width=130,state="readonly",justify="center")
        self.entry.pack()

    def sha512(self):
        file_hash=hashlib.sha512()
        with askopenfile(mode='rb',filetypes=[('All files','*.*')]) as f:
            fb=f.read(BLOCK_SIZE)
            while len(fb)>0:
                file_hash.update(fb)
                fb=f.read(BLOCK_SIZE)
        data_string=StringVar()
        data_string.set("SHA-512 Hash: "+file_hash.hexdigest())
        self.entry=Entry(self.master,textvariable=data_string,fg="black",bg="white",bd=0,width=130,state="readonly",justify="center")
        self.entry.pack()

    #Other Functions
    def quit(self):
        self.master.destroy()

root=Tk()
frame=Frame(root)
app=window(root)
root.mainloop()
