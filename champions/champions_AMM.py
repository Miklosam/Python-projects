#!/usr/bin/env python3
#Anthony Miklos
#COP2002.C02
#Champions display

import csv


def main():
    ## call import function
    winners = file_in("world_cup_champions.txt")
    print_table(winners)

def print_table(winners):
    print("FIFA World Cup Winners")
    print()
    print("Country       Wins   Years")
    print("=======       ====   =====")
    countries = list(winners.keys())
    countries.sort()
    line = "{:13} {:<6} {}"
    for country in countries:
        print(line.format(country, len(winners[country]), ", ".join(winners[country])))
    
    print()
def file_in(filename):
    winners = {}
    try:
        with open(filename, "r") as winners_file:
            reader = csv.reader(winners_file)
            next(reader, None)
            for line in reader:
                year = line[0]
                country = line[1]
                if country in winners:
                    old_years = winners[country]
                    old_years.append(year)
                else:
                    winners[country] = [year]
        return winners
    except:
        print("Could not find file!")
        exit()


if __name__ == "__main__":
    main()
