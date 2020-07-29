import random

def roll(num):
    return random.randint(1, num)


choice = input("Enter a max value for the roll (Enter a nonzero positive integer): ")
times = input("Enter the number of times you want to roll the dice (Enter a nonzero positive integer): ")

if choice.isdigit():

    max = int(choice)
    if max == 0:
        print("\nError: the number you gave is 0 for the max value. \nPlease Try Again")
    
    else:

        if times.isdigit():
            amount = int(times)

            if amount == 0:
                print("\nError: the number you gave is 0 for the number of times. \nPlease Try Again")
            else:
                for i in range(amount):
                    print(roll(max))
        
        else:
            print("\nError: you did not enter a positive integer for the number of times.\nPlease Try Again.")  
else:

    print("\nError: you did not enter a positive integer for the max value.\nPlease Try Again.")