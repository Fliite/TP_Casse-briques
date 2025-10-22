import tkinter as tk
from classeBrique import Brique

class Application(tk.Tk):
    '''La classe principale qui gère les différentes pages (frames).
    Les pages parametres, jeu, accueil sont des frames qui héritent de tk.Frame.
    Ce sont des onglets que l'on peut afficher ou cacher.
    '''
    def __init__(self, racine):
        '''
        Initialise le jeu : fenêtre, canevas, contrôles et objets du jeu.
        Entrée : informations liée à la fenêtre principale
        Sortie : aucune car fait une boucle
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

    def InitObjets(self):
        '''
        Crée la raquette, la balle, réinitialise le score/vies et crée les briques.
        Entrée : informations liée au jeu
        Sortie : aucune 
        '''
        # raquette positionnée au centre bas
        self.Raquette = Raquette(self.Canevas, self.Largeur/2, self.Hauteur - 40)
        # balle positionnée juste au-dessus de la raquette
        self.Balle = Balle(self.Canevas, self.Largeur/2, self.Hauteur - 60)
        # dictionnaire id_canvas -> brique
        self.Briques = {}
        # réinitialisation des compteurs
        self.ScoreVar.set(0)
        self.ViesVar.set(3)
        # création des briques
        self.CreerBriques()

    def CreerBriques(self, lignes=10, colonnes=10, espace=2, EspaceSuperieur=50):
        '''
        Crée une grille de briques en haut du canevas.
        Entrée : informations liée aux briques
        Sortie : aucune 
        '''
        # calcul de la largeur d'une brique en tenant compte des marges
        LBrique = (self.Largeur - espace * (colonnes + 1)) / colonnes
        # hauteur fixe des briques
        HBrique = 22
        # palette de couleurs par ligne
        couleurs = ["red","orange","yellow","green","cyan","lightgreen"]
        for r in range(lignes):
            for c in range(colonnes):
                # coordonnées de la brique
                x1 = espace + c * (LBrique + espace)
                y1 = EspaceSuperieur + r * (HBrique + espace)
                x2 = x1 + LBrique
                y2 = y1 + HBrique
                # création de l'objet Brique et stockage par id canvas
                brique = Brique(self.Canevas, x1, y1, x2, y2, color=couleurs[r % len(couleurs)])
                self.Briques[brique.id] = brique

    def StopRaquette(self, expect):
        '''
        Arrête la raquette uniquement si sa vitesse correspond à la direction attendue.
        Entrée : informations liée à la raquette
        Sortie : aucune
        '''
        # évite d'arrêter la raquette si l'autre touche est encore maintenue
        if self.Raquette.vx == expect:
            self.Raquette.GoRaquette(0)

    def Demarer(self):
        '''
        Démarre la boucle du jeu. Si pas de briques, réinitialise le plateau.
        Entrée : informations liée au jeu
        Sortie : aucune
        '''
        # si la boucle n'était pas en cours, on la lance
        if not self.Running:
            self.Running = True
            # si toutes les briques ont été détruites, on réinitialise l'écran
            if not self.Briques:
                self.Canevas.delete("all")
                self.InitObjets()
            # positionne la balle au-dessus de la raquette
            px, py = self.Raquette.center()
            self.Balle.set_position(px, py - 30)
            # petite vitesse initiale
            self.Balle.reset_velocity(vx=self.Balle.vitesseBalle * 0.6, vy=-abs(self.Balle.vitesseBalle * 0.6))

    def Boucle(self):
        '''
        Boucle périodique qui met à jour l'état du jeu quand il tourne.
        Entrée : informations liée au jeu
        Sortie : aucune
        '''
        # si le jeu est en cours, on met à jour une frame
        if self.Running:
            self.Update()
        # réenclenche la boucle après _TauxTick ms
        self.Racine.after(self._TauxTick, self.Boucle)

    def Update(self):
        '''
        Met à jour la position des objets et gère les collisions et la sortie.
        Entrée : informations liée au jeu
        Sortie : aucune
        '''
        # déplacement de la raquette selon sa vitesse
        self.Raquette.move()
        # déplacement de la balle
        self.Balle.move()
        # collisions avec les murs
        self.CollisionsMur()
        # collisions avec la raquette
        self.CollisionsPaddle()
        # collisions avec les briques
        self.CollisionsBriques()
        # vérifie si la balle est sortie par le bas
        self.VerifierSortie()

    def show_frame(self, page_name):
        '''Affiche la frame demandée'''
        frame = self.frames[page_name]
        frame.tkraise()

#permet de lancer l'application de manière autonome, utile pour les tests
if __name__ == "__main__":
    app = Application()
    app.mainloop()