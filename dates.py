import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()

print(year)

date_of_birth = dt.datetime(year=1995, month=12, day=13, hour=4) # from hour there are defaults
date_of_birth = dt.datetime(year=1995, month=12, day=13)
print(date_of_birth)



