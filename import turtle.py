import turtle
from turtle import*
#defining a turtle instance
t=turtle.Turtle()
speed(18000)
#intially penup
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
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()

#big blue circles
t.penup()
t.goto(70, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()
# Big White Circle
t.penup()
t.goto(60, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()
# Spokes
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("navy")
t.pensize(2)
for i in range(24):
	t.forward(60)
	t.backward(60)
	t.left(15)
turtle.done()

