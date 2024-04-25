# Créé par Marie SENGLER, le 31/12/2022 en Python 3.7
from tkinter import*
import math

largeur=900
hauteur=650
x1=0
y1=325
angle=0
rayon=30
x=rayon*(angle-math.sin(angle))
y=-rayon*(1-math.cos(angle))

def cycloide():
    global x1,y1,x,y,angle,rayon
    Canevas.create_arc(x1,y1+325,x,y+325,fill='red')
    x1,y1=x,y
    x=rayon*(angle-math.sin(angle))
    y=-rayon*(1-math.cos(angle))
    angle+=0.05
    fenetre.after(25,cycloide)


fenetre=Tk()
Canevas=Canvas(fenetre,height=hauteur,width=largeur,bg='white')
Canevas.pack(padx=5,pady=5)
ligne1 = Canevas.create_line(0, 325, 900, 325)
cycloide()
fenetre.mainloop()
