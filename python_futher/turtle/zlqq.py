import turtle

if __name__ == '__main__':
    turtle.setup(600, 400, )
    t = turtle.Turtle()
    t.pencolor("red")

    # Z
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.forward(100)
    t.right(120)
    t.forward(200)
    t.left(120)
    t.forward(100)
    # L
    t.penup()
    t.goto(-100, 120)
    t.pendown()
    t.right(90)
    t.forward(193)
    t.left(90)
    t.forward(200)
    # Q
    t.penup()
    t.goto(-40, 0)
    t.pendown()
    t.circle(50)

    t.penup()
    t.goto(-40, 0)
    t.pendown()
    t.right(90)
    t.forward(75)
    # Q
    t.penup()
    t.goto(60, 0)
    t.pendown()
    t.left(90)
    t.circle(50)

    t.penup()
    t.goto(60, 0)
    t.pendown()
    t.right(90)
    t.forward(75)

    t.penup()
    t.goto(1000,0)

    turtle.done()