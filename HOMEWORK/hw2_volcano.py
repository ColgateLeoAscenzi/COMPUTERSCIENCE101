# ----------------------------------------------------------
# HW 2       PROGRAM 4
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Time Spent: 1
# ----------------------------------------------------------


# Write your program for the volcano pattern here

import time
#sets up loop for easy testing
play = True
while play:
    size = int(raw_input("Enter a size: "))
    #cloud plumes
    for line in range(size):
        space1 = (size*4)-((line))+1
        space2 = (size*3)-(line*2)
        print " "*space1+"("+" "*space2+")"
    #top of the mountain
    for line in range(1):
        space1 = ((size*3)-(line)+1)
        underscore = size
        print " "*space1+"("+"_"*underscore+")"
    for line in range((size*3)):
        space1 = ((size*3)-(line+1)+1)
        ayyy = 2+line*2+(size-1)
        print " "*space1+"/"+"A"*ayyy+"\\"
    #loops if Y, not if N
    resp = raw_input("Would you like to make another pyramid? (Y/N) ")
    if resp == "Y":
        play == True
    elif resp == "N":
        play == False
        print "Later!"
time.sleep(2)
         
