from random import randint
import re

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def calculate_date():
    year = randint(1000, 9999)
    month = randint(1, 12)
    if month == 2:
        if is_leap_year(year):
            date = randint(1, 29)
        else:
            date = randint(1, 28)
    elif month in {4, 6, 9, 11}:
        date = randint(1, 30)
    else:
        date = randint(1, 31)

def is_valid_date(date):
    if re.match("^(\d{2}\/){2}\d{4}$", date) != None:
        pass
    else:
        return False