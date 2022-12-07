#Lab Assignment 2.1 For IT280 Jesse Stanford

import random


newgame = True
while (newgame == True):
    print('Hello, welcome to Guessing Game')
    while True:
        try:
            print('Please pick an option (1-5) \n 1. Rock \n 2. Paper \n 3. Scissors \n 4. Lizard \n 5. Spock')
            choice = int(input())
            if 1 <= choice <= 5:
                break
        except ValueError:
            print('You entered an invalid number, try again.')
            continue
    if (choice == 1):
        print('You chose Rock')
    elif (choice == 2):
        print('You chose Paper')
    elif (choice == 3):
        print('You chose Scissors')
    elif (choice == 4):
        print('You chose Lizard')
    elif (choice == 5):
        print('You chose Spock')

    compchoice = random.randint(1,5)
    if (compchoice == 1):
        print('Computer chose Rock')
    elif (compchoice == 2):
        print('Computer chose Paper')
    elif (compchoice == 3):
        print('Computer chose Scissors')
    elif (compchoice == 4):
        print('Computer chose Lizard')
    elif (compchoice == 5):
        print('Computer chose Spock')

    if (choice == compchoice):
        print('Tie')
    elif (choice == 1 and compchoice == 2):
        print('Paper covers Rock')
    elif (choice == 1 and compchoice == 3):
        print('Rock destorys Scissors')
    elif (choice == 1 and compchoice == 4):
        print('Rock crushes Lizard')
    elif (choice == 1 and compchoice == 5):
        print('Rock crushes Spock')
    elif (choice == 2 and compchoice == 1):
        print('Paper covers Rock')
    elif (choice == 2 and compchoice == 3):
        print('Scissors cuts Paper')
    elif (choice == 2 and compchoice == 4):
        print('Lizard eats Paper')
    elif (choice == 2 and compchoice == 5):
        print('Paper disproves Spock')
    elif (choice == 3 and compchoice == 1):
        print('Rock crushes Scissors')
    elif (choice == 3 and compchoice == 2):
        print('Scissors cuts Paper')
    elif (choice == 3 and compchoice == 4):
        print('Scissors decapitates Lizard')
    elif (choice == 3 and compchoice == 5):
        print('Scissors smashes Spock')
    elif (choice == 4 and compchoice == 1):
        print('Rock crushes Lizard')
    elif (choice == 4 and compchoice == 2):
        print('Lizard eats Paper')
    elif (choice == 4 and compchoice == 3):
        print('Scissors decapitates Lizard')
    elif (choice == 4 and compchoice == 5):
        print('Lizard poisons Spock')
    elif (choice == 5 and compchoice == 1):
        print('Rock crushes Spock')
    elif (choice == 5 and compchoice == 2):
        print('Paper disproves Spock')
    elif (choice == 5 and compchoice == 3):
        print('Spock smashes Scissors')
    elif (choice == 5 and compchoice == 4):
        print('Lizard poisons Spock')
    else:
        print('Invalid choice')
    print('Do you want to play again? (y/n)')
    while True:
        try:
            play = input()
            if play == 'y' or play == 'n':
                break
        except ValueError:
            print("Please Enter Y/N")
            continue
    if (play == 'n' or play == 'N'):
        print('Thank you for playing!')
        newgame = False