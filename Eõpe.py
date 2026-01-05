# Autor: Andre Pook
# Kuupäev: 05.01.2026
import turtle


# ---
# Esimene Muster
# ---
turtle.speed(0)
mustri_suurus = 100
for i in range(4):
    for i in range(3):
        turtle.forward(mustri_suurus)
        turtle.left(90)
        turtle.forward(mustri_suurus)
        turtle.right(90)
        turtle.forward(mustri_suurus)
        turtle.right(90)
    turtle.forward(mustri_suurus)
    turtle.left(90)
    turtle.forward(mustri_suurus)
    turtle.right(90)
    turtle.forward(mustri_suurus)

turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()
# ---
# Teine Muster
# ---
mustri_suurus = 120
for i in range(5):
    turtle.forward(mustri_suurus/2)
    turtle.left(120)
    turtle.forward(mustri_suurus)
    turtle.left(120)
    turtle.forward(mustri_suurus)
    turtle.left(120)
    turtle.forward(mustri_suurus/2)
    turtle.right(72)

turtle.done()