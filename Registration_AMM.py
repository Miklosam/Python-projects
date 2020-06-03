#!/usr/bin/env python3

# Anthony Miklos
# module 2 homework. registration program

print("Student Registration Form")
#fname = ""
#lname = "Williams"
#byear = 1973
#pword = "secret"
print ()
fname = input("First Name     ")
lname = input("Last Name      ")
byear = input("Birth Year   ")
pword = (fname + "*" + byear)
print ("Wlecome" + " " + fname + " " + lname + " ")
print ("Your password is   " + pword)

