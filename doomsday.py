from random import randint
import re
import time
from calendar import isleap

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

class Doomsday():
    def __init__(self, day=None, month=None, year=None):
        self.year = year if year is not None else randint(1000, 2999)

        self.month = month if month is not None else randint(1, 12)

        if day != None:
            self.day = day
        else:
            if month == 2:
                if isleap(self.year):
                    self.day = randint(1, 29)
                else:
                    self.day = randint(1, 28)
            elif month in {4, 6, 9, 11}:
                self.day = randint(1, 30)
            else:
                self.day = randint(1, 31)

        century = int(str(year)[0:2])  
        if (century - 18) % 4 == 0:
	        self.century_code = 5
        elif (century - 19) % 4 == 0:
	        self.century_code = 3
        elif (century - 20) % 4 == 0:
	        self.century_code = 2
        else:
	        self.century_code = 0


def is_valid_date(date):
    if re.match(r"^(\d{2}\/){2}\d{4}$", date) != None:
        date = date.split('/')
        day, month, year = [int(x) for x in date]
        if month == 2:
            if isleap(year):
                return 1 <= day <= 29 
            else:
                return 1 <= day <= 28 
        elif month in {4, 6, 9, 11}:
            return 1 <= day <= 30 
        else:
            return 1 <= day <= 31
    else:
        return False

def get_user_date():
    date = input("Enter date (dd/mm/yyyy): ")
    if is_valid_date(date):
        date = date.split('/')
        date = [int(x) for x in date]
        return date
    else:
        print("Not a valid date.")

def calculate_doomsday(day, month, year):
    century_code = calculate_century_code(year)
    year_no_century = int(str(year)[2:])
    year_code = year_no_century  // 12
    year_modulo = year_no_century % 12
    final_num = year_modulo // 4
    final_num = final_num % 7
    doomsday = (century_code + year_code + year_modulo + final_num) % 7

    if month == 1:
        if isleap(year):
            doomsday_anchor = 4 
        else:
            doomsday_anchor = 3 
    if month == 2:
        if isleap(year):
            doomsday_anchor = 29 
        else:
            doomsday_anchor = 28
    if month == 3:
        doomsday_anchor = 14 
    if month == 4:
        doomsday_anchor = 4 
    if month == 5:
        doomsday_anchor = 9 
    if month == 6:
        doomsday_anchor = 6 
    if month == 7:
        doomsday_anchor = 11 
    if month == 8:
        doomsday_anchor = 8 
    if month == 9:
        doomsday_anchor = 11 
    if month == 10:
        doomsday_anchor = 10 
    if month == 11:
        doomsday_anchor = 7 
    if month == 12:
        doomsday_anchor = 12 
    
    #print(days_of_week[doomsday - ((doomsday_anchor - day) % 7)])
    return days_of_week[doomsday - ((doomsday_anchor - day) % 7)]

if __name__ == '__main__':
    user_choice = input("1) Find out day 2) Test: ")
    if user_choice == "1":
        calculate_doomsday(*get_user_date())
    if user_choice == "2":
        date = calculate_date()
        date = date.split('/')
        date = [int(x) for x in date]
        doomsday = calculate_doomsday(*date)
        print(date)
        start = time.time()
        user_guess = input()
        end = time.time()
        if user_guess == doomsday:
            print("correct!")
        else:
            print("wrong!")
            print("the day was " + doomsday)
        print("time: " + str(end - start))
