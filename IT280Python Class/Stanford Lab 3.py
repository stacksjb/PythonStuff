#Lab Assignment 2.4 Lab #3 For IT280 Jesse Stanford "Selection of Mathematical Functions"
import math

def main():
    #Main Menu Loop
    while True:
        #Prompt for Option
        print ('Welcome to Selection of Mathematical Functions \n')
        print('Please pick an option (1-6) \n 1. Area of Circle \n 2. Vehicle Miles per Gallon \n 3. Work Week Hours \n 4. Debt to Income  \n 5. Compound Interest Savings \n 6. Exit')
        #Use integer_input function to collect input
        option = integer_input()
        #Match on option specified
        match option:
            case 1:
                area_of_circle()
            case 2:
                vehicle_mpg()
            case 3:
                work_hours()
            case 4:
                debt_to_income()
            case 5:
                compound_interest()
            case 6:
                print ("Thank you for playing!")
                exit()
            case _:
                print('You entered an invalid number, try again.')

#Common integer input function for entering integers
def integer_input():
    while True:
        try:
            num1 = int(input())
        except ValueError:
            print('You have entered an invalid number, try again.')
            continue
        return num1

def area_of_circle():
#Code for area of circle
    print('You have selected Area of Circle')
    print('Please enter the radius of the circle')
    radius = integer_input()
    #Calculate piRsquared
    print("The area of the circle is: " + str(math.pi * radius**2) + "\n")

def vehicle_mpg():
#Code for miles driven
    print('You have selected Vehicle Miles per Gallon')
    print('Please enter the miles driven')
    miles = integer_input()
    print('Please enter the gallons used')
    gallons = integer_input()
    #Calculate MPG
    print('The miles per gallon is: ' + str(miles/gallons)+ "\n")

def work_hours():
#Code for hours worked
    print('You have selected Work Week Hours')
    print('Please enter the hours worked')
    hours = integer_input()
    #Calculate hours worked
    print('The Number of Hours worked in a 5 day work week is: ' + str(hours*5)+ "\n")

def debt_to_income():
#Code for debt_to_income calculation
    print('You have selected Debt to Income')
    print('Please enter your annual income')
    income = integer_input()
    print('Please enter your monthly debt payments')
    debt = integer_input()
    #Calculate debt to income
    print('Your debt to income ratio is ', end='')
    print(f"{(debt*12/income):.0%}")
    print("\n")

def compound_interest():
#Code for compound interest calculation
    print('You have selected Compound Interest Savings')
    print('Please enter your starting amount')
    start_amount = integer_input()
    print('Please enter your annual APR interest rate')
    apr = integer_input()
    print('Please enter the number of years you will be saving')
    years = integer_input()
    #calculate compound interest
    ci = start_amount * (pow((1 + apr/100), years))
    print('Your total savings amount with compound interest will be $', end='')
    print(f"{(ci):.2f}")
    print("\n")

if __name__ == "__main__":
    main()