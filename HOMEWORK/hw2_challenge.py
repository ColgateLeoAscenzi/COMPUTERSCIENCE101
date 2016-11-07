# ----------------------------------------------------------
# HW 2       PROGRAM Challenge
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Time Spent: 1.2
# ----------------------------------------------------------

import time
#makes a loop for testing purposes
play = True
print "Welcome to create an Imperial Star Destroyer!"
while play:

#imagining lines as rabbits helps me, all other variables are self explanatory
    
    #prints top destroyer
    scale = int(raw_input("Please enter a scale for your warship! "))
    truescale = scale*2
    for rabbits in range(0,((truescale/2)-1)):
        space1 = (((truescale/2)*3)-(rabbits+1)+1)-2*scale
        stars = 2*rabbits+1
        print " "*space1+"===="*stars
    #prints bottom of destroyer
    for rabbits in range((truescale/2),(truescale)):
        space2 = (-scale+rabbits+1)
        inversestars = (truescale*2-1)-2*rabbits
        print " "*space2+"===="*inversestars

    print "Would you like to make another Star Destroyer?"
    resp = raw_input()
    if "y" in resp or "Y" in resp or "yes" in resp or "Yes" in resp or "YES" in resp:
        play == True
    else:
        print "Later!"
        break
time.sleep(2)
    
