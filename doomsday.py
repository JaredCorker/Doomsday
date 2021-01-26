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
    if re.match(r"^(\d{2}\/){2}\d{4}$", date) != None:
        pass
    else:
        return False

def calculate_doomsday(day, month, year):
    century_code = int(str(year)[0:2])  
    if (century_code - 18) % 4 == 0:
	    century_code = 5
    elif (century_code - 19) % 4 == 0:
	    century_code = 3
    elif (century_code - 20) % 4 == 0:
	    century_code = 2
    else:
	    century_code = 0


    year_no_century = int(str(year)[2:])
    year_code = year_no_century  // 12
    year_modulo = year_no_century % 12
    final_num = year_modulo // 4
    final_num = final_num % 7
    doomsday = (century_code + year_code + year_modulo + final_num) % 7

    if month == 1:
        print(days_of_week[doomsday - ((3 - day) % 7)])

calculate_doomsday(31, 1, 2021)