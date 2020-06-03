#!/usr/bin/env python3
#Anthony Miklos
#Prime calculator

def main():
    print("Prime Number Checker")
    print()
    choice = "y"
    while choice.lower() == "y":
        number = get_input()
        print_factors(number)
        choice = input ("\nTry again? (y/n): ")
        print()
   
        

def print_factors(number):
    # Print the factors of given number (from 1 to the number)
    counter = 0
    print("The factors of your number are: ")
    for x in range(1, number + 1):
        if number % x == 0:
            print (x)
            counter = counter + 1
    if (counter > 2) or (number == 1):
        print (number , "is NOT a prime number.")
        print ("It has" , counter , "factors.")
    else:
        print (number , "is a prime number.")
                
def get_input():
    #ask for input and store
    return int(input("Please enter an integer between 1 and 5,000: "))



if __name__ == "__main__":
    main()
