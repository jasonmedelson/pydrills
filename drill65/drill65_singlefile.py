import shutil
import glob
import os
from datetime import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(700,200) #(width, height)
        self.master.maxsize(700,200)
        self.master.title("Drill 65")
        self.master.configure(bg="#F0F0F0")
        arg = self.master
        load_gui(self)
        
def load_gui(self):
    self.lbl_srctag = tk.Label(self.master,text='Source:')
    self.lbl_srctag.grid(row=0,column=0,columnspan=1,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_desttag = tk.Label(self.master,text='Destination:')
    self.lbl_desttag.grid(row=1,column=0,columnspan=1,padx=(27,0),pady=(10,0),sticky=N+W)
    self.txt_srctag = tk.Label(self.master,text='', bg="#FFFFFF", borderwidth = '2px',width='50')
    self.txt_srctag.grid(row=0,column=2,rowspan=1,columnspan=3,padx=(30,40),pady=(10,0),sticky=N+E)
    self.txt_desttag = tk.Label(self.master,text='', bg="#FFFFFF",bd = '2px',width='50')
    self.txt_desttag.grid(row=1,column=2,rowspan=1,columnspan=3,padx=(30,40),pady=(10,0),sticky=N+E)
    self.btn_srctag = tk.Button(self.master,text="Choose Source",command =lambda: select_source(self))
    self.btn_srctag.grid(row=0,column=5,rowspan=1,columnspan=2,padx=(30,40),pady=(10,0),sticky=N+E)
    
    self.btn_desttag = tk.Button(self.master,text="Choose Destination",command =lambda: select_dest(self))
    self.btn_desttag.grid(row=1,column=5,rowspan=1,columnspan=2,padx=(30,40),pady=(10,0),sticky=N+E)


    self.btn_submit = tk.Button(self.master, text = "BACKUP",height = '4',width = '18',bd='3px',command =lambda: backup(self))
    self.btn_submit.grid(row = 3, column = 2,rowspan=2,columnspan=2,padx=(30,40),pady=(25,0),sticky=N+W)
    self.btn_submit = tk.Button(self.master, text = "CANCEL",height = '4',width = '15',bd='3px',command =lambda: clear(self))
    self.btn_submit.grid(row = 3, column = 4,rowspan=2,columnspan=2,padx=(30,40),pady=(25,0),sticky=N+W)

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
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
