import tkinter as tk
from classes import Brique, Balle

class PageJeu(tk.Frame):
    """Page qui contient la zone de jeu et les briques."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # --- Canvas principal du jeu ---
        self.canvasDeJeu = tk.Canvas(self, width=1080, height=720, bg="black")
        self.canvasDeJeu.pack(pady=20)

        # --- Bouton pour revenir à l'accueil ---
        boutonRetour = tk.Button(
            self,
            text="Retour à l'accueil",
            command=lambda: controller.show_frame("PageAccueil")
        )
        boutonRetour.pack(pady=10)

        # --- Création et affichage des briques ---
        self.creer_briques()

        """ Pour la balle """
        # --- Création de la balle (en attribut) ---
        self.balle = Balle()                      # crée la balle
        self.balle.set_position(100, 100)         # position initiale
        self.balle.draw(self.canvasDeJeu)         # l’affiche sur le Canvas
    
        # --- Démarre le mouvement (boucle d’animation) ---
        self._loop()
        
    def creer_briques(self):
        """Crée et affiche un petit mur de briques rouges."""
        cols, rows = 7, 3       # 5 colonnes, 3 lignes
        espace = 10             # espace entre briques
        start_x, start_y = 50, 50  # point de départ

        for r in range(rows):
            for c in range(cols):
                x = start_x + c * (75 + espace)
                y = start_y + r * (20 + espace)

                brique = Brique()
                brique.set_position(x, y)
                brique.draw(self.canvasDeJeu)

    

    def _loop(self):                  #boucle d'animation pour qu'elle le refasse en boucle
        """Met à jour la position de la balle en continu."""
        self.balle.step(self.canvasDeJeu, 1080, 720)  # la fait bouger
        self.after(16, self._loop)  # relance la fonction après 16 ms (~60 FPS)