"""time library
"""
import time

# time now
print(time.gmtime())
# epoch time: 1970-01-01 00:00:00
print(time.gmtime(0))
# time of 200,000 sec after epoch time
print(time.gmtime(200_000))

# current time in sec since the epoch
print(time.time())
# current time
print(time.ctime())

print('Hello')
time.sleep(1)  # 1 second delay
print('World!')

# str format time
custom_date = time.strftime("%A %B %Y, %d-%m-%y %I:%M:%S %p")
print(custom_date)
short_date = time.strftime("%a %b %y, %d/%m %H:%M:%S")
print(short_date)

per_start = time.perf_counter()  # User
pc_start = time.process_time()  # CPU

sum_ = 0
for num in range(10_000_000):
    sum_ += num

per_end = time.perf_counter()
pc_end = time.process_time()

print(f"sum of numbers: {sum_}")
print(f'Performance: {per_end - per_start}')
print(f'Process: {pc_end - pc_start}')


per_start = time.perf_counter()
pc_start = time.process_time()

for num in range(1, 6):
    print(num)
    time.sleep(1)

per_end = time.perf_counter()
pc_end = time.process_time()

# 5 sec, beccuse user wait for show numbers
print(f'Per_Counter => {per_end - per_start}')
# 0 sec, because cpu not working between show numbers
print(f'Process => {pc_end - pc_start}')
