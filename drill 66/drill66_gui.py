import shutil
import glob
import os
from datetime import *
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import sqlite3

import drill66_func
import drill66_main


def load_gui(self):
    self.lbl_srctag = tk.Label(self.master,text='Source:')
    self.lbl_srctag.grid(row=0,column=0,columnspan=1,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_desttag = tk.Label(self.master,text='Destination:')
    self.lbl_desttag.grid(row=1,column=0,columnspan=1,padx=(27,0),pady=(10,0),sticky=N+W)
    self.txt_srctag = tk.Label(self.master,text='', bg="#FFFFFF", borderwidth = '2px',width='50')
    self.txt_srctag.grid(row=0,column=2,rowspan=1,columnspan=3,padx=(30,40),pady=(10,0),sticky=N+E)
    self.txt_desttag = tk.Label(self.master,text='', bg="#FFFFFF",bd = '2px',width='50')
    self.txt_desttag.grid(row=1,column=2,rowspan=1,columnspan=3,padx=(30,40),pady=(10,0),sticky=N+E)
    self.btn_srctag = tk.Button(self.master,text="Choose Source",command =lambda: drill66_func.select_source(self))
    self.btn_srctag.grid(row=0,column=5,rowspan=1,columnspan=2,padx=(30,40),pady=(10,0),sticky=N+E)
    
    self.btn_desttag = tk.Button(self.master,text="Choose Destination",command =lambda: drill66_func.select_dest(self))
    self.btn_desttag.grid(row=1,column=5,rowspan=1,columnspan=2,padx=(30,40),pady=(10,0),sticky=N+E)
    
    self.btn_submit = tk.Button(self.master, text = "BACKUP",height = '4',width = '18',bd='3px',command =lambda: drill66_func.backup(self))
    self.btn_submit.grid(row = 3, column = 2,rowspan=2,columnspan=2,padx=(30,40),pady=(25,0),sticky=N+W)
    self.btn_submit = tk.Button(self.master, text = "CANCEL",height = '4',width = '15',bd='3px',command =lambda: drill66_func.clear(self))
    self.btn_submit.grid(row = 3, column = 4,rowspan=2,columnspan=2,padx=(30,40),pady=(25,0),sticky=N+W)

    self.lbl_datetag = tk.Label(self.master,text='Last Backup:')
    self.lbl_datetag.grid(row=5,column=0,columnspan=1,padx=(27,0),pady=(10,0),sticky=N+W)
    self.txt_datetag = tk.Label(self.master,text='', bg="#FFFFFF", borderwidth = '2px',width='50')
    self.txt_datetag.grid(row=5,column=2,rowspan=1,columnspan=3,padx=(30,40),pady=(10,0),sticky=N+E)

    drill66_func.create_db(self)

if __name__ == "__main__":
    pass
