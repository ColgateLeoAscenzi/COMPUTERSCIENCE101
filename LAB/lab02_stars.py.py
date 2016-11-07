#Leo Ascenzi

import time
play = True
while play:
    
    length = int(raw_input("Give me a length of a base of a pyramid! "))
             
    size = (length+1)/2#converts length of base to height (number of rows)
    count = 1
    for line in range(size):
        spaces = line+(size-count)
        stars = (line+(line+1))
        count = count + 2
        print " "*spaces+"*"*stars
    time.sleep(1)
    resp = raw_input("Test again (Y/N)")
    if resp == "Y":
        play = True
    elif resp =="N":
        play = False
    else:
        print "You didn't enter Y or N"

if play == "False":
    time.sleep(0.5)
    print "Okay, goodbye!"
    
             
