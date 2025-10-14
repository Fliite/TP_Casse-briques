""" 
fichier contenant toute les fonctions nécéssaire pour le casse brique 

"""


def quitter():
    root.destroy()

def demarrer():
    global score
    score = 0
    score_label.config(text=f"Score: {score}")

def GoPrarameteres():
    import old.FenetreParametres as p
    root.destroy()
    p.settings.mainloop()

# Fonction pour revenir à la fenêtre principale
def GoBack():
    import old.FenetreParametres as p
    p.settings.destroy()
    root.mainloop()