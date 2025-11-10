# Andre Pook (King_Andu)
#---o---

# Olümpiarõngad

#---o---
import turtle
import time

aken = turtle.Screen()
aken.setup(width=500, height=400)
print("akna laius: ", aken.window_width())
print("akna kõrgus: ", aken.window_height())
aken.title("Olümpiarõngad")

turtle.speed(0)
turtle.penup()
turtle.goto(-120,0) #blu

turtle.pendown()

turtle.pensize(6)
turtle.color("blue")
turtle.circle(50)

turtle.penup() #blu

turtle.goto(-10,0) #blackie

turtle.pendown()

turtle.color("black")
turtle.circle(50)

turtle.penup() #blackie

turtle.goto(100,0) # red

turtle.pendown()

turtle.color("red")
turtle.circle(50) # red

turtle.penup()

turtle.goto(-65,-50) #yel

turtle.pendown()

turtle.color("yellow")
turtle.circle(50)

turtle.penup() #yel

turtle.goto(45,-50) #green

turtle.pendown()

turtle.color("green")
turtle.circle(50) # green

#---o---

# Sinilill

#---o---
aken.clearscreen()
aken = turtle.Screen()
aken.setup(width=500, height=500)
print("akna laius: ", aken.window_width())
print("akna kõrgus: ", aken.window_width())
aken.title("Sinilill")
turtle.pensize(10)
turtle.speed(10)

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()

turtle.color("green")
turtle.goto(0,100)

turtle.penup()
turtle.goto(-13,20)
turtle.pendown()

turtle.begin_fill()
turtle.color("green", "green")
turtle.goto(-13,-20)
turtle.goto(-50,0)
turtle.goto(-13,20)
turtle.end_fill()

turtle.penup()
turtle.goto(0,50)
turtle.pendown()

turtle.begin_fill()
turtle.color("blue", "light blue")
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(0,85)
turtle.pendown()

turtle.begin_fill()
turtle.color("yellow", "yellow")
turtle.circle(15)
turtle.end_fill()

turtle.done()