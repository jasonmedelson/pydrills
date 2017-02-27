from datetime import *


def isOpen():
    port_time =  datetime.now().timetuple()
    #0=year;1=month;2=day;3=hour;4=min;5=sec;
    port_time = (port_time[3],port_time[4],port_time[5])
    ny_diff = 3
    lon_diff = 8
    if port_time[0] >=21:
        ny_time = (port_time[0]-21,port_time[1],port_time[2])
    else:
        ny_time = (port_time[0]+ny_diff,port_time[1],port_time[2])
    if port_time[0] >=16:
        lon_time = (port_time[0]-16,port_time[1],port_time[2])
    else:
        lon_time = (port_time[0]+lon_diff,port_time[1],port_time[2])
    if ny_time[0]> 8 and ny_time[0]<21:
        print ("New York Branch is: OPEN")
    else:
        print ("New York Branch is: CLOSED")
    if lon_time[0]> 8 and lon_time[0]<21:
        print ("London Branch is: OPEN")
    else:
        print ("London Branch is: CLOSED")
isOpen()
