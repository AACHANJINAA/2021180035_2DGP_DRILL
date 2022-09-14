import turtle

cnt = 1
dis = 100
while (1):
    turtle.forward(dis)
    if cnt == 30:
        break;
    if cnt % 5 == 0 :
        turtle.right(180)
        turtle.forward(dis * 5)
        turtle.right(90)
        turtle.forward(dis)
        turtle.right(90)
    cnt += 1;
    
turtle.right(90)
turtle.forward(dis*5)
cnt = 1

while (1):
    if cnt == 6:
        break;
    turtle.right(90)
    turtle.forward(dis)
    turtle.right(90)
    turtle.forward(dis*5)
    turtle.right(180)
    turtle.forward(dis*5)
    cnt += 1

turtle.exitonclick()
