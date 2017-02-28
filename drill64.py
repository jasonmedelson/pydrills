import shutil
import glob
import os
from datetime import *

files = glob.glob('C:\Users\Jason\Desktop\Folder A\*.txt')#name of all files in A
current_date = datetime.now().timetuple()
current_date = (current_date[2],current_date[3],current_date[4],current_date[5])
#day =0,hour =1,min=2,sec=3
current_time = (current_date[1]*10000)+(current_date[2]*100)+(current_date[3])
for name in files:
    text = name
    stat = os.path.getmtime(text)
    times = datetime.fromtimestamp(stat).strftime('%Y-%m-%d %H:%M:%S')
    day = int(times[8:10])
    hour = int(times[11:13])
    minute = int(times[14:16])
    sec = int(times[17:19])
    mod_time = (hour*10000)+(minute*100)+(sec)
    if (day == (current_date[0]-1)):
        if (current_time < mod_time):
            shutil.copy(name,'C:\Users\Jason\Desktop\Folder B')
            print name
    elif(day == current_date[0]):
        shutil.copy(name,'C:\Users\Jason\Desktop\Folder B')
        print name
    else:
        print ("file not recent enough")



