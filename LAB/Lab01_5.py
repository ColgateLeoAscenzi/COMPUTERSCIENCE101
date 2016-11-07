import time


#responses are floats
response1 = float(raw_input("Enter the first number: ")) #names response1 as an input and asks user for a number
time.sleep(0.5) #waits half a second to seem more human

response2 = float(raw_input("Enter the second number: ")) #names response2 as an input and asks user for a number
time.sleep(0.5) #waits half a second to seem more human

response3 = float(raw_input("Enter the third number: ")) #names response3 as an input and asks user for a number
#average is also a float
average_response = float((response1+response2+response3)/3) #sums the users numbers and divides the sum by 3

time.sleep(2) #waits two seconds to seem more human, rather than instantly printing as the user enters the third number

print("The average is %s" % average_response)

time.sleep(3)
