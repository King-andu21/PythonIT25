# Autor: Andre Pook
import turtle
#---o---

# Harjutus 3.1 (Tervitus)

#---o---
nimi="Andre Pook"
vanus=int(16)
keskmine_hinne= float(5.7)
print(nimi ,",", vanus ,"aastat vana ja keskmine hinne on", keskmine_hinne)
#---o---

# Harjutus 3.2 (Ostunimekiri)

#---o---
toode= "porgandeid"
kogus=int(3)
hind=float(5.35)

print("Soovin "+ toode+" "+ str(kogus)+", mille tüki hind on "+ str(hind))
#---o---

# Harjutus 3.3 (Reisiplaan)

#---o---
sihtkoht= "Soome"
Paevade_arv= int(5)
oobimise_hind= float(30.50)
print(sihtkoht, "reis kestab",Paevade_arv,"päeva ja üks öö maksab", oobimise_hind, "eurot")
#---o---

# Harjutus 3.4 (Lemmikraamat)

#---o---
raamatu_pealkiri = "Veebibeebi"
raamatu_autor = "Imre Tard"
raamat = raamatu_pealkiri + " " + raamatu_autor
lehekylgede_arv = 50
hindamisskoor = 8.8
print("Minu lemmikraamat on"+raamat+", mis on"+ str(lehekylgede_arv) +"pikk ja mille ma hindad" +str(hindamisskoor)+ "punktiga")
#---o---

# Harjutus 3.5 (Unistuste auto)

#---o---
auto_mark = "Opel"
auto_mudel = "Corsa"
auto = auto_mark + " " + auto_mudel
tootmisaasta = 2011
hind = 9999.99
print("minu unistuste auto on",auto,"aastast",tootmisaasta,", mille hind on ", hind,"eurot")
#---o---

# Harjutus 3.6 (Python Turtle ruut)

#---o---
kylje_pikkus = 50
nurk = 90
kujund_värv = "red"
drawing = 0
kordaja = 1.5
turtle.color(kujund_värv)
for drawing in range(3):
    turtle.pendown()
    turtle.forward(kylje_pikkus)
    turtle.left(nurk)
    turtle.forward(kylje_pikkus)
    turtle.left(nurk)
    turtle.forward(kylje_pikkus)
    turtle.left(nurk)
    turtle.forward(kylje_pikkus)
    turtle.left(nurk)
    turtle.penup()
    turtle.forward(kylje_pikkus*kordaja)
#---o---

# Harjutus 3.7 (Python Turtle kolmnurk)

#---o---
kylje_pikkus = 50
nurk = 120
kujund_värv = "blue"
drawing = 0
kordaja = 1.5
turtle.color(kujund_värv)
for drawing in range(3):
    turtle.pendown()
    turtle.forward(kylje_pikkus)
    turtle.left(nurk)
    turtle.forward(kylje_pikkus)
    turtle.left(nurk)
    turtle.forward(kylje_pikkus)
    turtle.left(nurk)
    turtle.penup()
    turtle.forward(kylje_pikkus*kordaja)
turtle.done()