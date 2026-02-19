import turtle
import random

aken = turtle.Screen()
aken.bgcolor("lightblue")
aken.setup(width=600, height=600)
aken.tracer(0)  # Keelab automaatse ekraani värskenduse



#
# ristkülik
#
ristkylik = turtle.Turtle()
ristkylik.shape("square")  # loome ruudu
ristkylik.shapesize(stretch_wid=1, stretch_len=5)  # Venitame ristkülikuks
ristkylik.penup()
ristkylik.color("black")
ristkylik.goto(ristkylik.xcor(), -250)
# liikumis kiirus
ristkyliku_kiirus = 20

# ristküliku liikumisfunktsioonid
def liigu_vasakule():
    x = ristkylik.xcor()
    if x > -280:
        ristkylik.setx(x - ristkyliku_kiirus)

def liigu_paremale():
    x = ristkylik.xcor()
    if x < 280:
        ristkylik.setx(x + ristkyliku_kiirus)
#
# ring
#

ring = turtle.Turtle()
ring.shape("circle")
ring.penup()
ring.speed('fastest')

# ringi kiirus ja nurk
kiirus = 2
ring.setheading(random.randint(0,360))

def peegelda_porkumisel():
    nurk = ring.heading()
    if ring.xcor() >= 300 or ring.xcor() <= -300:  # Põrkumine vasakult või paremalt
        uus_nurk = 180 - nurk
        if uus_nurk < 0:
            uus_nurk += 360
        ring.setheading(uus_nurk)
    if ring.ycor() >= 300 or ring.ycor() <= -300:  # Põrkumine ülalt või alt
        uus_nurk = 360 - nurk
        ring.setheading(uus_nurk)

def ring_liigu():
    ring.forward(kiirus)
    peegelda_porkumisel()
    aken.update()  # Värskenda ekraani pärast liikumist
    aken.ontimer(ring_liigu, 20)  # `ring_liigu` käivitamine 20ms pärast

def ristkyliku_kokkuporkamine():
    # if ring.xcor() =
    nurk = ring.heading

ring_liigu()

aken.listen()
aken.onkeypress(liigu_vasakule, "Left")
aken.onkeypress(liigu_paremale, "Right")

aken.mainloop() 