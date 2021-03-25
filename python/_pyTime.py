'''
Created by Khalid Hussain
Date created: 25 March 2021
'''

import sys
from datetime import datetime, timezone
from hijri_converter import convert

# Current date and time
utc_now = datetime.now(timezone.utc)
utc_now_tz = utc_now.astimezone()
dt_string = utc_now_tz.strftime("(%I:%M:%S %p %z)")

# Convert today to hijri date
todayHijri = convert.Gregorian.today().to_hijri()

# Hijri date components
theDate = todayHijri.datetuple()[2]
theDay = todayHijri.day_name('en')
theMonth = todayHijri.month_name('en')
theYear = todayHijri.year

# Hijri date components concatenation
theHijriDate = f'{theDay}, {theDate} {theMonth}, {theYear}'

# Date and time concatenation
theHijriDateAndTime = theHijriDate + ' ' + dt_string

# Print as UTF-8 encoded string
# https://stackoverflow.com/questions/3597480/how-to-make-python-3-print-utf8/3603160#3603160
sys.stdout.buffer.write((theHijriDateAndTime).encode('utf-8'))
