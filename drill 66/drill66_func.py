import shutil
import glob
import os
from datetime import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import sqlite3

import drill66_gui
import drill66_main

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
        backup_date_str = (str(current_date[1]) +'/'+str(current_date[2])+'/'+str(current_date[0])+'  '+str(current_date[3])+':'+str(current_date[4])+':'+str(current_date[5]))#string for displaying
        backup_date_int = ((current_date[0]*10000000000)+(current_date[1]*100000000)+(current_date[2]*1000000)+(current_date[3]*10000)+(current_date[4]*100)+(current_date[5]))#year*month*day format
        last_backup = str(get_backup_int())
        if (len(last_backup)==14):#if month is oct,nov,dec, length will be 14
            last_date = int(last_backup[:8])
            last_time = int(last_backup[8:])
        elif(len(last_backup)==13):#all other months length is 13
            last_date = int(last_backup[:7])
            last_time = int(last_backup[7:])
        #current time in single int
        for name in files:
            text = name
            stat = os.path.getmtime(text)
            times = datetime.fromtimestamp(stat).strftime('%Y-%m-%d %H:%M:%S') # format time
            mod_date = ((int(times[:4])*10000)+(int(times[5:7])*100)+(int(times[8:10])))#year*month*day
            mod_time = ((int(times[11:13])*10000)+(int(times[14:16])*100)+(int(times[17:])))#hour.min.second
            anyfilesmoved = false
            if (mod_date > last_date): #larger mod date means file changed since last backup 
                    shutil.copy(name,dest)
                    print ("{}, has been copied".format(name))
                    anyfilesmoved = True
            elif(mod_date == last_date):#if same day, need to compare time
                if(mod_time>last_time):#change happend same day as back up but later time
                    shutil.copy(name,dest)
                    print ("{}, has been copied".format(name))
                    anyfilesmoved = True
                else:
                    print ("{}, file has not changed since last backup".format(name))#same day, but before
            else:
                print ("{}, file has not changed since last backup".format(name))#earlier day
        #print(backup_date_str)
        #print(backup_date_int)
        if (anyfilesed):
            messagebox.showinfo('Transfer Completed', 'Success!')
        else:
            messagebox.showinfo('Nothing To Transfer', 'No files have been created or modified'
                                        '\nsince the last file backup.')
        update_backup(backup_date_str,backup_date_int)
        display_date(self)

def create_db(self):
    conn = sqlite3.connect('db_drill66.db')
    with conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_backupdate(Id INT,Date_str TEXT,Date_int INT)")
        conn.commit()
    conn.close()
    first_run(self)
    display_date(self)

def first_run(self):
    conn =  sqlite3.connect('db_drill66.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_backupdate(Id,Date_str,Date_int)
                        VALUES(?,?,?)""", (1,'NEVER',1111111111111))
            conn.commit()
    conn.close()
        
def count_records(cur):
    count =""
    cur.execute("""SELECT COUNT(*) from tbl_backupdate""")
    count = cur.fetchone()[0]
    return cur,count

def update_backup(date_str,date_int):
    conn =  sqlite3.connect('db_drill66.db')
    with conn:
        cur = conn.cursor()
        cur.execute("UPDATE tbl_backupdate SET Date_str=? WHERE Id=1",(date_str,))
        cur.execute("UPDATE tbl_backupdate SET Date_int=? WHERE Id=1",(date_int,))
        conn.commit()            
    conn.close()

def display_date(self):
    conn =  sqlite3.connect('db_drill66.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT Date_str FROM tbl_backupdate WHERE Id == 1")
        row =cur.fetchone()
        self.txt_datetag.config(text = row)
        conn.commit()            
    conn.close()

def get_backup_int():
    conn =  sqlite3.connect('db_drill66.db')
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT Date_int FROM tbl_backupdate WHERE Id == 1")
        row =cur.fetchone()
        conn.commit()
    conn.close()
    return row[0]

if __name__ == "__main__":
    pass
