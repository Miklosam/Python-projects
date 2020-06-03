#!/usr/bin/env python3
#""" Project Statement The guessing game has four errors.
##Find and correct the errors so that the user can set an upper
##limit to the range of numbers, it gets a random number in that range,
##and allows the user to guess until correct. It should display 'too high'
##or 'too low' hints. ---------------------------------------------------
##----------------------When you fix the program, upload the working program
##and list, as comments, the errors you found and fixed. Error 1: Error 2:
##    Error 3: Error 4:

import random

def main(): #error 1 no colon
    display_title()
    again = "y"
    while again.lower() == "y":
        limit = set_limit()
        play_game(limit)
        again = input("Play again? (y/n): ")
        print()
        print("Bye!")

def display_title():
    print("Guess the number!")
    print()

def set_limit():
    limit = int(input("Enter the upper limit for the range of numbers: ")) #Error 5 imput was one line below print statement.
    return limit

def play_game(limit):
    number = random.randint(1, limit)
    guess = 0 #error 4 guess and count not initially defined
    count = 0
    print("I'm thinking of a number from 1 to " + str(limit) + "\n")
    while True:
        guess = int(input("Your guess: "))

        if guess < number:
            count = count + 1 #error 3 counter after print statement
            print("Too low.")
            
            
        if guess > number: #error 2 did not want to be equal to
            count = count + 1 #error 3
            print("Too high.")
            
            
        elif guess == number:
            count = count + 1 #error 3
            print("You guessed it in " + str(count) + " tries.\n")
            return



# if started as the main module, call the main function
if __name__ == "__main__":
    main()
