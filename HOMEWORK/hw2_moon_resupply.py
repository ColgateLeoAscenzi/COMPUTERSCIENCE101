# ----------------------------------------------------------
# --------               PROGRAM 2                 ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent on program 2: 0.5
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# write your python program for the moon resupply problem here
import time
#Asks for variables
name = raw_input("What is your name? ")
total_water = float(raw_input("How much water do the colonists have left (in liters)? "))
depletion_rate = float(raw_input("How fast do the colonists drink water (in liters/day)? "))

#calculates how much time of each type based on hours, then subtracts previous value, and makes it an int to truncate
time_total =total_water/depletion_rate
days = int(time_total)
hours = int((time_total)*24-(days*24))
minutes = int((time_total*24*60)-(days*24*60)-(hours*60))
seconds = int((time_total*24*60*60)-(days*24*60*60)-(hours*60*60)-(minutes*60))

#tells ending time
print "%s, the colonists need supplies within", days, "days,", hours, "hours,", minutes, "minutes, and", seconds, "seconds."

time.sleep(5)
