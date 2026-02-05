tous = 140
kasv = 15
tous_protsent = 0


#---o---
# Harjutus 6.1
#---o---
import turtle
import math
# turtle.pendown()
# turtle.forward(440)
nurk = math.radians(53)
maja_korgus = 4.4 
kaugus = maja_korgus / math.tan(nurk)
pikkus = round(math.sqrt(math.pow(maja_korgus,2) + math.pow(kaugus,2)),2)
print(nurk ,maja_korgus, kaugus, pikkus)
kordaja = 50
turtle.speed(0)
turtle.right(53)
turtle.forward(pikkus*kordaja)
turtle.goto(0,0)
turtle.left(53)
turtle.right(90)
turtle.forward(maja_korgus*kordaja)
turtle.left(90)
turtle.forward(kaugus*kordaja)
turtle.done()
# 0.3.12.2025 Andre
#---o---
# Harjutus 6.2
#---o---