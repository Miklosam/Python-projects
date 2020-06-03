#!/usr/bin/env python3

# Anthony Miklos
# module 3 homework. change calculator

print ("Change Calculator")
#initial variables
quarter = 25
dime = 10
nickle = 5
penny = 1

#loop statement
choice = "y"
while choice.lower() == "y": 
    dollar_amt = input ("\nEnter dollar amount (for example, .56, 7.85): ") 
    dollar_amt = float(dollar_amt) * 100

    #calculator

    # find number of quarters
    quarter_back = int(dollar_amt / quarter)
    subtotal = (dollar_amt) - (quarter * quarter_back)

    # find number of dimes
    dime_back = int(subtotal / dime)
    subtotal = (subtotal) - (dime * dime_back)

    # find number of nickles
    nickle_back = int(subtotal / nickle)
    subtotal =  (subtotal) - (nickle * nickle_back)

    # find number of pennies
    penny_back = int(subtotal / penny)
    subtotal = (subtotal) - (penny * penny_back)

    # printing out change
    print("\nQuarters: ", quarter_back)
    print("Dimes:    ", dime_back)
    print("Nickles:  ", nickle_back)
    print("Pennies:  ", penny_back, "\n")
    choice = input ("Continue? (y/n): ")

print ("\nBye!")


