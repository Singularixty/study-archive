import datetime

destination_date = datetime.datetime.fromtimestamp(1715364001)
remaining_days = destination_date - datetime.datetime.now()

print(f'{remaining_days.days} Days until Thailand senate retires.')