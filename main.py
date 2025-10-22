import tkinter as tk
from PageParametres import PageParametres
from classeBalle import Balle
from classeRaquette import Raquette
from classeBrique import Brique

class Application(tk.Tk):
    '''La classe principale qui gère les différentes pages (frames).
    Les pages parametres, jeu, accueil sont des frames qui héritent de tk.Frame.
    Ce sont des onglets que l'on peut afficher ou cacher.
    '''
    def __init__(self):
        '''
        Initialise le jeu : fenêtre, canevas, contrôles et objets du jeu.
        Entrée : information de la fenêtre
        Sortie : aucune
        '''
        # référence à la fenêtre principale
        self.Racine = racine
        # titre de la fenêtre
        self.Racine.title("Jeu de casse-briques")
        # dimensions du canevas
        self.Largeur, self.Hauteur = 900, 600
        # création du canevas où tout est dessiné
        self.Canevas = tk.Canvas(self.Racine, width=self.Largeur, height=self.Hauteur, bg="black")
        self.Canevas.pack()

        # barre d'outils en haut pour boutons et affichage
        self.HautFrame = tk.Frame(self.Racine)
        self.HautFrame.pack(fill="x")
        # bouton démarrer
        self.DemarerBtn = tk.Button(self.HautFrame, text="Démarrer", command=self.Demarer)
        self.DemarerBtn.pack(side="left", padx=5, pady=3)
        # bouton quitter
        self.QuitterBtn = tk.Button(self.HautFrame, text="Quitter", command=self.Racine.quit)
        self.QuitterBtn.pack(side="left", padx=5, pady=3)
        # variables Tk pour score et vies
        self.ScoreVar = tk.IntVar(value=0)
        self.ViesVar = tk.IntVar(value=3)
        tk.Label(self.HautFrame, text="Score:").pack(side="left", padx=(20,0))
        tk.Label(self.HautFrame, textvariable=self.ScoreVar).pack(side="left")
        tk.Label(self.HautFrame, text="  Vies:").pack(side="left", padx=(20,0))
        tk.Label(self.HautFrame, textvariable=self.ViesVar).pack(side="left")

        # initialisation des objets du jeu (raquette, balle, briques)
        self.InitObjets()
        # indicateur si la boucle de jeu tourne
        self.Running = False
        # liaisons des touches clavier
        self.LierTouches()
        # délai entre ticks en ms (~60 FPS)
        self._TauxTick = 16
        # démarre la boucle périodique
        self.Boucle()

#permet de lancer l'application de manière autonome, utile pour les tests
if __name__ == "__main__":
    app = Application()
    app.mainloop()