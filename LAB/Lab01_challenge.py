
import time
import random

#Sets up the human like AI, and asks a random question every time
AI = random.randint(1,3)
if AI == 1:
    print "Please type a number with a decimal!"
elif AI == 2:
    print "Give me a decimal number please!"
elif AI == 3:
    print "Please enter a decimal number!"

#defines the response and prompts the user to enter a number
response = float(raw_input())

#defines the rounded response and does the math
rounded_response = int(response)+1

#makes the computer seem more human
a = "."
print "Calculating"
time.sleep(0.5)
print(a)
time.sleep(0.5)
print(a)
time.sleep(0.5)
print(a)
time.sleep(1)

#prints the users number rounded up
print "Response calculated!"
time.sleep(1)
print"The rounded up version of your number is: %s" % rounded_response

#adds a delay at the end for the user to reflect upon their answer
time.sleep(3)

