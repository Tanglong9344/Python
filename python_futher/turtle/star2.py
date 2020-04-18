import turtle

turtle.setup(500, 500)
t = turtle.Turtle()
t.color('red')
t.speed(1)
while True:
    for i in range(30):
        t.forward(i * 15)
        t.right(144)
    t.goto(0,0)
turtle.done()