import turtle

a = turtle.Turtle()
a.pensize(3)
b = turtle.Screen()

a.fillcolor('yellow')
a.begin_fill()
for _ in range(3):
    a.forward(100)
    a.left(120)
a.end_fill()

a.forward(100)

a.fillcolor('blue')
a.begin_fill()
for _ in range(2):
    a.forward(100)
    a.left(90)
a.forward(100)
a.end_fill()

a.fillcolor('white')
a.begin_fill()
for _ in range(2):
    a.forward(40)
    a.right(90)
    a.forward(35)
    a.right(90)
a.end_fill()

a.penup()
a.forward(200)
a.pendown()

a.fillcolor('blue')
a.begin_fill()
for _ in range(2):
    a.forward(80)
    a.left(90)
    a.forward(25)
    a.left(90)
a.end_fill()

a.forward(60)
a.right(90)

a.fillcolor('yellow')
a.begin_fill()
a.circle(20)
a.end_fill()

turtle.done()
