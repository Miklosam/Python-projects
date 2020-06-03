#!/usr/bin/env python3
#Anthony Miklos
#COP2002.C02
#contact manager

#with open("contacts.csv", "r") as view_con: #statement to grab the list
                                             #can use "w" for write mode

#seperate read and write lines and creat them into functions for calling
#using try to create error checking.
import csv

FILENAME = "contacts.csv"

#create main trying simplified main
def main():
    file_check()
        #display main title
    display_main()
        #get user input and start functions based on user input.
    command_menu()

#define command menu
def command_menu():
    command = ""
    while command != "exit":
        if command == "list":
            list_contacts()
        elif command == "view":
            view()
        elif command == "add":
            add()
        elif command == "del":
            del_con()
        command = str(input ("\nCommand: "))
    print ("Bye!")

#display command menu
def display_main():
    print ("Contact Manager")
    print ("\nCOMMAND MENU")
    print ("list - Display all contacts")
    print ("view - View a contact")
    print ("add  - Add a contact")
    print ("del  - Delete a contact")
    print ("exit - Exit program")
    
def file_check():
    try:
        with open(FILENAME, "r") as view_con:
            re_con = csv.reader(view_con)
    except:
        print("Could not find contacts file!")
        print("Starting new contacts file...")
        print()
        with open("contacts.csv", "w"):
            pass

#def for displaying contacts as a list
def list_contacts():
    try:
        with open(FILENAME, "r") as view_con:
            re_con = csv.reader(view_con)
            y = 0
            for x in re_con:
                y = y + 1
                print (str(y) + "." , x[0])
            if y == 0:
                print("There are no contacts in the list")
    except:
        print("There are no contacts in the list.")
       
#viewing a specific contact from the list
def view():
    try:
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            full_file =  list(reader)
            try:
                con_num = int(input("number: "))
                if con_num <= len(full_file) and con_num >= 1:
                    print ("Name:  " , full_file[con_num -1][0])
                    print ("Email: " , full_file[con_num -1][1])
                    print ("Phone: " , full_file[con_num -1][2])
                else:
                    print ("Invalid contact number.")
            except:
                print("Invalid integer")
    except:
        print("There are no contacts to view")
#adding contact function
def add():
    with open(FILENAME, "r", newline="") as file:
        fullfile = list(csv.reader(file))
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        name = input("Name: ")
        email = input("email: ")
        phone = input("phone: ")
        fullfile.append([name, email, phone])
        writer.writerows(fullfile)

#removes contact
def del_con():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            full_file =  list(reader)
            try:
                con_num = int(input("Input contact number: "))
                if con_num <= len(full_file) and con_num >= 1:
                    print ("Your contact: " , full_file[con_num - 1][0] , " was deleted.")
                    del full_file[con_num - 1]
                else:
                    print ("Invalid contact number")
            except:
                print("Invalid integer")
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(full_file)
    except:
        print("could not open file for editing")



if __name__ == "__main__":
    main()

