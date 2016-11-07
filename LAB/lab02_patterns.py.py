#Leo Ascenzi

import time

num = int(raw_input("Please type a whole number: "))#Asks for a number (comments assume number is 3)
for i in range(num): #prints 0 1 2
    print i,

print
time.sleep(0.5)#rests

#num2 = int(raw_input("Okay. Please type another whole number! ")
for i in range(num): #prints 1 2 3
    print i+1,

print
time.sleep(0.5)

#num3 = int(raw_input("Again!!! ")
for i in range(num):#prints 10 20 30
    print (i+1)*10,

print
time.sleep(0.5)

#num4 = int(raw_input("Give me another one! ")
for i in range(num):#prints 1... 2... 3...
    print str(i+1)+"...",

    
print
time.sleep(0.5)

#num5 = int(raw_input("One more time!!! ")
for i in range(num):#prints 0 -1 -2
    print (i)*(-1),

    
print
time.sleep(0.5)

count = 0
#print("Alright, last time! ")
for i in range(num):#prints 3 2 1 blast off!
    print(i+(num-count)),
    count = count + 2

print " blast off!"

time.sleep(5)

