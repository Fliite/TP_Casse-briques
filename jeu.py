import tkinter as tk

class PageJeu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Page du jeu")
        label.pack(pady=20)

        background = tk.Canvas(self, width=1280, height=720, bg="black") # on cree un canvas en tant que background
        background.pack()

        canvas = tk.Canvas(self, width=200, height=100, bg="black")
        canvas.pack(pady=10)

        bouton_retour = tk.Button(self, text="Retour à l'accueil",command=lambda: controller.show_frame("PageAccueil"))
        bouton_retour.pack()