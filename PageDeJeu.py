import tkinter as tk
from classes import Brique

class PageJeu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="black", width=1280, height=720)

        label = tk.Label(self, text="Page du jeu")
        label.pack(pady=20)

        canvas = tk.Canvas(self, width=200, height=100, bg="red")
        canvas.pack(pady=10)



        bouton_retour = tk.Button(self, text="Retour à l'accueil",command=lambda: controller.show_frame("PageAccueil"))
        bouton_retour.pack()