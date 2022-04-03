# -*- coding: utf-8 -*-

__author__ = "venkat"
__author_email__ = "venkatram0273@gmail.com"


# from datetime import datetime, timedelta, timezone
# from dateutil import parser

# dt = datetime.strptime("2022-04-03 07:56:25", "%Y-%m-%d %H:%M:%S")

# dt = parser.parse("2016-04-15T08:27:18-0500")

# print(dt)
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.hour)
# print(dt.minute)
# print(dt.second)

# JST = timezone(timedelta(hours=+5, minutes=+30))

# dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)

# print(dt)
# print(dt.tzname())
# print(dt.ctime())
# print(dt.hour)

# now = datetime.now()
# then = datetime.strptime("2020-01-01", "%Y-%m-%d")

# delta: timedelta = now - then
# print(delta.days)
# print(delta.seconds)

# addition: timedelta = timedelta(days=9)
# print(datetime.now() - addition)

# subtraction: timedelta = timedelta(days=-9)
# print(datetime.now() - subtraction)

import datetime


# today: datetime.date = datetime.date.today()

# today_new: datetime.date = datetime.date(2020, 1, 1)
# print(today)
# print(today_new)

# noon: datetime.time = datetime.time(12, 00, 00)
# print(noon)

# now: datetime.datetime = datetime.datetime.now()
# print(now)

# date_time: datetime.datetime = datetime.datetime(2020, 1, 2, 0, 0, 0)
# print(datetime.datetime.strftime(date_time, "%A %B %Y"))

# combined: datetime.datetime = datetime.datetime.combine(today, noon)
# print(combined)

# dt = datetime.datetime.today()

# day_delta = datetime.timedelta(days=1)

# start_date = datetime.date.today()
# end_date = start_date + 7*day_delta

# for i in range((end_date - start_date).days):
#     print(start_date + i*day_delta)
