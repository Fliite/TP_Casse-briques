import tkinter as tk
from FonctionCasseBrique import *


root = tk.Tk()
root.title("Casse-Briques")
root.geometry("1280x720")

# Bouton Quitter en haut à droite
btn_quitter = tk.Button(root, text="Quitter", command=quitter)
btn_quitter.place(x=1200, y=10, width=60, height=30)

# Affichage du score
score = 0
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 16))
score_label.place(x=20, y=10)

# Bouton Paramètres en haut au centre
btn_parametres = tk.Button(root, text="Paramètres", command=GoPrarameteres)
btn_parametres.place(x=610, y=10, width=100, height=30)

# Bouton pour démarrer
btn_demarrer = tk.Button(root, text="Démarrer", command=demarrer)
btn_demarrer.place(x=500, y=10, width=60, height=30)

root.mainloop()