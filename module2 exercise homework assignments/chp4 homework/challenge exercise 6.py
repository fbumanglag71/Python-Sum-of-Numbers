## Author: Francisco Bumanglag
## Project: Sum of Numbers
## Assignment: Module 2 Project 3
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 24, 2023


#declare variable and set to zero 
total = 0

#while loop true statement
while True: 
    number = int(input("Enter a postive number.  To terminate the program, enter a negative number: "))

    if number < 0:
        break               #term program if user enters negative number
    
    total += number         #counter for total variable

#print function -- display summation of numbers
print("The sum of all the numbers you entered is:", total)





