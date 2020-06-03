#!/usr/bin/env python3
#Anthony Miklos
#COP2002.C02
#lists and arrays

#list
inventory = ["wooden staff", "wizard hat", "cloth shoes"]

#create main
def main():
    print ("The Wizard Inventory program")
    print ("\nCOMMAND MENU")
    print ("show - Show all items")
    print ("grab - Grab an item")
    print ("edit - Edit an item")
    print ("drop - Drop an item")
    print ("exit - exit program")
    #get user input and start functions based on user input.
    command = ""
    while command != "exit":
        if command == "show":
            show(inventory)
        elif command == "grab":
            grab(inventory)
        elif command == "edit":
            edit(inventory)
        elif command == "drop":
            drop(inventory)
        command = str(input ("\nCommand: "))
    print ("Bye!")

#def for displaying inventory contents
def show(inventory):
    y = 0
    for x in inventory:
        y = y + 1
        print (str(y) + "." , x)
       
#add an item to inventory
def grab(inventory):
    if len(inventory) < 4:
        grabber = str(input ("Name: "))
        inventory.append(grabber)
        print(grabber, "was added")
    else:
        print ("You can't carry any more items. Drop something first.")
        
        
#change corrosponding item in inventory
def edit(inventory):
    editor = int(input ("Number: "))
    if editor <= len(inventory) and editor >= 1:
        update_name = str(input("Updated name: "))
        inventory[editor - 1] = update_name
        print ("item number" , editor , "was updated")
    else:
        print ("Not a valid item")

    
#removes specific item from inventory
def drop(inventory):
    trash = int(input ("Number: "))
    if trash <= len(inventory) and trash >= 1:
        trash =  trash -1
        print(inventory[trash], "was dropped")
        inventory.remove(inventory[trash])
    else:
        print ("Not a valid item")



if __name__ == "__main__":
    main()
