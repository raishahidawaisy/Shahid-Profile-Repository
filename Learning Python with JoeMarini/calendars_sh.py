#
# Example file for working with Calendars
#

# import the calendar module
import calendar
from datetime import date

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2020,1)
print(st)

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2019,2)
# print(st)

# loop over the days of a month
# for i in c.itermonthdays(2020,2):
#     print(i)


# zeroes mean that the day of the week is in an overlapping month

  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms

# for name in calendar.month_name:
#     print(name)

# for day in calendar.day_name:
#     print(day)
 

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

for m in range(1,13):
    cal = calendar.monthcalendar(2020,m)
    weekone = cal[0]
    weektwo = cal[1]
    mon_name = calendar.month_name[m]
    # print("First week of ", mon_name, "is: ", weekone)
    # print("Second week of ", mon_name, "is: ", weektwo)

#here the if Friday of first week has value 0, then it belongs to another month
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print("\nMeeting in the month of", mon_name, "will be: %s %d\n" % (calendar.month_name[m], meetday))

