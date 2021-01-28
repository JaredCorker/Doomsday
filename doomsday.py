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

def get_user_date():
    date = input("Enter date (dd/mm/yyyy): ")
    date = date.split('/')
    date = [int(x) for x in date]
    return date

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
        if is_leap_year(year):
            print(days_of_week[doomsday - ((4 - day) % 7)])
        else:
            print(days_of_week[doomsday - ((3 - day) % 7)])
    if month == 2:
        if is_leap_year(year):
            print(days_of_week[doomsday - ((29 - day) % 7)])
        else:
            print(days_of_week[doomsday - ((28 - day) % 7)])
    if month == 3:
        print(days_of_week[doomsday - ((14 - day) % 7)])
    if month == 4:
        print(days_of_week[doomsday - ((4 - day) % 7)])
    if month == 5:
        print(days_of_week[doomsday - ((9 - day) % 7)])
    if month == 6:
        print(days_of_week[doomsday - ((6 - day) % 7)])
    if month == 7:
        print(days_of_week[doomsday - ((11 - day) % 7)])
    if month == 8:
        print(days_of_week[doomsday - ((8 - day) % 7)])
    if month == 9:
        print(days_of_week[doomsday - ((11 - day) % 7)])
    if month == 10:
        print(days_of_week[doomsday - ((10 - day) % 7)])
    if month == 11:
        print(days_of_week[doomsday - ((7 - day) % 7)])
    if month == 12:
        print(days_of_week[doomsday - ((12 - day) % 7)])

if __name__ == '__main__':
    calculate_doomsday(*get_user_date())