#Leo Ascenzi
#Gets input
fraction = str(raw_input("Enter a fraction (ex:2/7): "))
#splits at /
split = fraction.split("/")
#sets variables
a = split[0]
b = split[1]

#accounts for 0
if float(b) == 0:
    print "Invalid input - the denominator cannot be zero!"

#calculates
else:
    print "Your decimal equivalent is:", (float(a)/float(b))
