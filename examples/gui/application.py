import tkinter as tk

def affichage():
    """ Modifie le texte d'un label. """
    global cpt
    cpt += 1
    label.config(text="tu as cliqué " + str(cpt)+ " fois")

cpt = 0
racine = tk.Tk() # Création de la fenêtre racine
label = tk.Label(racine, text="texte avant de cliquer sur le bouton",
                  padx=20, pady=20, font = ("helvetica", "30") 
                )
label.grid(row=0, column=0)
bouton = tk.Button(racine, text="Un bouton sur lequel cliquer", 
                    command=affichage, font = ("helvetica", "30") 
                  ) # création du widget
bouton.grid(row=1, column=0) # positionnement du widget
racine.mainloop() # Lancement de la boucle principale