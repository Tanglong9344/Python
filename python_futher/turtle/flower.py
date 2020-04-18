import turtle

turtle.screensize(600, 400, "green")
t = turtle.Turtle()
t.speed(10)
t.pencolor("red")
for i in range(200):
    t.forward(150)

    t.right(30)
    t.forward(20)

    t.left(60)
    t.forward(50)

    t.right(30)
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    t.right(2)
turtle.done()