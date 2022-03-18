#import datetime as dt

# t = dt.time(4, 32, 15)
# print(t)
# print(t.second)
# print(t.minute)
# print(t.hour)

# d = dt.date(1997, 3, 15)
# print(d)
# print(d.year)
# print(d.month)
# print(d.day)

# print(dt.date.fromtimestamp(24*60*60)) # 1970-01-01 00:00:00
# print(dt.date.today())

# d = dt.datetime(1997, 11, 23, hour=4, minute=32, second=32)
# print(d)
# print(dt.datetime.now())
# print(d.month)
# print(d.timestamp())

# d1 = dt.date(1997, 10, 21)
# d2 = dt.date(2001, 6, 5)

# print(d2-d1)

# now = dt.datetime.now()
# print(now)
# tm = dt.timedelta(weeks=2, days=2, hours=4, minutes=8)
# print(now+tm)
# print(now-tm)

# ### pip install pytz ###
# import pytz

# local = dt.datetime.now()
# new_york = dt.datetime.now(pytz.timezone('America/New_York'))
# Tehran = dt.datetime.now(pytz.timezone('Asia/Tehran'))
# print(local)
# print(new_york)
# print(Tehran)

# ### All Time Zone: 
# for i in pytz.all_timezones:
#     print(i)


import time as tm

# print(tm.gmtime()) # Get the time of now
# print(tm.gmtime(0)) # Get the epoch time
# print(tm.gmtime(200000)) # Get the time of 200_000 s after the epoch time
# print(tm.gmtime(1607514488.4146872))
# print(tm.time()) # good for save in database but not good for show to user!
# print(tm.ctime())
# print('hello')
# tm.sleep(2)
# print('world')

# value = tm.strftime('%a %A/%b %B %y-%Y------%d-%m-%y----- %H:%M:%S %p') # Check the Document's
# print(value)

# print('hello world')

# print(tm.perf_counter()) #Users
# print(tm.process_time()) #CPU

# per_start = tm.perf_counter()
# pc_start = tm.process_time()

# a = 0
# for i in range(100000000):
#     a += 1

# per_end = tm.perf_counter()
# pc_end = tm.process_time()

# print(f'Per_Counter => {per_end - per_start}')
# print(f'Process => {pc_end - pc_start}')


per_start = tm.perf_counter()
pc_start = tm.process_time()

tm.sleep(5)
print('hello')
per_end = tm.perf_counter()
pc_end = tm.process_time()

print(f'Per_Counter => {per_end - per_start}') # 5.0 beccuse user patience(wait) for show "hello"
print(f'Process => {pc_end - pc_start}') # 0.0 because cpu not working in this code
