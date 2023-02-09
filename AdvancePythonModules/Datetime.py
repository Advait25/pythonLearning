print('DATETIME')

#import module

import datetime

print('\n Time Objects')   # it will only prit the parameters that are provided, rest are assumed 0 by default
mytime = datetime.time(21,25)

print(mytime)

mytime = datetime.time(21)

print(mytime)

mytime = datetime.time(21,26,30,25)

print(mytime)

print('\nDate object')

today = datetime.date.today()

print(f'today = {today},day = {today.day},month = {today.month},year = {today.year},ctime = {today.ctime()}')

print('\n get date and time')

from datetime import datetime

today_detail = datetime(2022,2,7,21,34,30,5)

print(f"\ntoday's date and time is {today_detail}")

print(f"mistake , current year is 2023, updating..")

today_detail = today_detail.replace(year = 2023)

print(f"updated details - > {today_detail}")


print('\nArithmatic Operations')

from datetime import date

print('Exampl 1.  difference between 2 dates')

date1 = date(2022,8,11)
date2 = date(2022,10,7)
diff = date1-date2
print(f'difference = {diff}') 
print(type(diff))    #the result is in days, and its type is special timedelta object which has its own usefule methods


print('Exampl 2.  difference between 2 datetime objects')

datetime1 = datetime(2022,8,11,20,20)
datetime2 = datetime(2022,10,7,12,20)
diff1 = datetime2 - datetime1
print(f'difference = {diff1}') 
print(type(diff1)) 


