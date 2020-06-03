#!/usr/bin/env python3
##Anthony Miklos

def main():
    homes = get_prices()
    print (homes)
    homes.sort()
    get_stats(homes)

def get_prices():
    homes = []
    num_homes = int(input("how many do you have? "))
    count = 1
    while count <= num_homes:
        home = float(input("Enter a price: "))
        homes.append(home)
        count += 1
    return homes

def get_stats(homes):
    sum = 0
    for x in homes:
        sum += x
    average =  sum/len(homes)
    print ("Average = " , average)
    print ("The max value is: " , max(homes))
    print ("The min value is: " , min(homes))
    if len(homes)%2 == 1:
        median_index = len(homes)//2
        median = homes[median_index]
        print ("Median value is " , median)
        #then an else statement to find even number median





if __name__ == "__main__":
    main()
