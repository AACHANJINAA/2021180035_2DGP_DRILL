import turtle

turtle.reset()

y = -100
while y <= 400:
    turtle.penup()
    turlte.goto(0, y)
    turtle.pendown()
    turtle.goto(500, y)
    y += 100

x = 0
while x <= 500:
    turtle.penup()
    turlte.goto(x, -100)
    turtle.pendown()
    turtle.goto(x, 400)
    x += 100
