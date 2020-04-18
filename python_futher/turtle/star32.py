import turtle

def star(x,y,color,times):
    t.penup()
    t.goto(x,y)
    t.pencolor(color)
    t.pendown()
    for i in range(times):
        t.forward(50)
        angle = 180 - 360/times
        t.right(angle)

if __name__ == '__main__':
    turtle.setup(500, 500, )
    t = turtle.Turtle()
    star(-100,  100, 'red',   8)
    star(100,   100, 'green', 12)
    star(100,  -100, 'blue',  24)
    star(-100, -100, 'brown', 36)
    t.penup()
    t.goto(0, 0)
    turtle.done()