"""calendar library
"""
import calendar

print(calendar.month(2022, 4))
print(calendar.calendar(2022))
print(calendar.isleap(2022))  # False
print(calendar.isleap(2020))  # True
print(calendar.leapdays(2000, 2022))
print(calendar.monthcalendar(2022, 3))

html_calendar = calendar.HTMLCalendar()
codes = ""
for month in range(1, 13):
    month_code = html_calendar.formatmonth(2022, month)
    codes += month_code
    codes += "<br>"

with open("2022.html", 'w') as html:
    html.write(codes)
