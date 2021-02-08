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

        self.century_code = calculate_century_code()

    def calculate_century_code(self):
        century = int(str(year)[0:2])  
        if (century - 18) % 4 == 0:
	        return 5
        elif (century - 19) % 4 == 0:
	        return 3
        elif (century - 20) % 4 == 0:
	        return 2
        else:
	        return 0

    def calculate_doomsday(self):
        # Get the last two digits of the year i.e., '69 or '04
        last_two_digits_year = int(str(self.year)[2:])
        # See how many times 12 goes into the year i.e., 74 // 12 = 6
        first_num = last_two_digits_year // 12
        # Get the remainder from the above calculation i.e., 74 % 12 = 2
        second_num = last_two_digits_year % 12
        # See how many times 4 goes into the remainder calculated in the last step i.e., 2 % 4 = 0
        third_num = second_num // 4
        # Add these 3 numbers together with the century code and modulus by 7 to get the day of the week
        #   will return a number from 0 to 6 (sunday to saturday)
        doomsday = (self.century_code + first_num + second_num + third_num) % 7

        # Check the anchor day for each month (every month has a date that will be the same day of the week as all other anchor days that year)
        # i.e., the Doomsday for 2021 is Sunday, so the 8th of August, the 11th of September and the 10th of October will all be Sundays and so on.
        # This helps to quickly find an "anchor" in each month and then you can quickly count up or down to the actual date in your head

        # January is the 3rd (4th if leap year)
        if self.month == 1:
            if isleap(year):
                doomsday_anchor = 4 
            else:
                doomsday_anchor = 3 
        # February is the 28th (29th if leap year)
        if self.month == 2:
            if isleap(year):
                doomsday_anchor = 29 
            else:
                doomsday_anchor = 28
        #March is the 14th 
        if self.month == 3:
            doomsday_anchor = 14
        # April is the 4th 
        if self.month == 4:
            doomsday_anchor = 4 
        # May is the 9th
        if self.month == 5:
            doomsday_anchor = 9 
        # June is the 6th
        if self.month == 6:
            doomsday_anchor = 6 
        # July is the 11th
        if self.month == 7:
            doomsday_anchor = 11 
        # August is the 8th
        if self.month == 8:
            doomsday_anchor = 8 
        # September is the 9th
        if self.month == 9:
            doomsday_anchor = 5 
        # October is the 10th
        if self.month == 10:
            doomsday_anchor = 10
        # November is the 7th
        if self.month == 11:
            doomsday_anchor = 7 
        # December is the 12th
        if self.month == 12:
            doomsday_anchor = 12 

        # Calculate the difference between the given day and the anchor day of that month and modulus it by 7
        #   then subtract this from the doomsday and return the day of the week
        #   i.e., 03/03/2021 doomsday is Sunday so 14th of March is Sunday
        #       14 - 3 = 11, 11 % 7 = 4 so the the day of the week is 4 days before Sunday (Wednesday)
        return days_of_week[doomsday - ((doomsday_anchor - self.day) % 7)]

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
