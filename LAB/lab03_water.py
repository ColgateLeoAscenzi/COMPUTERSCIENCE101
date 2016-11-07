#Leo Ascenzi

temp = (raw_input("How many degrees is the temperature of the water?: "))
region = "nowhere" #very important variable
degree = str(raw_input(" Is this in Celsius or Farenheit? (C/F): "))

#sets variable to Celsius
if degree in "cC":
    region = "tea"

#sets variable to farenheit
elif degree in "fF":
    region = "freedom"
else:
    print "Enter a 'C' or 'F' next time!"
    region = "usererror"

if region == "tea":
    if temp>100:
        print "Your water is currently gas!"
    elif temp<0:
        print "You water is currently solid!"
    else:
        print "Your water is currently liquid!"

elif region == "freedom":
    if temp>212:
        print "Your water is currently gas!"
    elif temp<32:
        print "Your water is currently solid!"
    else:
        print "Your water is currently liquid!"


