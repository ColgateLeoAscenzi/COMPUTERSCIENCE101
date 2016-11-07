#Leo Ascenzi
import turtle
import time

times = int(raw_input("Please enter a number of squares you want for your spiral: "))
#ss stands for spiraly square
ss = turtle.Turtle()
L = 10
ss.pencolor("orchid")
squares = times*4
count = 0
if 0<times<25:
    ss.speed("normal")
    for i in range(squares):
        ss.forward(L+count)
        ss.left(90)
        count = count + L

elif 25<times<50:
    ss.speed(10)
    for i in range(squares):
       ss.forward(L+count)
       ss.left(90)
       count = count + L
else:
    ss.speed("fastest")
    for i in range(squares):
        ss.forward(L+count)
        ss.left(90)
        count = count + L

turtle.done()
time.sleep(5)
