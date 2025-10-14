"""
BERRY Lucas
Objectif : Creer la fenetre des parametres. Elle pourra cahnger la vitesse de la balle, le nombre de vie, le son etc...
"""

import tkinter as tk

def GoBack():
    import old.FenetrePrincipale as FenetrePrincipale
    

def OuvrirParametres():
    settings = tk.Tk()
    settings.title("Casse-Briques")
    settings.geometry("600x400")
    settings.configure(bg="blue")

    # Bouton Retour en haut à gauche
    btn_back = tk.Button(settings, text="Retour", command=GoBack)
    btn_back.place(x=10, y=10, width=60, height=30)

    settings.mainloop()