# ----------------------------------------------------------
# --------               PROGRAM 1                 ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after having completed this
# program
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Hours spent on program 1: 0.083333
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


# write your python program for the mad libs problem here

import time
#Welcome Greeting
print "Welcome to Mad libs!"
time.sleep(1)

#gets nouns and verbs
noun = raw_input("Please enter a noun: ")
time.sleep(0.75)
verb1 = raw_input("Next, enter a verb: ")
time.sleep(0.75)
verb2 = raw_input("Lastly, enter one more different verb: ")
time.sleep(0.75)

#prints the mad lib
print "Okay, generating mad lib"
time.sleep(1)
print "If it", verb1, "like a", noun, "and", verb2, "like a", noun + ", then it probably is a", noun + "."
time.sleep(5)
