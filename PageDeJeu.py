import tkinter as tk
from classes import Brique

class PageJeu(tk.Frame):
    """Page qui contient la zone de jeu et les briques."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # --- Canvas principal du jeu ---
        self.canvasDeJeu = tk.Canvas(self, width=1500, height=720)
        self.canvasDeJeu.pack(pady=20)

        #separer le canvas de jeu en deux parties
        self.canvas1 = tk.Canvas(self.canvasDeJeu, width=1080, height=720, bg="black")
        self.canvas1.pack(side=tk.LEFT)

        self.canvas2 = tk.Canvas(self.canvasDeJeu, width=400, height=720, bg="white")
        self.canvas2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # --- Bouton pour revenir à l'accueil ---
        boutonRetour = tk.Button(
            self.canvas2,
            text="Retour à l'accueil",
            command=lambda: controller.show_frame("PageAccueil")
        )
        boutonRetour.pack(pady=10)
        
        # --- Label pour afficher le score ---
        self.score = 0
        self.score_label = tk.Label(self.canvas2, text=f"Score: {self.score}", font=("Arial", 16))
        self.score_label.pack(pady=10)

        # --- Création et affichage des briques ---
        self.creer_briques()

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
                brique.draw(self.canvas1)