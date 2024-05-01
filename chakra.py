import turtle
from turtle import *

# Defining a turtle instance 
t = turtle.Turtle()
speed(18000)

# Initially penup
t.penup()
t.goto(-400, 250)
t.pendown()

# Big Blue Circles
t.penup()
t.goto(0, -60)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(60)
t.end_fill()

# Big White Circle
t.penup()
t.goto(0, 50)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(-50)
t.end_fill()

# Spokes
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
t.pencolor("navy")
for _ in range(24):
    t.forward(60)
    t.backward(60)
    t.left(360/24)  # Adjusted angle for correct spoke direction
t.hideturtle()
turtle.done()
