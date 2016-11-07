import math
import time
pi_val = math.pi
print "Welcome to the digits of py."
print
digits = int(raw_input("Please enter the digit to which you wish to truncate it! "))

print str(pi_val)[:digits+2]

time.sleep(1)
digits1 = int(raw_input("Give me another number, so we can try again! "))
pi_int = int(pi_val*10**digits1)
pi_rounded = float(float(pi_int)/(10**digits1))
print pi_rounded

time.sleep(2)
