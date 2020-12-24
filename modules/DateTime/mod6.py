import time
import datetime
import calendar

localtime = time.localtime(time.time())
print("loacal current time :" , localtime)

time.sleep(4)


localtimes = time.asctime(time.localtime(time.time()))
print("\n loacal current time :" , localtimes)



datet = datetime.datetime.now()

print("\n loacal current time :" , datet)


print("\n loacal current time :" , datet.strftime("%H:%M:%S"))


print("\n days",calendar.month( 2020,12))
