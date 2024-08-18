from datetime import date
from datetime import time
from datetime import datetime, timedelta

my_date = date(2100, 4, 10)

print(my_date)

print(my_date.day)
print(my_date.month)
print(my_date.year)
print(my_date.max)

print(my_date.isocalendar())

my_time = time(15, 33, 45)

print(my_time)
print(my_time.hour)
print(my_time.minute)
print(my_time.second)

my_datetime = datetime(2222, 4, 22, 18, 10, 45)

print(type(my_datetime))

print(my_datetime.year)
print(my_datetime.month)
print(my_datetime.day)
print(my_datetime.date)
print(my_datetime.hour)
print(my_datetime.minute)


print(my_datetime.isocalendar())
print(my_datetime.now())

print(my_datetime.strftime('%d-%b-%y'))
print(my_datetime.strftime('%d-%m-%y'))
print(my_datetime.strftime('%d/%m/%y'))
print(my_datetime.strftime('%d-%b-%y %H:%M:%S'))

date_str = '10/12/2222'

converted_date = datetime.strptime(date_str, '%d/%m/%Y')

print(converted_date)

print(timedelta)
print(converted_date + timedelta(days=100, minutes=125))
print(converted_date + timedelta(days=100, hours=5))
print(converted_date - timedelta(days=100, hours=5))
