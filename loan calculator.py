#!/usr/bin/env python3
##Anthony Miklos
##COP2002.C02
##Loan calculator

import math as m
from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc

##variables

## x = y/(1-1/(1 + z)^w)
##main
def main():
        again = "y"
        while again.lower() == "y":
                display()
                us_input()
                print()
                again = input("Continue (y/n): ")
                print()
       
##displaying the purpose of the program
def display():
    print("Monthly Payment Calculator")
    
##Get user input
def us_input():
    print("DATA ENTRY")
    lnAmt = Decimal(input("Loan amount:             "))
    inRat = Decimal(input("Yearly interest rate:    "))
    numYr = Decimal(input("Number of years:         "))
    print()
    calcu(lnAmt, inRat, numYr)
    
##making the calculations
def calcu(lnAmt, inRat, numYr):
    monthlyRate = inRat/100/12
    compoundedMonthlyRate = (1 + monthlyRate) ** (numYr * 12)
    multiplier = (compoundedMonthlyRate * monthlyRate) / (compoundedMonthlyRate - 1)
    monPa = multiplier * lnAmt
    finish(lnAmt, inRat, numYr, monPa)

##printing out formatted results                
def finish(lnAmt, inRat, numYr, monPa):
    result = lc.setlocale(lc.LC_ALL, "")
    if result == "C":
        lc.setlocale(lc.LC_ALL, "en_US")
    line = "{:30} {:>15}"
    print("FORMATTED RESULTS")
    print(line.format("Loan amount:",lc.currency(lnAmt, grouping=True)))
    print(line.format("Yearly interest rate:" , str(inRat) + "%"))
    print(line.format("Number of years:" , numYr))
    print(line.format("Monthly payment:", lc.currency(monPa, grouping=True)))

if __name__ == "__main__":
    main()
    
