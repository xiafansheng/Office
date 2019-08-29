import time
import datetime
#秒进制转格式
def nowtime(t = time.time()): #t = time.time()
    year = time.localtime(t).tm_year
    month = time.localtime(t).tm_mon
    day = time.localtime(t).tm_mday
    hour = time.localtime(t).tm_hour
    min = time.localtime(t).tm_min
    sec = time.localtime(t).tm_sec
    week = time.asctime(time.localtime(t)).split(' ')[0]
    #return [year,month,day,hour,min,sec,week]
    date = str(year)+ '-'+ str(month)+ '-'+str(day)
    return date





