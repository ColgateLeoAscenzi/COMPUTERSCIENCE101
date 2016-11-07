# ----------------------------------------------------------
# HW 6, Program 3
# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name: Leo Ascenzi
# Hours spent on this program: 0.333
# Collaborators and sources: N/A
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

#Greeting messages
ask_miles = "How many miles did you run today? "
start = "Nice start,"
after = "Good work!"
congrats = "Congrats on completing your marathon!"
congrats_special = "Congrats on completing your marathon with no training!"


#Important Running Variables
totalmiles = 0.0
days = 0

#Handles the first input
first_time_switch = True
tempmiles = float(raw_input(ask_miles))
totalmiles += tempmiles

if tempmiles < 26.2:
    print start, "so far you have run", totalmiles, "miles"
    print
    days += 1
else:
    print congrats_special


#The rest of the input, breaks if user runs marathon
while True:
    #Breaks if it's 26.2 from the first input
    if tempmiles == 26.2:
        break
    else:
        #Breaks if it's 26.2 before adding
        tempmiles = float(raw_input(ask_miles))
        if tempmiles == 26.2:
            break
        else:
            #Adds to the total miles and days
            totalmiles += tempmiles
            days += 1
            print after, "So far you have run", totalmiles, "miles in", days, "days."
            print

if days > 1:
    #Prints the congrats message only if you've been training for more than 1 day
    print congrats
    print "During your training you ran", totalmiles, "miles in", days, "days."
    print "That's an average of", int(totalmiles/days), "miles per day."
    
###Test Cases
##
##How many miles did you run today? 26.2
##Congrats on completing your marathon with no training!
##
##
##How many miles did you run today? 9
##Nice start, so far you have run 9.0 miles
##
##How many miles did you run today? 13.1
##Good work! So far you have run 22.1 miles in 2 days.
##
##How many miles did you run today? 18
##Good work! So far you have run 40.1 miles in 3 days.
##
##How many miles did you run today? 26.2
##Congrats on completing your marathon!
##During your training you ran 40.1 miles in 3 days.
##That's an average of 13 miles per day.
