import turtle
import math

# Heart funksiyaları
def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

# Ekranı qur
turtle.bgcolor("black")
turtle.color("#f73487")
turtle.pensize(2)
turtle.speed(0)
turtle.penup()

# Rəsmə başla
for i in range(0, 360):
    k = math.radians(i)  # dərəcəni radiana çevir
    x = hearta(k) * 20
    y = heartb(k) * 20
    turtle.goto(x, y)
    if i == 0:
        turtle.pendown()

turtle.hideturtle()
turtle.done()

# Rəsmi .eps (və ya .ps) faylına yaz
ts = turtle.getscreen()
ts.getcanvas().postscript(file="heart.eps")