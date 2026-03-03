import turtle
screen = turtle.Screen()
text_turtle = turtle.Turtle()
text_turtle.left(90)
text_turtle.forward(20)
text_turtle.right(90)
text_turtle.write(0, font=("Arial", 16, "normal"))
turtle.speed(0)
def movement(length):
    cycles = length/10
    bigger = 5
    mult = 1
    for i in range(length+1):
        if bigger >= 5:
            text_turtle.forward(length/cycles*5)
            text_turtle.write(i+5, font=("Arial", 16, "normal"))
            mult = 2
            bigger = 0
        else:
            mult = 1
        turtle.left(90)
        turtle.forward(10*mult)
        turtle.right(180)
        turtle.forward(10*mult)
        turtle.left(90)
        turtle.forward(length/cycles)
        #mult = 1
        bigger +=1
length = int(screen.textinput("Sisestamine", "Joonlaua pikkus"))
movement(length)
turtle.done()
