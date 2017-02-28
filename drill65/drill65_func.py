import shutil
import glob
import os
from datetime import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk

import drill65_gui
import drill65_main

def select_source(self):
    src_folder = filedialog.askdirectory()
    self.txt_srctag.config(text = src_folder)

def select_dest(self):
    dest_folder = filedialog.askdirectory()
    self.txt_desttag.config(text = dest_folder)

def clear(self):
    self.txt_srctag.config(text="")
    self.txt_desttag.config(text="")

def backup(self):
    src = self.txt_srctag['text']
    dest = self.txt_desttag['text']
    if(len(src) == 0 or len(dest)==0):
        messagebox.showerror(title='Error', message = 'Source or Destination folder not selected')
    else:
        src = src+ r"\*.txt"
        files= glob.glob(src)
        current_date = datetime.now().timetuple()
        current_date = (current_date[2],current_date[3],current_date[4],current_date[5])
        #day =0,hour =1,min=2,sec=3
        current_time = (current_date[1]*10000)+(current_date[2]*100)+(current_date[3])
        #current time in single int
        for name in files:
            text = name
            stat = os.path.getmtime(text)
            times = datetime.fromtimestamp(stat).strftime('%Y-%m-%d %H:%M:%S') # format time
            mod_day = int(times[8:10])
            hour = int(times[11:13])
            minute = int(times[14:16])
            sec = int(times[17:19])
            mod_time = (hour*10000)+(minute*100)+(sec) #modified time in single int
            if (mod_day == (current_date[0]-1)): #if modification date = yesterday, possible for <24hours 
                if (current_time < mod_time):#if current time<modtime, file <24hours
                    shutil.copy(name,dest)
                    print ("{}, has been copied".format(name))
            elif(mod_day == current_date[0]):#if same day, file<24hours
                shutil.copy(name,dest)
                print ("{}, has been copied".format(name))
            else:
                print ("{}, file not recent enough".format(name))
          
    
if __name__ == "__main__":
    pass
