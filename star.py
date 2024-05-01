import turtle
from turtle import*
s=turtle.Turtle()
s.pencolor("black")
s.fillcolor("yellow")
s.begin_fill()
for i in range(5):
    s.forward(200)
    s.left(144)
s.end_fill()
turtle.done