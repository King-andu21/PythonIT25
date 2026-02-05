def my_boner(a, b):
    c = a + b
    return c
    print("Tere Peter Griffin")
print(my_boner(2, 3))
some_list = ["big","weld","hunghorse","bigbonerdownthelane","longhorseee"]

def pikim_sona(lis):
    prev_value = 0
    sona = ""
    for i in lis:
        if len(i) > prev_value:
            prev_value = len(i)
            sona = i
    return(sona)

sona= pikim_sona(some_list)
print(f"pikim sõna: {sona}")

def length(e):
        return len(e)

def kolm_pikimat_sona(lis):
    if len(lis) > 2:
        lis.sort(key=length, reverse=True)
    return(lis[0:3])
print(kolm_pikimat_sona(some_list))

word_to_check = "Wawa Wowo"
def starting_letter_detector(check):
    check = [check[0] for check in check.split()]
    print(check)
    letter1 = check[0]
    letter2 = check[1]
    if letter1 == letter2:
        return True
    else:
        return False
print(starting_letter_detector(word_to_check))
word_to_check = "Big Chungus"
print(starting_letter_detector(word_to_check))

import turtle
import random
turtle.speed(0)
turtle.penup()
turtle.goto(-400,0)
turtle.pendown()
def ring(amount):
    print("drawing: ring")
    for i in range(amount):
            turtle.pendown()
            turtle.circle(40)
            turtle.penup()
            turtle.forward(80)
def viisnurk(amount):
    print("drawing: viisnurk")
    for i in range(amount):
        for i in range(6):
            turtle.pendown()
            turtle.forward(40)
            turtle.left(72)
        turtle.penup()
        turtle.forward(60)
def ruut(amount):
    print("drawing: ruut")
    for i in range(amount):
        for i in range(4):
            turtle.pendown()
            turtle.forward(40)
            turtle.left(90)
        turtle.penup()
        turtle.forward(60)
def shape_writer(shape,amount):
    amount = int(amount)
    a = 0
    if shape == "ring":
        ring(amount)
    if shape == "viisnurk":
        viisnurk(amount)
    if shape == "ruut":
        ruut(amount)
    if shape == "suvaline":
        print("drawing: random")
        for i in range(amount):
            random2 = random.randint(1,3)
            turtle.penup()
            turtle.goto(random.randint(-300,300),random.randint(-300,300))
            if random2 == 1:
                turtle.pendown()
                ring(1)
            if random2 == 2:
                turtle.pendown()
                viisnurk(1)
            if random2 == 3:
                turtle.pendown()
                ruut(1)
    go_again = input("go again?:y/n")
    if go_again == "y":
        sel_shape = input("shape to draw: ")
        sel_amount = input("amount: ")
        shape_writer(sel_shape,sel_amount)
    if go_again == "n":
        turtle.bye()
sel_shape = input("shape to draw: ")
sel_amount = input("amount: ")
shape_writer(sel_shape,sel_amount)
turtle.done()