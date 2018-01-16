# python time and date
import time
import datetime
import calendar

# time
print(time.time())  # get all the seconds since 1970-01-01 12:00:00
print(time.clock())  # get CPU time
print(time.localtime())
print(time.localtime(time.time()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # format date
print(time.asctime(time.localtime()))
print(time.asctime(time.localtime(time.time())))

# datetime
# --1
starttime = datetime.datetime.now()
time.sleep(1)  # sleep for 1s
endtime = datetime.datetime.now()
print((endtime - starttime).seconds, "s")

# --2
startday = datetime.datetime.now()
endday = startday + datetime.timedelta(days=3)
print(endday)
print(str(endday))
print(endday.ctime())

# --3
t = datetime.datetime.now()
y = t.year
print("year=", y)

m = t.month
print("month=", m)

minu = t.minute
print("minute", minu)

s = t.second
print("second=", s)

ms = t.microsecond
print("microsecond=", ms)

# calendar
print("calendar:\n", calendar.calendar(2017))  # calendar of 2017
print("calendar:\n", calendar.month(2017, 12))  # calendar of 2017 12
print("monthcalendar:\n", calendar.monthcalendar(2017, 12))  # return calendar of 2017 12 in int[]
print("weekday: ", calendar.firstweekday())  # get the start day of a week
print("weekday: ", calendar.weekday(2017, 12, 31))  # return the weekday of a day
print(calendar.isleap(2017))  # is leap year or not

# compute the time of a loop
start = time.clock()
i = 0
while i < 10000:
    i += 0.01
end = time.clock()
print("Time:", (end-start))
