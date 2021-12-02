import tkinter as tk
import random

N= int(input("combien de cercles voulez vous?"))
liste= ["blue", "green", "black", "yellow", "magenta", "red"] 
P,h = 500, 500

racine= tk.Tk()
racine.title("CERCLE CONCENTRIQUE")

canvas= tk.Canvas(racine,bg= "black", height=P, width= h)
canvas.grid()

Xm=P//2
Ym=h//2

index_color=0

for i in range(N):
    xpi=Xm*i//N
    ypi = i*Ym//N
    xqi= h - Xm*i//N
    yqi= P - i*Ym//N
    canvas.create_oval(xpi,ypi,xqi,yqi , fill=liste[index_color])
    index_color +=1
    if index_color==len(liste):
        index_color=0

    

racine.mainloop()

