import tkinter as tk
import random 

racine = tk.Tk() # Création de la fenêtre racine
racine.title("MON DESSIN")

canvas = tk.Canvas(racine, bg="black", height=500, width=500)
canvas.grid(row=1, column=1,rowspan=3)
 # Lancement de la boucle principale

def cercle():
    x0= random.randint(0, 500)
    y0= random.randint(0,500)
    dessin= canvas.create_oval(x0 , y0 , x0 + 100, y0 +100, fill=("yellow"))
    return dessin

def carré():
    x1= random.randint(0, 500)
    y1= random.randint(0, 500)
    figure= canvas.create_rectangle(x1, y1, x1+100,  fill=("purple"))
    return figure



button1= tk.Button(racine, text= "cercle",font=("helvetica", "20"), command=cercle)
button1.grid(column=0, row=1)
button2= tk.Button(racine, text= "carré",font=("helvetica", "20"), command=carré)
button2.grid(column=0, row=2)
button3= tk.Button(racine, text= "croix",font=("helvetica", "20"))
button3.grid(column=0, row=3)
button4= tk.Button(racine, text= "choisir une couleur",font=("helvetica", "20"))
button4.grid(column=1, row=0)

racine.mainloop()
