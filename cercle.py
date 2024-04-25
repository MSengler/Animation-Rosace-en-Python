from tkinter import*
import math


largeur = 1000
hauteur = 1000
rayon = 10
angle = 0
angle1 = 0
angle2 = 0

x = largeur//2
y = hauteur//2
vitesse = 4
dx = vitesse*math.cos(angle)
dy = vitesse*math.sin(angle)


x1 = x+20
y1 = y+20
vitesse1 = 2
dx1 = vitesse1*math.cos(angle)
dy1 = vitesse1*math.sin(angle)

x2 = x1-20
y2 = y1-20
vitesse2 = 4
dx2 = vitesse2*math.cos(angle)
dy2 = vitesse2*math.sin(angle)


def deplacement():
    global x,y,dx,dy,angle,angle1, angle2, rayon,largeur,hauteur,x1,y1,dx1,dy1,x2,y2,dx2,dy2
    x += dx
    y += dy
    x1 += dx+dx1
    y1 += dy+dy1
    x2 += dx+dx1+dx2
    y2 += dy+dx2+dy2


    dx = vitesse*math.cos(angle)
    dy = vitesse*math.sin(angle)
    dx1 = vitesse1*math.cos(angle1)
    dy1 = vitesse1*math.sin(angle1)
    dx2 = vitesse2*math.cos(angle2)
    dy2 = vitesse2*math.sin(angle2)

    angle += 0.06
    angle1 += 0.08
    angle2 -= 0.075

    Canevas.coords(Balle3, x2-rayon, y2-rayon, x2+rayon, y2+rayon)
    #Canevas.coords(Balle2, x1-rayon, y1-rayon, x1+rayon, y1+rayon)
    #Canevas.coords(Balle, x-rayon, y-rayon, x+rayon, y+rayon)

    #Canevas.create_arc(x, y, x+dx, y+dy,fill='green')
    #Canevas.create_arc(x1, y1,x1+dx1+dx, y1+dy1+dy,fill='red')
    Canevas.create_arc(x2, y2,x2+dx2+dx1+dx, y2+dy2+dy1+dy,fill='blue')
    fenetre.after(50, deplacement)






fenetre=Tk()
Canevas=Canvas(fenetre,height=hauteur,width=largeur,bg='white')
Canevas.pack(padx=5,pady=5)

#Balle=Canevas.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,width=1,fill='green')
#Balle2=Canevas.create_oval(x1-rayon,y1-rayon,x1+rayon,y1+rayon,width=1,fill='red')
Balle3=Canevas.create_oval(x2-rayon,y2-rayon,x2+rayon,y2+rayon,width=1,fill='blue')
deplacement()

fenetre.mainloop()