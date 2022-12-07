#Lab Assignment 3.3 Lab #4 For IT280 Jesse Stanford List Manipulation lab
import math

def main():
    #Main Menu Loop
    #Prompt for Option
    print ('List Manipulation Lab \n')
    print('Please enter a list of numbers (integers), separated by space')
    #Call input string into list to integers
    
    #Output list
    input_list=int_string_input()
    if input_list == None:
        print('The list is empty. Exiting program.')
        exit()
    else:
        #Remove duplicates
        input_list = list(set(input_list))
        #Sort string
        input_list.sort()
    print('The sorted and deduplicated list is: ' + str(input_list))


#integer input function for entering integers
def int_string_input():
    while True:
        try:
            integer_string = list(map(int, input().split()))
        except ValueError:
            print('You have entered an invalid value that is not an integer, try again.')
            continue
        return integer_string

if __name__ == "__main__":
    main()