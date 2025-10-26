import tkinter as tk
from tkinter import messagebox
from classeBalle import Balle
from classeRaquette import Raquette
from classeBrique import Brique
import random, math

class JeuCasseBrique(tk.Tk):
    '''La classe principale qui gère les différentes pages (frames).
    Les pages parametres, jeu, accueil sont des frames qui héritent de tk.Frame.
    Ce sont des onglets que l'on peut afficher ou cacher.
    '''
    def __init__(self, root):
        '''
        Initialise le jeu : fenêtre, canevas, contrôles et objets du jeu.
        Entrée : informations liée à la fenêtre principale
        Sortie : aucune car fait une boucle
        '''
        # référence à la fenêtre principale
        self.Racine = root
        # titre de la fenêtre
        self.Racine.title("Jeu de casse-briques")
        # On peut changer les dimensions du canevas à sa guise
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
        self.InitObjets()
        self.Running = False # indicateur si la boucle de jeu tourne
        self.LierTouches()
        self._Rafraichissement = 16  # délai entre déclenchement de la boucle en ms (~60 FPS)
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
        # dictionnaire de briques
        self.Briques = {}
        self.ScoreVar.set(0)
        self.ViesVar.set(3)
        self.CreerBriques()

    def CreerBriques(self, lignes=10, colonnes=10, espace=2, EspaceSuperieur=50):
        '''
        Crée une grille de briques en haut du canevas. calcul en tenant compte de la taille de la fenetre
        Entrée : informations liée aux briques
        Sortie : aucune 
        '''
        LBrique = (self.Largeur - espace * (colonnes + 1)) / colonnes
        HBrique = 22    
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

    def LierTouches(self):
        '''Lie les touches clavier aux actions de la raquette et du jeu.'''
        self.Racine.bind("<KeyPress-Left>", lambda e: self.Raquette.GoRaquette(-self.Raquette.vitesse))
        self.Racine.bind("<KeyPress-Right>", lambda e: self.Raquette.GoRaquette(self.Raquette.vitesse))
        self.Racine.bind("<KeyRelease-Left>", lambda e: self.StopRaquette(-self.Raquette.vitesse))
        self.Racine.bind("<KeyRelease-Right>", lambda e: self.StopRaquette(self.Raquette.vitesse))
        self.Racine.bind("<space>", lambda e: self.Demarer()) # espace -> démarrer/relancer la partie

    def StopRaquette(self, expect):
        '''Arrête la raquette uniquement si sa vitesse correspond à la direction attendue. évite d'arrêter la raquette si l'autre touche est encore maintenue '''
        if self.Raquette.vx == expect:
            self.Raquette.GoRaquette(0)

    def Demarer(self):
        '''Démarre la boucle du jeu. Si y a pas de briques, réinitialise le plateau.'''
        if not self.Running:
            self.Running = True
            if not self.Briques: # si toutes les briques ont été détruites, on réinitialise l'écran
                self.Canevas.delete("all")
                self.InitObjets()
            # positionne la balle au-dessus de la raquette
            px, py = self.Raquette.centre()
            self.Balle.Position(px, py - 30)
            # petite vitesse initiale
            speed = getattr(self.Balle, "vitesseBalle", 5) * 0.6
            # vitesse aléatoire vers le haut : on choisit vx aléatoire et on calcule vy négatif
            vx = random.uniform(-speed, speed)
            vy = -math.sqrt(max(0.0, speed * speed - vx * vx))
            self.Balle.VerifierVitesse(vx=vx, vy=vy)

    def Boucle(self):
        '''Boucle périodique qui met à jour l'état du jeu quand il tourne.
        On a cree cette fonction pour gerer la fluidité et pour eviter que le jeu plante quand on quitte.
        '''
        # si le jeu est en cours, on met à jour une frame
        if self.Running:
            self.Update()
        # réenclenche la boucle après (rafraichissement) ms
        self.Racine.after(self._Rafraichissement, self.Boucle)

    def Update(self):
        '''Met à jour la position des objets et gère les collisions et la sortie.'''
        self.Raquette.deplacement()
        self.Balle.Deplacer()
        self.CollisionsMur()
        self.CollisionsRaquette()
        self.CollisionsBriques()
        self.VerifierSortie()

    def CollisionsMur(self):
        '''Gère la réflexion de la balle sur les bords du canevas.'''
        x1, y1, x2, y2 = self.Balle.Coordonnees()
        if x1 <= 0 and self.Balle.vx < 0:    # collision gauche
            self.Balle.RebondX()
        if x2 >= self.Largeur and self.Balle.vx > 0:        # collision droite
            self.Balle.RebondX()
        if y1 <= 0 and self.Balle.vy < 0:        # collision haut
            self.Balle.RebondY()

    def CollisionsRaquette(self):
        '''Gère les collisions entre la balle et la raquette.'''
        # trouve les objets qui chevauchent la balle
        CollisionsBalle = self.Canevas.find_overlapping(*self.Balle.Coordonnees())
        CoordsRaquette = self.Raquette.id
        # si on touche la raquette et que la balle descend
        if CoordsRaquette in CollisionsBalle and self.Balle.vy > 0:
            # réflexion selon la règle d'angle de la raquette
            self.Balle.RebondRaquette(self.Raquette.coordonnees())
            # on repositionne la balle au-dessus de la raquette pour éviter qu'elle colle
            bx1, by1, bx2, by2 = self.Balle.Coordonnees()
            px1, py1, px2, py2 = self.Raquette.coordonnees()
            overlap = by2 - py1
            if overlap > 0:
                self.Canevas.move(self.Balle.id, 0, -overlap - 1)

    def CollisionsBriques(self):
        '''Gère les collisions entre la balle et les briques et supprime les briques touchées.'''
        CollisionsL = []
        # Il y a collision si la balle et une brique se chevauchent (grace à overlapping())
        for CollisionsBalle in self.Canevas.find_overlapping(*self.Balle.Coordonnees()):
            if CollisionsBalle in self.Briques:
                CollisionsL.append(CollisionsBalle)
        for Objet in CollisionsL:
            brique = self.Briques.get(Objet)
            if not brique: #si la collision n'est pas avec une brique
                continue
            # calcul des recouvrements pour déterminer l'axe de réflexion
            Boite = self.Balle.Coordonnees() #boite qui encadre la balle ronde. (on la considère carrée)
            brect = self.Canevas.coords(Objet)
            ChevauchementX = max(0, min(Boite[2], brect[2]) - max(Boite[0], brect[0])) # recouvrement en x : c est la largeur du chevauchement
            ChevauchementY = max(0, min(Boite[3], brect[3]) - max(Boite[1], brect[1])) # recouvrement en y : c est la hauteur du chevauchement
            if ChevauchementX > ChevauchementY:
                self.Balle.RebondY() #rebond vertical
            else:
                self.Balle.RebondX() #rebond horizontal
            brique.DetruireBrique()
            del self.Briques[Objet]
            # augmentation du score
            self.ScoreVar.set(self.ScoreVar.get() + 10)
            # si plus de briques, victoire
            if not self.Briques:
                self.Victoire()
            # on gère au plus une brique par frame pour éviter des réflexions multiples
            break

    def VerifierSortie(self):
        '''Vérifie si la balle est sortie par le bas et gère la perte de vie / reset.'''
        x1, y1, x2, y2 = self.Balle.Coordonnees()
        # si la balle est sortie en bas
        if y1 > self.Hauteur:
            vies = self.ViesVar.get() - 1
            self.ViesVar.set(vies)
            # pause de la boucle jusqu'au redémarrage
            self.Running = False
            if vies <= 0:
                # si plus de vies -> défaite
                self.Defaite()
            else:
                # repositionne la balle et attend l'utilisateur pour redémarrer
                px, py = self.Raquette.centre()
                self.Balle.Position(px, py - 30)

    def Victoire(self):
        '''Affiche la boîte de dialogue de victoire et arrête le jeu.'''
        self.Running = False
        messagebox.showinfo("Victoire", f"Bravo ! Score: {self.ScoreVar.get()}")
        # on conserve le canevas pour permettre de relancer

    def Defaite(self):
        '''Affiche la boîte de dialogue de défaite et réinitialise le jeu.'''
        messagebox.showinfo("Défaite", f"Perdu ! Score: {self.ScoreVar.get()}")
        # réinitialisation du canevas et des objets
        self.Canevas.delete("all")
        self.InitObjets()