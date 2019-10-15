import time
import calendar
ticks = time.time()
print ticks
#getting current time
localtime = time.asctime(time.localtime(time.time()))
print localtime
#playing with calender module
calendar = calendar.month(2019,10)
print calendar