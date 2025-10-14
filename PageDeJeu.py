import tkinter as tk
from classes import Brique

class PageJeu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="black", width=1280, height=720)

        label = tk.Label(self, text="Page du jeu")
        label.pack(pady=20)

        self.canvas = tk.Canvas(self, width=1000, height=600, bg="red")
        self.canvas.pack(pady=10)

        bouton_retour = tk.Button(self, text="Retour à l'accueil",command=lambda: controller.show_frame("PageAccueil"))
        bouton_retour.pack()

        def _create_bricks(self):
            cols, rows = 10, 6         # 10 colonnes, 6 lignes
            pad = 12                   # marge entre briques
            top = 60                   # décalage du haut
            bL, bH = 100, 24          # largeur/hauteur brique

            start_x = (W - (cols*bL + (cols-1)*pad)) // 2  # centrer le mur

            for r in range(rows):
                for c in range(cols):
                    x = start_x + c*(bL + pad)
                    y = top     + r*(bH + pad)
                    b = Brique()
                    b.set_position(x, y)
                    b.draw(self.canvas)
                    self.briques.append(b)