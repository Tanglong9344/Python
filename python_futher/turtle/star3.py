import turtle

turtle.setup(500, 500, )
t = turtle.Turtle()
# t.speed(1)
t.pencolor('white')
t.goto(-100,100)
t.pencolor("blue")
for i in range(8):
    t.forward(50)
    t.right(135)
t.goto(-50,100)
t.pencolor('white')
t.goto(100,100)
t.pencolor("green")
for i in range(12):
    t.forward(50)
    t.right(150)

t.pencolor('white')
t.goto(100,-100)
t.pencolor("red")
for i in range(24):
    t.forward(50)
    t.right(165)

t.pencolor('white')
t.goto(-100,-100)
t.pencolor("brown")
for i in range(36):
    t.forward(50)
    t.right(170)

t.pencolor('white')
t.goto(0,0)
turtle.done()