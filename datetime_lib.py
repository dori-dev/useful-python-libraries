"""datetime library
"""
import datetime as dt
import pytz
# pip install pytz

# time
time = dt.time(4, 32, 15)
print(time)
print(time.second)
print(time.minute)
print(time.hour)

# date
date = dt.date(1997, 3, 15)
print(date)
print(date.year)
print(date.month)
print(date.day)

# time-stamp: 1970-01-01 00:00:00
ONE_DAY = 24*60*60
print(dt.date.fromtimestamp(ONE_DAY*20))
print(dt.date.today())

# custom date
date = dt.datetime(1997, 11, 23, hour=4, minute=32, second=32)
print(date)
print(date.timestamp())

# time calculating
date1 = dt.date(1997, 10, 21)
date2 = dt.date(2001, 6, 5)
print(date2-date1)

# time delta
now = dt.datetime.now()
print(now)
custom_time = dt.timedelta(weeks=2, days=2, hours=4, minutes=8)
print(now+custom_time)
print(now-custom_time)

# use timezone
local = dt.datetime.now()
new_york = dt.datetime.now(pytz.timezone('America/New_York'))
Tehran = dt.datetime.now(pytz.timezone('Asia/Tehran'))
print(local)
print(new_york)
print(Tehran)

# all timezones
print(pytz.all_timezones)
