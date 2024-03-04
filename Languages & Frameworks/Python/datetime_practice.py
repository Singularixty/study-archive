import time
import datetime

current_date = datetime.datetime.now()
current_day = str(current_date.day)
current_month = str(current_date.month)
current_year = str(current_date.year)
current_microsecond = str(current_date.microsecond)
print("-".join([current_day, current_month, current_year]))
