from random import randint
import re
import time
from calendar import isleap

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def calculate_doomsday(day, month, year):
    century = int(str(year)[0:2])  
    if (century - 18) % 4 == 0:
        century_code = 5
    elif (century - 19) % 4 == 0:
        century_code = 3
    elif (century - 20) % 4 == 0:
        century_code = 2
    else:
        century_code = 0
     
    # Get the last two digits of the year i.e., '69 or '04
    last_two_digits_year = int(str(year)[2:])
    # See how many times 12 goes into the year i.e., 74 // 12 = 6
    first_num = last_two_digits_year // 12
    # Get the remainder from the above calculation i.e., 74 % 12 = 2
    second_num = last_two_digits_year % 12
    # See how many times 4 goes into the remainder calculated in the last step i.e., 2 % 4 = 0
    third_num = second_num // 4
    # Add these 3 numbers together with the century code and modulus by 7 to get the day of the week
    #   will return a number from 0 to 6 (sunday to saturday)
    doomsday = (century_code + first_num + second_num + third_num) % 7

    # Check the anchor day for each month (every month has a date that will be the same day of the week as all other anchor days that year)
    # i.e., the Doomsday for 2021 is Sunday, so the 8th of August, the 11th of September and the 10th of October will all be Sundays and so on.
    # This helps to quickly find an "anchor" in each month and then you can quickly count up or down to the actual date in your head

    # January is the 3rd (4th if leap year)
    if month == 1:
        if isleap(year):
            doomsday_anchor = 4 
        else:
            doomsday_anchor = 3 
    # February is the 28th (29th if leap year)
    if month == 2:
        if isleap(year):
            doomsday_anchor = 29 
        else:
            doomsday_anchor = 28
    #March is the 14th 
    if month == 3:
        doomsday_anchor = 14
    # April is the 4th 
    if month == 4:
        doomsday_anchor = 4 
    # May is the 9th
    if month == 5:
        doomsday_anchor = 9 
    # June is the 6th
    if month == 6:
        doomsday_anchor = 6 
    # July is the 11th
    if month == 7:
        doomsday_anchor = 11 
    # August is the 8th
    if month == 8:
        doomsday_anchor = 8 
    # September is the 9th
    if month == 9:
        doomsday_anchor = 5 
    # October is the 10th
    if month == 10:
        doomsday_anchor = 10
    # November is the 7th
    if month == 11:
        doomsday_anchor = 7 
    # December is the 12th
    if month == 12:
        doomsday_anchor = 12 

    # Calculate the difference between the given day and the anchor day of that month and modulus it by 7
    #   then subtract this from the doomsday and return the day of the week
    #   i.e., 03/03/2021 doomsday is Sunday so 14th of March is Sunday
    #       14 - 3 = 11, 11 % 7 = 4 so the the day of the week is 4 days before Sunday (Wednesday)
    return days_of_week[doomsday - ((doomsday_anchor - day) % 7)]

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

def generate_random_date():
    year = randint(1000, 2999)
    month = randint(1, 12)
    
    if month == 2:
        if isleap(year):
            day = randint(1, 29)
        else:
            day = randint(1, 28)
    elif month in {4, 6, 9, 11}:
        day = randint(1, 30)
    else:
        day = randint(1, 31)

    return day, month, year

if __name__ == '__main__':
    user_choice = input("1) Find out day 2) Test: ")
    if user_choice == "1":
        calculate_doomsday(*get_user_date())
    if user_choice == "2":
        date = generate_random_date()
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
