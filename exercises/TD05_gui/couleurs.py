def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


import tkinter as tk
import random 

racine = tk.Tk() # Création de la fenêtre racine
racine.title("couleurs degradé")

canvas = tk.Canvas(racine, bg="black", height=256, width=256)
canvas.grid(row=1, column=1,rowspan=3)


 
button1= tk.Button(racine, text= "Aléatoire",font=("Algerian", "20"),fg="blue")
button1.grid(column=0, row=1)
button2= tk.Button(racine, text= "Dégradé Gris",font=("Algerian", "20"), fg="blue")
button2.grid(column=0, row=2)
button3= tk.Button(racine, text= "Dégradé 2D",font=("Algerian", "20"), fg="blue")
button3.grid(column=0, row=3)

racine.mainloop()