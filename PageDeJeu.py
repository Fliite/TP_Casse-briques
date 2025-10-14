import tkinter as tk
from classes import Brique

class PageJeu(tk.Frame):
    '''Classe représentant la page de jeu'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Page du jeu")
        label.pack(pady=20)

        canvasDeJeu = tk.Canvas(self, width=720, height=480, bg="black")
        canvasDeJeu.pack(pady=10)

        boutonRetour = tk.Button(self, text="Retour à l'accueil",command=lambda: controller.show_frame("PageAccueil"))
        boutonRetour.pack()