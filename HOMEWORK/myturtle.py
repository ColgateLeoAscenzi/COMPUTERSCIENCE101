# ----------------------------------------------------------
# HW 2       PROGRAM 3
# ----------------------------------------------------------
# Name:  Leo Ascenzi
# Time Spent: 4 hours
# ----------------------------------------------------------


import time
import turtle

#Asks for colors and side length
L = float(raw_input("Enter a sidelength for this christmas tree: ")) #l is used because "side_length" is hard to type
color1 = raw_input("Now enter the leaf color: ")
color2 = raw_input("Next, enter a color for the star: ")
color3 = raw_input("Also, enter a color for the ornaments: ")
print "One more thing, polygonal or star-like ornaments?(poly/star)"
polystar = raw_input("Star like ornaments only work for even numbers: ")
sides = int(raw_input("Lastly, enter the number of sides for the ornaments (3 to 20): "))
#Odd numbered stars and side numbers of over 20 mess it up

#Developer tip: Make leaf color gold, star color white, and polygon side 0 to draw a triforce!

#Defines the two new turtles
triforce = turtle.Turtle()
star = turtle.Turtle()
ornaments = turtle.Turtle()

#Starts drawing the triforce
triforce.color(color1)
triforce.begin_fill()

#Starts the first triangle
triforce.forward(L)
star.forward(L)
triforce.left(120)
star.left(120)
triforce.forward(L)
star.forward(L)
star.color(color2)
star.begin_fill()#star start
triforce.left(120)
star.right(48)
triforce.forward(L)
star.forward(L/2)
triforce.end_fill()#end of first triangle
star.left(144)
star.forward(L/2)

triforce.begin_fill()#start of second triangle
triforce.forward(L)
triforce.left(120)
star.left(144)
star.forward(L/2)
triforce.forward(L)
triforce.left(120)
star.left(144)
star.forward(L/2)
triforce.forward(L)
star.left(144)

star.forward(L/2)
triforce.backward(L)
triforce.right(60)
triforce.end_fill()#end of second triangle
star.end_fill()#star end

triforce.begin_fill()#last triangle start
triforce.forward(L)
triforce.right(120)
triforce.forward(L)
triforce.right(120)
triforce.forward(L)
triforce.end_fill()#last triangle end


#Draws 2 star-like ornaments
if polystar == "star":
    ornaments.forward(L/8)
    ornaments.left(90)
    ornaments.forward(L/8)
    ornaments.right(180)
    ornaments.begin_fill()
    for num in range(sides):#Draws the shape
        ornaments.color(color3)
        ornaments.forward(L/6)
        ornaments.left((180*(sides-2))/sides)
    ornaments.end_fill()
    ornaments.color(color1)#Needed so it wont show an ornament colored line
    ornaments.left(90)
    ornaments.forward((2*L)/3)
    ornaments.right(90)
    ornaments.forward(L/8)
    ornaments.begin_fill()
    for num in range(sides):#Draws second shape
        ornaments.color(color3)
        ornaments.forward(L/6)
        ornaments.left((180*(sides-2))/sides)
    ornaments.end_fill()
    
#Draws 2 polygonal ornaments  
elif polystar == "poly":
    ornaments.forward(L/8)
    ornaments.left(90)
    ornaments.forward(L/8)
    ornaments.right(180)
    ornaments.begin_fill()
    for num in range(sides):#Draws shape
        ornaments.color(color3)
        ornaments.forward(L/(2*sides))
        ornaments.left(180-((180*(sides-2))/sides))
    ornaments.end_fill()
    ornaments.color(color1)#Again, no visible line
    ornaments.left(180)
    ornaments.forward(L/16)
    ornaments.right(90)
    ornaments.forward((2*L)/3)
    ornaments.right(90)
    ornaments.forward(L/6)
    ornaments.begin_fill()
    for num in range(sides):#Draws second shape
        ornaments.color(color3)
        ornaments.forward(L/(2*sides))
        ornaments.left(180-((180*(sides-2))/sides))
    ornaments.end_fill()
else:
    print "You didn't specify poly/star"
    quit()

print "There is your tree!"

time.sleep(10) #Allows user to marvel at tree
