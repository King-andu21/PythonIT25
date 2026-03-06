import turtle
aken = turtle.Screen()
aken.title("Turtle Joonistamine")

def ekraanile_klikkimine(x, y):
   turtle.goto(x, y)
def object_creation(x,y):
   turtle.penup()
   turtle.goto(x,y)
   turtle.pendown()
   turtle.circle(10)
def reset(x,y):
   turtle.clear()
def red():
   turtle.color("red")
def green():
   turtle.color("green")
def blue():
   turtle.color("blue")
turtle.onkeypress(red, "r")
turtle.onkeypress(green, "g")
turtle.onkeypress(blue, "b")
aken.onscreenclick(object_creation, 1)
aken.onscreenclick(reset, 3)

aken.listen()
turtle.mainloop()
turtle.speed(0)