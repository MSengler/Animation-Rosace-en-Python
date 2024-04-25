# Créé par Marie SENGLER, le 31/12/2022 en Python 3.7
from tkinter import*
import math

#Une épicycloïde est une courbe plane transcendante, trajectoire d'un point fixé à un cercle qui roule sans glisser sur un autre cercle dit directeur

largeur,hauteur=900,650

x1,y1=450,325
angle=0
r,R=50,100

x=(R+r)*math.cos(angle)-r*math.cos(angle*(R+r)/r)
y=(R+r)*math.sin(angle)-r*math.sin(angle*(R+r)/r)


xcercle=R*math.cos(angle)
ycercle=R*math.sin(angle)
x1cercle,y1cercle=450-R,325

def epicycloide():
    global x1,y1,x,y,angle,rayon,xcercle,ycercle,x1cercle,y1cercle
    Canevas.create_arc(x1+450,y1+325,x+450,y+325,fill='red')
    Canevas.create_arc(x1cercle+450,y1cercle+325,xcercle+450,ycercle+325,fill='blue')

    x1cercle,y1cercle=xcercle,ycercle
    x1,y1=x,y
    angle+=0.05

    x=(R+r)*math.cos(angle)-r*math.cos(angle*(R+r)/r)
    y=(R+r)*math.sin(angle)-r*math.sin(angle*(R+r)/r)
    xcercle=R*math.cos(angle)
    ycercle=R*math.sin(angle)

    fenetre.after(25,epicycloide)

fenetre=Tk()
Canevas=Canvas(fenetre,height=hauteur,width=largeur,bg='white')
Canevas.pack(padx=5,pady=5)
#ligne1 = Canevas.create_line(0, 325, 900, 325)
epicycloide()
fenetre.mainloop()
