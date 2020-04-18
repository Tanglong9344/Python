import turtle

turtle.setup(500,500)
t = turtle.Turtle()
t.color('green')
t.speed(1)
t.goto(0,0)
for i in range(4):
    t.forward(100)
    t.left(90)  # 逆时针旋转90度
turtle.done()