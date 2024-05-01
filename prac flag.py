import turtle
from turtle import*
t=turtle.Turtle
speed(0)
t.penup()
t.goto(-400,250)
t.pendown()
#orange rectangle 
#green rectangle
t.color("orange")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.forward(167)
#green rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
