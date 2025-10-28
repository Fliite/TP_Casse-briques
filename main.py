'''
Cree par Lucas BERRY et Baudry DEROUBAIX modifié en dernier le 22/10/25
But : lancer le programme principal du jeu de casse-briques.
'''

import tkinter as tk
from ProgrammeJeu import JeuCasseBrique

if __name__ == "__main__":
    root = tk.Tk() # création de la fenêtre principale
    game = JeuCasseBrique(root) # création de l'objet jeu
    root.mainloop() # boucle principale de la fenêtre