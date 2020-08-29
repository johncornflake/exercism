from datetime import date, timedelta
import calendar as cal
from collections import deque

class MeetupDayException(Exception):
    pass

def meetup(year, month, week, day_of_week):
    ordinal = ['1st', '2nd', '3rd', '4th', '5th']
    first_date = date(year, month, 1)
    first_day = date(year, month, 1).weekday()
    days_of_week = deque(cal.day_name)
    days_of_week.rotate(first_day * -1)
    start_date = first_date + timedelta(days=days_of_week.index(day_of_week))

    if week == 'first':
        return start_date

    elif week in ordinal:
        res = start_date + timedelta(days=ordinal.index(week)*7)

    elif week == 'teenth':
        res = start_date
        while res.day not in range(13,20):
            res = res + timedelta(days=7)

    elif week == 'last':
        res = start_date
        while (res + timedelta(days=7)).month == month:
            res = res + timedelta(days=7)

    if res.month != month:
        raise MeetupDayException('that date does not exist')

    return res
