import turtle
import math

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

turtle.speed(0)
turtle.bgcolor("black")
turtle.color("#f73487")
turtle.penup()

# Use smaller steps and k in radians from 0 to 2*pi
for i in range(0, 360, 1):
    k = math.radians(i)
    x = hearta(k) * 20
    y = heartb(k) * 20
    turtle.goto(x, y)
    turtle.pendown()

turtle.hideturtle()

# Save drawing to file
ts = turtle.getscreen()
ts.getcanvas().postscript(file="heart.ps")

turtle.done()
