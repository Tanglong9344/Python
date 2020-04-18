import turtle

def polygon(side_num):
    side_length = 100
    angle = 360.0 / side_num
    for i in range(side_num):
        t.forward(side_length)
        t.right(angle)



if __name__ == '__main__':
    turtle.screensize(600, 600,'black')
    t = turtle.Turtle()
    t.pencolor('black')
    t.goto(0,200)
    t.speed(10000)
    t.pencolor('white')
    for i in range(3,13):
        polygon(i)
    turtle.done()