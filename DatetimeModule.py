from datetime import datetime, date, time
import time as time_module


# datetime.now()
now = datetime.now()

print("Current datetime:")
print(now)


# Access datetime attributes
print("\nYear:")
print(now.year)

print("\nMonth:")
print(now.month)

print("\nDay:")
print(now.day)

print("\nHour:")
print(now.hour)

print("\nMinute:")
print(now.minute)

print("\nSecond:")
print(now.second)

print("\nMicrosecond:")
print(now.microsecond)


# datetime.strptime()
date_string = "05:15:00 AM 23 October, 1996"

converted_date = datetime.strptime(
    date_string,
    "%I:%M:%S %p %d %B, %Y"
)

print("\nConverted datetime:")
print(converted_date)


# datetime.replace()
new_date = now.replace(
    year=1996,
    month=10,
    day=23,
    hour=5,
    minute=15
)

print("\nReplaced datetime:")
print(new_date)


# datetime.strftime()
formatted_date = now.strftime(
    "%I:%M:%S %p %d %B, %Y"
)

print("\nFormatted datetime:")
print(formatted_date)


# datetime.combine()
my_date = date(1994, 10, 23)
my_time = time(5, 15, 0)

combined_datetime = datetime.combine(my_date, my_time)

print("\nCombined datetime:")
print(combined_datetime)


# time.gmtime()
utc_time = time_module.gmtime()

print("\nUTC time:")
print(utc_time)


# time.localtime()
local_time = time_module.localtime()

print("\nLocal time:")
print(local_time)


# time.strptime()
time_string = "30 Nov 00"

converted_time = time_module.strptime(
    time_string,
    "%d %b %y"
)

print("\nConverted time:")
print(converted_time)


# time.struct_time
print("\nYear:")
print(local_time.tm_year)

print("\nMonth:")
print(local_time.tm_mon)

print("\nDay:")
print(local_time.tm_mday)

print("\nYear using index:")
print(local_time[0])

print("\nMonth using index:")
print(local_time[1])

print("\nDay using index:")
print(local_time[2])


# time.time()
start = time_module.time()

count = 0

while count <= 1000:
    count += 1

stop = time_module.time()

print("\nComputational cost:")
print(stop - start)


# time.sleep()
start = time_module.time()

time_module.sleep(3)

stop = time_module.time()

print("\nSleep duration:")
print(stop - start)


# time.strftime()
formatted_time = time_module.strftime(
    "%I:%M:%S %p %d %B, %Y",
    local_time
)

print("\nFormatted time:")
print(formatted_time)


# time.strptime()
converted_time = time_module.strptime(
    "04:57:21 PM 09 February, 2018",
    "%I:%M:%S %p %d %B, %Y"
)

print("\nConverted time:")
print(converted_time)